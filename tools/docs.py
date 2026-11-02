"""Write repo/README.md, repo/LICENSE and repo/jurisdiction.json for the Mississippi repository from corpus.json
(the Constitution) and the corpus.d parts that have PUBLISH. Deterministic.

    python -X utf8 -I docs.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE / 'repo'


def main():
    rows, ocr_rows, total = [], [], 0
    for p in sorted((HERE / 'corpus.d').glob('*.json')):
        if not p.with_suffix('.PUBLISH').exists():
            continue
        part = json.loads(p.read_text(encoding='utf-8'))
        a = part['acts'][0]
        v = a['versions'][0]
        n = len(v['units'])
        total += n
        rows.append(f"| `{a['slug']}/` | {a['title']} ({n} sections) | 1 | 2022 Edition volume, dated 1 July 2022 (oldest version available); text by OCR |")
        ocr_rows.append(f"- `{a['slug']}/`: OCR (Tesseract 5.2.0) of <{v['source_url']}>. {part['sources'][0]['notes'].split(' Left out:')[0]}")
    REPO.mkdir(exist_ok=True)
    readme = f"""# Mississippi: law history in git

The statute law of Mississippi as a git repository: one file per section, committed with the publisher named as author. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now (a first build, not complete)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of the State of Mississippi (1890) | 1 | The Secretary of State edition updated May 2022 (oldest version available) |
{chr(10).join(rows)}

That is all the law this repository holds today. The other titles of the Mississippi Code of 1972, the session laws and the regulations are not in it yet, and it has no amendment history yet.

## Where the text comes from

- **Constitution:** [The Constitution of the State of Mississippi, annotated, updated May 2022](https://sos.ms.gov/content/documents/ed_pubs/pubs/Mississippi_Constitution.pdf), published by the Mississippi Secretary of State. Only the section numbers, headings and text are taken; the annotations, source lines and notes are left out.
- **Mississippi Code of 1972:** the official code is published by LexisNexis for the State, under a click-through licence online. The code titles here are read instead from **Public.Resource.Org's scans of the printed 2022 Edition volumes** ("containing permanent public statutes of Mississippi to the end of the 2022 regular legislative session"), in its "Official State Codes" collection on the Internet Archive. That collection's rights statement quotes Banks v. Manchester, 128 U.S. 244 (1888): "The authentic exposition and interpretation of the law, which, binding every citizen, is free for publication to all". Statute text is not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)).

**Statute text only.** From each section the number, the catchline and the text up to its HISTORY line are kept. Everything the publisher adds is left out: the HISTORY lines, cross references, editor's notes, amendment notes, judicial decisions (case notes), opinions of the Attorney General, research references, editorial brackets in catchlines, running heads and page numbers. No annotation or other vendor material is included.

## OCR texts

The code titles are scans, so their text was read by optical character recognition (OCR) and may contain misreadings. Each title's commit says so on a line of its own (`Text-source: OCR (Tesseract 5.2.0) of <scan url>`), and every section file in these folders is OCR text:

{chr(10).join(ocr_rows) if ocr_rows else '- (none yet)'}

How the OCR was checked: the first reading is the Internet Archive's own Tesseract 5.2.0 text layer of each scan. A second, independent reading was made here with different settings (Tesseract 5.4.0, `--psm 4 --oem 1`, on each page rendered at 300 dpi). Every section, not only a sample, was compared on its letters and digits, word by word and then character by character; a section where the two readings agree on less than 98% is left out. Paragraph breaks and line-end hyphens are rebuilt from the page layout (a hyphen is removed only when the joined word occurs elsewhere in the volume), so a break or a hyphen can be wrong.

## Dates

- The Constitution's single version is dated 1 May 2022, from the edition's own "Updated May, 2022".
- Each code title is one version, dated **1 July 2022**, the effective date of most acts of the 2022 regular session, which the 2022 Edition volumes include. A section whose HISTORY line gives a later effective date is left out. Each commit is credited to the publisher as "oldest version available".

## What it does not show

- Any history before these editions, and any change after them.
- Repealed and reserved sections, sections not yet in force on 1 July 2022, sections whose HISTORY line could not be found in the OCR text, and sections below the 98% OCR agreement: each title's source note in `REPRODUCE.md` lists them.
- Nothing here is an official publication or legal advice. For anything that matters, read the official text.

## How it is checked

- Every unit is read back from git on its day and compared with the corpus (`tools/check_repo.py`; results in `REPRODUCE.md`).
- Each source file is identified by its sha256, in `data/versions.json`.

## What "author" means

Each commit is authored by the publisher because this build holds one version of each act, the oldest version available. The committer is always Lexifina.
"""
    (REPO / 'README.md').write_text(readme, encoding='utf-8', newline='\n')
    (REPO / 'LICENSE').write_text("""Constitution text published by the Mississippi Secretary of State (https://sos.ms.gov). The text of a constitution is
law and cannot be copyrighted (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). The Secretary of State's
annotations are not included.

Mississippi Code of 1972 text (the code titles) read by OCR from Public.Resource.Org's scans of the 2022 Edition
volumes on the Internet Archive (collection "Official State Codes", https://archive.org/details/govlaw), whose rights
statement reads: Supreme Court of the United States, Banks v. Manchester [128 U.S. 244, 1888]: "The authentic
exposition and interpretation of the law, which, binding every citizen, is free for publication to all, whether it is
a declaration of unwritten law, or an interpretation of a constitution or a statute." Statute text is not
copyrightable (Georgia v. Public.Resource.Org, above). The volumes' annotations, under the State of Mississippi's
copyright notice, and all other publisher material are not included: statute text only.

The arrangement of this repository, its tables, commit messages and tools are by Lexifina and may be reused under the
Creative Commons Attribution 4.0 International licence (https://creativecommons.org/licenses/by/4.0/). This repository
is not legal advice and not an official publication. Neither the State of Mississippi, LexisNexis nor
Public.Resource.Org endorses it.
""", encoding='utf-8', newline='\n')
    (REPO / 'jurisdiction.json').write_text(json.dumps({
        'path': 'us-ms', 'code': 'MS', 'name': 'Mississippi', 'level': 'state',
        'repo': 'https://github.com/lexifina/united-states-mississippi-law',
        'build': 'built: Constitution of the State of Mississippi (1890), Secretary of State edition updated May 2022'
                 + (f'; Mississippi Code of 1972, {len(rows)} titles (2022 Edition, OCR, one version each)' if rows else ''),
        'register_date': '2026-10-30'}, indent=2) + '\n', encoding='utf-8', newline='\n')


if __name__ == '__main__':
    main()
