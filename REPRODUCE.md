# How this repository was made (United States (Mississippi))

This file is written by the build on 2026-11-02, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| The Constitution of the State of Mississippi, annotated, updated May 2022 (Mississippi Secretary of State) | <https://sos.ms.gov/content/documents/ed_pubs/pubs/Mississippi_Constitution.pdf> | 2026-10-30 | The text of a constitution is a law of the State and is not copyrightable (Georgia v. Public.Resource.Org, 2020). The Secretary of State's annotations are not copied. |
| Mississippi Code of 1972, Mississippi Code, Vol. 13, Title 55-57 (2022 Edition): scan by Public.Resource.Org on the Internet Archive (mississippicode113unse) | <https://archive.org/details/mississippicode113unse> | 2026-11-02 | Public.Resource.Org's "Official State Codes" collection (govlaw) on the Internet Archive, whose rights statement quotes Banks v. Manchester, 128 U.S. 244 (1888): "The authentic exposition and interpretation of the law, which, binding every citizen, is free for publication to all". Statute text is not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)); the annotations, under the State's copyright notice, are not used. |
| Mississippi Code of 1972, Mississippi Code, Vol. 13, Title 55-57 (2022 Edition): scan by Public.Resource.Org on the Internet Archive (mississippicode113unse) | <https://archive.org/details/mississippicode113unse> | 2026-11-02 | Public.Resource.Org's "Official State Codes" collection (govlaw) on the Internet Archive, whose rights statement quotes Banks v. Manchester, 128 U.S. 244 (1888): "The authentic exposition and interpretation of the law, which, binding every citizen, is free for publication to all". Statute text is not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)); the annotations, under the State's copyright notice, are not used. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the State of Mississippi (1890) | 1 | 2022-05-01 to 2022-05-01 |
| `title-55` | Mississippi Code of 1972, Title 55: Parks and Recreation | 1 | 2022-07-01 to 2022-07-01 |
| `title-57` | Mississippi Code of 1972, Title 57: Planning, Research and Development | 1 | 2022-07-01 to 2022-07-01 |

The build made 3 commits:

| Commits | Kind |
| ---: | --- |
| 3 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-02.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 1 laws in the record.
- 3 tags.

## Dates

Each commit is dated at noon (America/Chicago) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Only the Secretary of State edition updated May 2022 is online; it is the oldest (and only) version available and is dated 2022-05-01. https://sos.ms.gov/content/documents/ed_pubs/pubs/Mississippi_Constitution.pdf

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `2a796ef381ccc3d933e748a0c1de3fa12dd2c9c3147b5dee81ab7c2f0224e989` (2103585 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

3 versions of 3 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- The Mississippi Code of 1972 is published only by LexisNexis under a click-through licence; no Mississippi Code text is included.
- Only the Secretary of State edition updated May 2022 is online, so the Constitution has one version, the oldest available, dated 2022-05-01 from the edition's own "Updated May, 2022".
- The PDF prints its curly quotation marks as U+FFFD; between two letters these were restored as apostrophes and elsewhere as double quotation marks.
- SOURCES lines, NOTE paragraphs and annotations are dropped. A section heading that wraps over two lines in the PDF keeps its second line at the start of the text.
- Mississippi Code title 55: one version, the 2022 Edition volume (Mississippi Code, Vol. 13, Title 55-57 (2022 Edition)), dated 2022-07-01, the effective date of most acts of the 2022 regular session; sections whose HISTORY line gives a later effective date are left out.
- Mississippi Code title 55: text read by OCR; only the statute text between each section heading and its HISTORY line is kept; HISTORY lines, cross references, editor's notes, amendment notes, judicial decisions, Attorney General opinions and research references (the publisher's annotations) are left out.
- Mississippi Code title 57: one version, the 2022 Edition volume (Mississippi Code, Vol. 13, Title 55-57 (2022 Edition)), dated 2022-07-01, the effective date of most acts of the 2022 regular session; sections whose HISTORY line gives a later effective date are left out.
- Mississippi Code title 57: text read by OCR; only the statute text between each section heading and its HISTORY line is kept; HISTORY lines, cross references, editor's notes, amendment notes, judicial decisions, Attorney General opinions and research references (the publisher's annotations) are left out.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
- none
- none
