# How this repository was made (United States (Mississippi))

This file is written by the build on 2026-11-10, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| The Constitution of the State of Mississippi, annotated, updated May 2022 (Mississippi Secretary of State) | <https://sos.ms.gov/content/documents/ed_pubs/pubs/Mississippi_Constitution.pdf> | 2026-10-30 | The text of a constitution is a law of the State and is not copyrightable (Georgia v. Public.Resource.Org, 2020). The Secretary of State's annotations are not copied. |
| Mississippi Legislature, House Bill 314 (2026), final text approved by the Governor | <https://billstatus.ls.state.ms.us/documents/2026/pdf/HB/0300-0399/HB0314SG.pdf> | 2026-11-05 | Official statute text; government edicts are not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). |
| Mississippi Code of 1972, Mississippi Code, Vol. 13, Title 55-57 (2022 Edition): scan by Public.Resource.Org on the Internet Archive (mississippicode113unse) | <https://archive.org/details/mississippicode113unse> | 2026-11-02 | Public.Resource.Org's "Official State Codes" collection (govlaw) on the Internet Archive, whose rights statement quotes Banks v. Manchester, 128 U.S. 244 (1888): "The authentic exposition and interpretation of the law, which, binding every citizen, is free for publication to all". Statute text is not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)); the annotations, under the State's copyright notice, are not used. |
| Mississippi Code of 1972, Mississippi Code, Vol. 13, Title 55-57 (2022 Edition): scan by Public.Resource.Org on the Internet Archive (mississippicode113unse) | <https://archive.org/details/mississippicode113unse> | 2026-11-02 | Public.Resource.Org's "Official State Codes" collection (govlaw) on the Internet Archive, whose rights statement quotes Banks v. Manchester, 128 U.S. 244 (1888): "The authentic exposition and interpretation of the law, which, binding every citizen, is free for publication to all". Statute text is not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)); the annotations, under the State's copyright notice, are not used. |
| Mississippi Code of 1972, Mississippi Code, Vol. 13A, Title 59-63 (2022 Edition): scan by Public.Resource.Org on the Internet Archive (mississippicode113unse_0) | <https://archive.org/details/mississippicode113unse_0> | 2026-11-02 | Public.Resource.Org's "Official State Codes" collection (govlaw) on the Internet Archive, whose rights statement quotes Banks v. Manchester, 128 U.S. 244 (1888): "The authentic exposition and interpretation of the law, which, binding every citizen, is free for publication to all". Statute text is not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)); the annotations, under the State's copyright notice, are not used. |
| Mississippi Code of 1972, Mississippi Code, Vol. 13A, Title 59-63 (2022 Edition): scan by Public.Resource.Org on the Internet Archive (mississippicode113unse_0) | <https://archive.org/details/mississippicode113unse_0> | 2026-11-02 | Public.Resource.Org's "Official State Codes" collection (govlaw) on the Internet Archive, whose rights statement quotes Banks v. Manchester, 128 U.S. 244 (1888): "The authentic exposition and interpretation of the law, which, binding every citizen, is free for publication to all". Statute text is not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)); the annotations, under the State's copyright notice, are not used. |
| Mississippi Code of 1972, Mississippi Code, Vol. 13A, Title 59-63 (2022 Edition): scan by Public.Resource.Org on the Internet Archive (mississippicode113unse_0) | <https://archive.org/details/mississippicode113unse_0> | 2026-11-02 | Public.Resource.Org's "Official State Codes" collection (govlaw) on the Internet Archive, whose rights statement quotes Banks v. Manchester, 128 U.S. 244 (1888): "The authentic exposition and interpretation of the law, which, binding every citizen, is free for publication to all". Statute text is not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)); the annotations, under the State's copyright notice, are not used. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the State of Mississippi (1890) | 1 | 2022-05-01 to 2022-05-01 |
| `ibogaine-drug-development-clinical-trial-act-2026` | Ibogaine Drug Development Clinical Trial Act (2026) | 1 | 2026-07-01 to 2026-07-01 |
| `title-55` | Mississippi Code of 1972, Title 55: Parks and Recreation | 1 | 2022-07-01 to 2022-07-01 |
| `title-57` | Mississippi Code of 1972, Title 57: Planning, Research and Development | 1 | 2022-07-01 to 2022-07-01 |
| `title-59` | Mississippi Code of 1972, Title 59: Ports, Harbors, Landings and Watercraft | 1 | 2022-07-01 to 2022-07-01 |
| `title-61` | Mississippi Code of 1972, Title 61: Aviation | 1 | 2022-07-01 to 2022-07-01 |
| `title-63` | Mississippi Code of 1972, Title 63: Motor Vehicles and Traffic Regulations | 1 | 2022-07-01 to 2022-07-01 |

