# Mississippi: law history in git

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is the law of Mississippi, United States, which global-law reads at `united-states/mississippi/acts/`.

The statute law of Mississippi as a git repository: one file per section, committed with the publisher named as author. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**Recorded editions (coverage remains incomplete)**

The table describes the editions prepared for this repository. A record is available in a checkout when its listed folder is present. This also allows documentation to describe a reviewed record while its inclusion is pending.

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of the State of Mississippi (1890) | 1 | The Secretary of State edition updated May 2022 (oldest version available) |
| `ibogaine-drug-development-clinical-trial-act-2026/` | Ibogaine Drug Development Clinical Trial Act (2026) (15 sections) | 1 | As enacted; in force 2026-07-01 under the act's commencement clause |
| `title-55/` | Mississippi Code of 1972, Title 55: Parks and Recreation (250 sections) | 1 | 2022 Edition volume, dated 1 July 2022 (oldest version available); text by OCR |
| `title-57/` | Mississippi Code of 1972, Title 57: Planning, Research and Development (683 sections) | 1 | 2022 Edition volume, dated 1 July 2022 (oldest version available); text by OCR |
| `title-59/` | Mississippi Code of 1972, Title 59: Ports, Harbors, Landings and Watercraft (301 sections) | 1 | 2022 Edition volume, dated 1 July 2022 (oldest version available); text by OCR |
| `title-61/` | Mississippi Code of 1972, Title 61: Aviation (143 sections) | 1 | 2022 Edition volume, dated 1 July 2022 (oldest version available); text by OCR |
| `title-63/` | Mississippi Code of 1972, Title 63: Motor Vehicles and Traffic Regulations (555 sections) | 1 | 2022 Edition volume, dated 1 July 2022 (oldest version available); text by OCR |
| `title-73/` | Mississippi Code of 1972, Title 73: Professions and Vocations (1003 sections) | 1 | 2022 Edition volume, dated 1 July 2022 (oldest version available); text by OCR |
| `title-83/` | Mississippi Code of 1972, Title 83: Insurance (1106 sections) | 1 | 2022 Edition volume, dated 1 July 2022 (oldest version available); text by OCR |

Coverage remains incomplete. Other Code titles, other session laws and regulations remain outside the listed records. No amendment history is represented.

## Where the text comes from

- **Constitution:** [The Constitution of the State of Mississippi, annotated, updated May 2022](https://sos.ms.gov/content/documents/ed_pubs/pubs/Mississippi_Constitution.pdf), published by the Mississippi Secretary of State. Only the section numbers, headings and text are taken; the annotations, source lines and notes are left out.
- **Mississippi Code of 1972:** the official code is published by LexisNexis for the State, under a click-through licence online. The code titles here are read instead from **Public.Resource.Org's scans of the printed 2022 Edition volumes** ("containing permanent public statutes of Mississippi to the end of the 2022 regular legislative session"), in its "Official State Codes" collection on the Internet Archive. That collection's rights statement quotes Banks v. Manchester, 128 U.S. 244 (1888): "The authentic exposition and interpretation of the law, which, binding every citizen, is free for publication to all". Statute text is not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)).

