"""Read the statute text of one Mississippi Code volume from Public.Resource.Org's scan (Internet Archive PDF, whose
text layer is the Internet Archive's Tesseract OCR) into sections.

    from ocr_parse import parse_volume
    secs = parse_volume(pdf_path)   # [{'num': '59-7-7', 'heading': ..., 'paras': [...], 'pages': [..]}]

Only the statute text is kept: each section runs from its heading ("§ 59-7-7. Heading.") to its HISTORY line. The
HISTORY line and everything after it up to the next section heading (cross references, editor's notes, amendment
notes, judicial decisions, opinions of the Attorney General, research references: the publisher's annotations) are
dropped, as are running heads and page numbers.
"""
from __future__ import annotations

import re
import statistics
from pathlib import Path

HEAD = re.compile(r'^[§$S]{1,2}\s*(\d{1,3})-(\d{1,3}[A-Z]?)-(\d{1,4}(?:\.\d+)?)\.\s*(.*)$')
HIST = re.compile(r'^(HISTORY|SOURCES?)\s*[:;.]', re.I)


def _key(num: str) -> tuple:
    t, c, s = num.split('-')
    cm = re.match(r'(\d+)([A-Z]?)', c)
    sm = re.match(r'(\d+)(?:\.(\d+))?', s)
    return (int(t), int(cm.group(1)), cm.group(2), int(sm.group(1)), int(sm.group(2) or 0))


