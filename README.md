# Mississippi: law history in git

The statute law of Mississippi as a git repository: one file per section, committed with the official publisher named as author. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now (a first build, not complete)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of the State of Mississippi (1890) | 1 | The Secretary of State edition updated May 2022 (oldest version available) |

Nothing else of Mississippi's law is in it yet.

## Where the text comes from

[The Constitution of the State of Mississippi, annotated, updated May 2022](https://sos.ms.gov/content/documents/ed_pubs/pubs/Mississippi_Constitution.pdf), published by the Mississippi Secretary of State. Only the section numbers, headings and text are taken; the Secretary of State's annotations, source lines and notes are left out. The Mississippi Code of 1972 is published only by LexisNexis under a click-through licence, so no code text is included.

## Dates

The single version is dated 1 May 2022, from the edition's own "Updated May, 2022".

## What it does not show

- One version only: the Secretary of State publishes no earlier editions online.
- The PDF prints curly quotation marks as an unreadable character; they were restored as apostrophes (between letters) or double quotation marks.
- Repealed sections are kept as headings so section numbers stay in place.
- The Mississippi Code is not included.

## How it is checked

- Every unit is read back from git on its day and compared with the corpus (`tools/check_repo.py`; results in `REPRODUCE.md`).
- Each source file is identified by its sha256, in `data/versions.json`.

## What "author" means

Each commit is authored by the publisher (Mississippi Secretary of State) because this first build holds one version of each act, the oldest version available. The committer is always Lexifina.