- **Ibogaine Drug Development Clinical Trial Act (2026):** [HB 314 (2026), official final text](https://billstatus.ls.state.ms.us/documents/2026/pdf/HB/0300-0399/HB0314SG.pdf). As enacted: House Bill 314 (2026), approved by the Governor March 26, 2026. Section 15: This act shall take effect and be in force from and after July 1, 2026. In-force basis: the express commencement clause in section 15. No subsequent amendments are represented.

**Statute text only.** From each section the number, the catchline and the text up to its HISTORY line are kept. Everything the publisher adds is left out: the HISTORY lines, cross references, editor's notes, amendment notes, judicial decisions (case notes), opinions of the Attorney General, research references, editorial brackets in catchlines, running heads and page numbers. No annotation or other vendor material is included.

## OCR texts

The code titles are scans, so their text was read by optical character recognition (OCR) and may contain misreadings. Each title's commit says so on a line of its own (`Text-source: OCR (Tesseract 5.2.0) of <scan url>`), and every section file in these folders is OCR text:

- `title-55/`: OCR (Tesseract 5.2.0) of <https://archive.org/details/mississippicode113unse>. OCR text: the Internet Archive's Tesseract 5.2.0 text layer of the scan (PDF sha256 7643bc7fed28888953aaa05e3d8083439868f6a6101dd520942bcee24795566c). Second pass: local Tesseract 5.4.0, --psm 4 --oem 1, 300 dpi page renders; all 253 sections read were compared.
- `title-57/`: OCR (Tesseract 5.2.0) of <https://archive.org/details/mississippicode113unse>. OCR text: the Internet Archive's Tesseract 5.2.0 text layer of the scan (PDF sha256 7643bc7fed28888953aaa05e3d8083439868f6a6101dd520942bcee24795566c). Second pass: local Tesseract 5.4.0, --psm 4 --oem 1, 300 dpi page renders; all 688 sections read were compared.
- `title-59/`: OCR (Tesseract 5.2.0) of <https://archive.org/details/mississippicode113unse_0>. OCR text: the Internet Archive's Tesseract 5.2.0 text layer of the scan (PDF sha256 40db225ac3d4e82bd969b1ace3d643740a5ae52a22e0c683db0329c2c4271656). Second pass: local Tesseract 5.4.0, --psm 4 --oem 1, 300 dpi page renders; all 302 sections read were compared.
- `title-61/`: OCR (Tesseract 5.2.0) of <https://archive.org/details/mississippicode113unse_0>. OCR text: the Internet Archive's Tesseract 5.2.0 text layer of the scan (PDF sha256 40db225ac3d4e82bd969b1ace3d643740a5ae52a22e0c683db0329c2c4271656). Second pass: local Tesseract 5.4.0, --psm 4 --oem 1, 300 dpi page renders; all 146 sections read were compared.
- `title-63/`: OCR (Tesseract 5.2.0) of <https://archive.org/details/mississippicode113unse_0>. OCR text: the Internet Archive's Tesseract 5.2.0 text layer of the scan (PDF sha256 40db225ac3d4e82bd969b1ace3d643740a5ae52a22e0c683db0329c2c4271656). Second pass: local Tesseract 5.4.0, --psm 4 --oem 1, 300 dpi page renders; all 572 sections read were compared.
- `title-73/`: OCR (Tesseract 5.2.0) of <https://archive.org/details/mississippicode115unse>. OCR text: the Internet Archive's Tesseract 5.2.0 text layer of the scan (PDF sha256 501b88d1270841b7890d99d7f4e9ee5bbdb05da302631012979cac1b913945d8). Second pass: local Tesseract 5.4.0, --psm 4 --oem 1, 300 dpi page renders; all 1023 sections read were compared.
- `title-83/`: OCR (Tesseract 5.2.0) of <https://archive.org/details/mississippicode11919unse>. OCR text: the Internet Archive's Tesseract 5.2.0 text layer of the scan (PDF sha256 d4a4c7deb2804793ea6216ac29f2186362fc9ff8ae894b91f3be9e61d260c0a2). Second pass: local Tesseract 5.4.0, --psm 4 --oem 1, 300 dpi page renders; all 1124 sections read were compared.

How the OCR was checked: the first reading is the Internet Archive's own Tesseract 5.2.0 text layer of each scan. A second, independent reading was made here with different settings (Tesseract 5.4.0, `--psm 4 --oem 1`, on each page rendered at 300 dpi). Every section, not only a sample, was compared on its letters and digits, word by word and then character by character; a section where the two readings agree on less than 98% is left out. Paragraph breaks and line-end hyphens are rebuilt from the page layout (a hyphen is removed only when the joined word occurs elsewhere in the volume), so a break or a hyphen can be wrong.

## Dates

- The Constitution's single version is dated 1 May 2022, from the edition's own "Updated May, 2022".
- Each code title is one version, dated **1 July 2022**, the effective date of most acts of the 2022 regular session, which the 2022 Edition volumes include. A section whose HISTORY line gives a later effective date is left out. Each commit is credited to the publisher as "oldest version available".
- Ibogaine Drug Development Clinical Trial Act (2026), HB 314 (2026), as enacted, in force 2026-07-01; dated by its express commencement clause.

## What it does not show

- Earlier versions and subsequent amendments to the recorded editions, including the as-enacted session-law records.
- Repealed and reserved sections, sections not yet in force on 1 July 2022, sections whose HISTORY line could not be found in the OCR text, sections below the 98% OCR agreement, and (from titles 59 on) sections whose OCR text has the publisher's annotation column mixed into it: each title's source note in `REPRODUCE.md` lists them.
- Nothing here is an official publication or legal advice. For anything that matters, read the official text.

## How it is checked

- Every unit is read back from git on its day and compared with the corpus (`tools/check_repo.py`; results in `REPRODUCE.md`).
- Each source file is identified by its sha256, in `data/versions.json`.

## What "author" means

Each commit is authored by the publisher because this build holds one version of each act, the oldest version available. The committer is always Lexifina.