def page_lines(page) -> list[dict]:
    """Text lines of one page, running head and page number removed, lines on one baseline merged."""
    H = page.rect.height
    raw = []
    for b in page.get_text('dict')['blocks']:
        for ln in b.get('lines', []):
            t = ''.join(s['text'] for s in ln['spans'])
            if not t.strip():
                continue
            x0, y0, x1, y1 = ln['bbox']
            if y1 < 0.085 * H or y0 > 0.935 * H:
                continue
            size = max(s['size'] for s in ln['spans'])
            raw.append({'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'size': size, 'text': t})
    merged: list[dict] = []
    for ln in raw:
        if merged and abs((ln['y0'] + ln['y1']) / 2 - (merged[-1]['y0'] + merged[-1]['y1']) / 2) < 3 \
                and ln['x0'] > merged[-1]['x1'] - 2 and ln['x0'] - merged[-1]['x1'] < 40:
            m = merged[-1]
            m['text'] = m['text'].rstrip() + ' ' + ln['text'].lstrip()
            m['x1'] = ln['x1']
            m['size'] = max(m['size'], ln['size'])
            continue
        merged.append(dict(ln))
    return merged


def normalise(s: str) -> str:
    s = s.replace(' ', ' ').replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('ﬁ', 'fi').replace('ﬂ', 'fl').replace('—', '—').replace('–', '-')
    return re.sub(r'\s+', ' ', s).strip()


def all_lines(pdf: str | Path, cache: str | Path) -> list[list[dict]]:
    """page_lines() of every page, kept in a JSON file (the text layer never changes)."""
    import json
    cache = Path(cache)
    if cache.exists():
        return json.loads(cache.read_text(encoding='utf-8'))
    import fitz
    doc = fitz.open(str(pdf))
    out = [page_lines(doc[n]) for n in range(doc.page_count)]
    tmp = cache.with_suffix('.part')
    tmp.write_text(json.dumps(out), encoding='utf-8')
    tmp.replace(cache)
    return out


def parse_volume(pages: list[list[dict]], first: str, last: str) -> tuple[list[dict], list[str]]:
    """Sections numbered first..last (inclusive, e.g. '59-1-1', '63-33-3'). Returns (sections, notes)."""
    lo, hi = _key(first), _key(last)
    secs: list[dict] = []
    notes: list[str] = []
    cur = None
    state = 'skip'   # 'head' (heading continuing), 'body', 'skip' (annotations)
    prev_key = None
    for pno in range(len(pages)):
        lines = pages[pno]
        if not lines:
            continue
        sizes = [ln['size'] for ln in lines if len(ln['text']) > 25]
        med = statistics.median(sizes) if sizes else 9.5
        xs = sorted(ln['x0'] for ln in lines if len(ln['text']) > 40)
        margin = xs[len(xs) // 10] if xs else min(ln['x0'] for ln in lines)
        rs = sorted(ln['x1'] for ln in lines if len(ln['text']) > 40)
        right = rs[len(rs) * 9 // 10] if rs else max(ln['x1'] for ln in lines)
        prev = None
        for ln in lines:
            t = normalise(ln['text'])
            m = HEAD.match(t)
            is_head = False
            if m and ln['size'] >= med * 1.07 and ln['x0'] < margin + 12:
                num = f'{m.group(1)}-{m.group(2)}-{m.group(3)}'
                try:
                    k = _key(num)
                except (AttributeError, ValueError):
                    k = None
                if k and lo <= k <= hi and (prev_key is None or k >= prev_key):
                    is_head = True
            if is_head:
                if cur:
                    secs.append(cur)
                prev_key = k
                prev = None
                cur = {'num': num, 'heading': m.group(4), 'paras': [], 'pages': [pno], 'closed': False}
                state = 'head'
                continue
            if cur is None:
                continue
            if state == 'hist':
                # the HISTORY paragraph runs on at the margin; the next annotation starts indented
                if ln['x0'] <= margin + 5 and len(cur['history']) < 2000:
                    cur['history'] += ' ' + t
                    continue
                state = 'skip'
            if state == 'head':
                if ln['size'] >= med * 1.07 and ln['x0'] > margin + 20 and not cur['paras']:
                    cur['heading'] = _join(cur['heading'], t, None)
                    continue
                state = 'body'
            if state == 'body':
                if HIST.match(t):
                    cur['closed'] = True
                    cur['history'] = t
                    state = 'hist'
                    continue
                if not re.search(r'[A-Za-z0-9]', t):
                    continue  # OCR specks at the margins
                if pno not in cur['pages']:
                    cur['pages'].append(pno)
                if prev is None or prev[0] != pno:
                    # first line on this page: a new paragraph only when indented from the margin
                    new = ln['x0'] > margin + 8
                else:
                    new = ln['x0'] > prev[1] + 6 or prev[2] < right - 30
                prev = (pno, ln['x0'], ln['x1'], right)
                if not cur['paras'] or new:
                    cur['paras'].append(t)
                else:
                    cur['paras'][-1] = _join(cur['paras'][-1], t, None)
    if cur:
        secs.append(cur)
    keep = []
    for s in secs:
        if re.match(r'\[?(Repealed|Reserved)\b', s['heading']):
            notes.append(f"{s['num']}: repealed or reserved, left out")
        elif not s['closed']:
            notes.append(f"{s['num']}: no HISTORY line found after the text, left out")
        elif not s['paras']:
            notes.append(f"{s['num']}: no text, left out")
        else:
            # An editorial bracket in the heading ("[Repealed effective July 1, 2025]") is the publisher's note.
            s['heading'] = re.sub(r'\s*\[[^\]]*(?:[Ee]ffective|[Rr]epealed)[^\]]*\]', '', s['heading']).strip()
            keep.append(s)
    return keep, notes


def _join(a: str, b: str, vocab) -> str:
    if a.endswith('-') and b[:1].islower():
        return a + '\x00' + b   # resolved later against the volume's own vocabulary
    return a + ' ' + b


def dehyphenate(secs: list[dict]) -> None:
    """A line-end hyphen before a lower-case letter is dropped when the joined word occurs elsewhere in the volume
    unhyphenated, and kept (as a real hyphen) otherwise."""
    words: dict[str, int] = {}
    for s in secs:
        for p in [s['heading'], *s['paras']]:
            for w in re.findall(r"[A-Za-z]+", p.replace('\x00', ' ')):
                words[w.lower()] = words.get(w.lower(), 0) + 1

    def fix(p: str) -> str:
        def rep(m):
            left, right = m.group(1), m.group(2)
            return left + right if (left + right).lower() in words else left + '-' + right
        return re.sub(r'([A-Za-z]+)-\x00([a-z]+)', rep, p).replace('\x00', '')
    for s in secs:
        s['heading'] = fix(s['heading'])
        s['paras'] = [fix(p) for p in s['paras']]