The build made 7 commits:

| Commits | Kind |
| ---: | --- |
| 7 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-10.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 1 laws in the record.
- 7 tags.

## Dates

Each commit is dated at noon (America/Chicago) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Only the Secretary of State edition updated May 2022 is online; it is the oldest (and only) version available and is dated 2022-05-01. https://sos.ms.gov/content/documents/ed_pubs/pubs/Mississippi_Constitution.pdf

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `18ff41516fff11c4ed3bc51925afb9eb9f1cdf59021c2e9e5b8a68d8282be945` (3815331 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `3024ff164c261807dfc4d5b7b1b4a2cde4357da1`, `check.py` `5d719354ea4c62d240c93d2cae446307d81d9e81`, `on.py` `aff48cf1b68d50c7ba8f399ca32261871c301824`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- The Mississippi Code of 1972 is published only by LexisNexis under a click-through licence; no Mississippi Code text is included.
- Only the Secretary of State edition updated May 2022 is online, so the Constitution has one version, the oldest available, dated 2022-05-01 from the edition's own "Updated May, 2022".
- The PDF prints its curly quotation marks as U+FFFD; between two letters these were restored as apostrophes and elsewhere as double quotation marks.
- SOURCES lines, NOTE paragraphs and annotations are dropped. A section heading that wraps over two lines in the PDF keeps its second line at the start of the text.
- HB 314 (2026) is a standalone as-enacted act, not a consolidated edition. Its single version is dated July 1, 2026 from section 15; first_law is null and the publisher is credited.
- The born-digital PDF text layer is used verbatim. Line numbers, page furniture, sponsor and committee information are excluded; all words from the long title to the final commencement clause are retained. Paragraphs are joined across printed lines.
- HB 314 contains no embedded images. Its vector marks are typographical underlining and page furniture, not normative tables, maps or formulas.
- No amendment history or later consolidation is asserted for HB 314 (2026).
- Mississippi Code title 55: one version, the 2022 Edition volume (Mississippi Code, Vol. 13, Title 55-57 (2022 Edition)), dated 2022-07-01, the effective date of most acts of the 2022 regular session; sections whose HISTORY line gives a later effective date are left out.
- Mississippi Code title 55: text read by OCR; only the statute text between each section heading and its HISTORY line is kept; HISTORY lines, cross references, editor's notes, amendment notes, judicial decisions, Attorney General opinions and research references (the publisher's annotations) are left out.
- Mississippi Code title 57: one version, the 2022 Edition volume (Mississippi Code, Vol. 13, Title 55-57 (2022 Edition)), dated 2022-07-01, the effective date of most acts of the 2022 regular session; sections whose HISTORY line gives a later effective date are left out.
- Mississippi Code title 57: text read by OCR; only the statute text between each section heading and its HISTORY line is kept; HISTORY lines, cross references, editor's notes, amendment notes, judicial decisions, Attorney General opinions and research references (the publisher's annotations) are left out.
- Mississippi Code title 59: one version, the 2022 Edition volume (Mississippi Code, Vol. 13A, Title 59-63 (2022 Edition)), dated 2022-07-01, the effective date of most acts of the 2022 regular session; sections whose HISTORY line gives a later effective date are left out.
- Mississippi Code title 59: text read by OCR; only the statute text between each section heading and its HISTORY line is kept; HISTORY lines, cross references, editor's notes, amendment notes, judicial decisions, Attorney General opinions and research references (the publisher's annotations) are left out.
- Mississippi Code title 61: one version, the 2022 Edition volume (Mississippi Code, Vol. 13A, Title 59-63 (2022 Edition)), dated 2022-07-01, the effective date of most acts of the 2022 regular session; sections whose HISTORY line gives a later effective date are left out.
- Mississippi Code title 61: text read by OCR; only the statute text between each section heading and its HISTORY line is kept; HISTORY lines, cross references, editor's notes, amendment notes, judicial decisions, Attorney General opinions and research references (the publisher's annotations) are left out.
- Mississippi Code title 63: one version, the 2022 Edition volume (Mississippi Code, Vol. 13A, Title 59-63 (2022 Edition)), dated 2022-07-01, the effective date of most acts of the 2022 regular session; sections whose HISTORY line gives a later effective date are left out.
- Mississippi Code title 63: text read by OCR; only the statute text between each section heading and its HISTORY line is kept; HISTORY lines, cross references, editor's notes, amendment notes, judicial decisions, Attorney General opinions and research references (the publisher's annotations) are left out.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
- GPT-6 inspected source structure, selected the standalone act and wrote extraction and verification code; no model-generated law text or OCR was used.
- none
- none
- none
- none
- none
