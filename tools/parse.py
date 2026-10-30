"""Parse the cached Mississippi Constitution PDF (Secretary of State, annotated edition updated May 2022) into corpus.json.
Only the section number, heading and text are kept; SOURCES lines, NOTE paragraphs and annotations are dropped."""
import hashlib, json, os, re
import pymupdf
HERE = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(HERE, '.cache', 'Mississippi_Constitution.pdf')
URL = 'https://sos.ms.gov/content/documents/ed_pubs/pubs/Mississippi_Constitution.pdf'
FROM = '2022-05-01'

def fix(s):
    s = s.replace(' ', ' ').replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('–', '-').replace('—', '-')
    # the PDF's curly quotes arrive as U+FFFD: between letters it is an apostrophe, otherwise a double quote
    s = re.sub(r'(?<=[A-Za-z])�(?=[A-Za-z])', "'", s)
    return s.replace('�', '"')

def lines():
    d = pymupdf.open(PDF)
    out = []
    for p in list(d)[3:]:
        for l in p.get_text().split('\n'):
            out.append(fix(l).replace('\t', ' '))
    return out

DROP = re.compile(r'^\s*(\d+|MISSISSIPPI CONSTITUTION|ART\. \d+, SEC\. \d+[A-Za-z]*)\s*$')
def main():
    L = [l for l in lines() if not DROP.match(l)]
    blocks, cur, art = [], None, None
    for l in L:
        m = re.match(r'^SECTION\s+(\d+(?:\.\d+)?[A-Za-z]?)\.\s*$', l)
        a = re.match(r'^ARTICLE\s+(\d+)\s*$', l)
        if a:
            art = int(a.group(1)); cur = None; continue
        if m:
            cur = [art, m.group(1), []]; blocks.append(cur); continue
        if cur is not None:
            cur[2].append(l)
    best = {}
    for art, num, body in blocks:
        # drop the SOURCES / NOTE tail and all-capital running headings
        out = []
        for l in body:
            if re.match(r'^\s*(SOURCES|NOTE|Cross References|Cross-References|ANNOTATIONS|JUDICIAL DECISIONS)\b', l): break
            if re.match(r'^[A-Z][A-Z ,;&\'-]{4,}\s*$', l.strip()) : continue
            out.append(l)
        ne = [l.strip() for l in (x for x in out if x.strip())]
        t = 1
        while t < min(3, len(ne)) and not ne[t - 1].endswith('.'): t += 1
        title, rest = ' '.join(ne[:t]), [x for x in out if x.strip()][t:]
        paras, cur = [], ''
        for l in rest:
            cur = (cur + ' ' + l.strip()).strip()
            if l.endswith('  '):
                paras.append(cur); cur = ''
        if cur: paras.append(cur)
        paras = [re.sub(r'\s+', ' ', p) for p in paras if p]
        k = (art, num)
        if k not in best or sum(map(len, paras)) > sum(map(len, best[k][1])):
            best[k] = (title, paras)
    units = {}
    for (art, num), (title, paras) in best.items():
        key = 'art-%03d-sec-%s' % (art, re.sub(r'[^a-z0-9-]', '-', re.sub(r'(\d+)', lambda m: m.group().zfill(4), num.lower())))
        units[key] = {'label': f'Art. {art}, § {num}', 'kind': 'section', 'text': f'# Art. {art}, § {num}. {re.sub(chr(32)+"+", chr(32), title)}\n' + ''.join(p + '\n' for p in paras)}
    pre = '# Preamble\nWe, the people of Mississippi in convention assembled, grateful to Almighty God, and invoking his blessing on our work, do ordain and establish this constitution.\n'
    units = {'preamble': {'label': 'Preamble', 'kind': 'preamble', 'text': pre}, **dict(sorted(units.items()))}
    print(len(units))
    sha = hashlib.sha256(open(PDF, 'rb').read()).hexdigest()
    corpus = {'country': {'code': 'US-MS', 'name': 'United States (Mississippi)', 'slug': 'united-states-mississippi', 'lang': 'en', 'tz': 'America/Chicago', 'future_branch': 'future',
                          'publisher': {'name': 'Mississippi Secretary of State', 'email': 'sos@sos.ms.invalid'},
                          'default_in_force_rule': {'text': 'Only the Secretary of State edition updated May 2022 is online; it is the oldest (and only) version available and is dated 2022-05-01.', 'source': URL},
                          'licence_note': 'Constitution text from the Mississippi Secretary of State. Annotations, source notes and editorial notes are omitted.'},
              'sources': [{'name': 'The Constitution of the State of Mississippi, annotated, updated May 2022 (Mississippi Secretary of State)', 'url': URL, 'retrieved': '2026-10-30',
                           'licence': 'The text of a constitution is a law of the State and is not copyrightable (Georgia v. Public.Resource.Org, 2020). The Secretary of State\'s annotations are not copied.', 'notes': 'robots.txt for sos.ms.gov does not disallow /content/documents/.'}],
              'laws': {'ms-sos-2022-05': {'label': 'Secretary of State edition, updated May 2022', 'title': 'The Constitution of the State of Mississippi, adopted November 1, 1890, annotated, updated May 2022', 'kind': 'publisher',
                                            'enacted': FROM, 'published': FROM, 'url': URL, 'temporary_until': None, 'restores': None, 'note': None}},
              'acts': [{'slug': 'constitution', 'short': 'MS Const.', 'title': 'Constitution of the State of Mississippi (1890)', 'url': URL, 'first_law': None, 'earlier_laws': [],
                        'versions': [{'from': FROM, 'source_url': URL, 'sha256': sha, 'units': units}]}],
              'applies': [],
              'decisions': ['The Mississippi Code of 1972 is published only by LexisNexis under a click-through licence; no Mississippi Code text is included.',
                            'Only the Secretary of State edition updated May 2022 is online, so the Constitution has one version, the oldest available, dated 2022-05-01 from the edition\'s own "Updated May, 2022".',
                            'The PDF prints its curly quotation marks as U+FFFD; between two letters these were restored as apostrophes and elsewhere as double quotation marks.',
                            'SOURCES lines, NOTE paragraphs and annotations are dropped. A section heading that wraps over two lines in the PDF keeps its second line at the start of the text.'],
              'ai_use': ['none']}
    json.dump(corpus, open(os.path.join(HERE, 'corpus.json'), 'w', encoding='utf-8', newline='\n'), indent=1, ensure_ascii=False)
    return units

if __name__ == '__main__':
    u = main()
    for k in ('art-001-sec-0001', 'art-004-sec-0036', 'art-016-sec-0001'):
        if k in u: print(u[k]['text'][:600])
