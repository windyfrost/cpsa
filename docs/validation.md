# Validation results

[Home](../README.md) · [Audit](audit.md) · [Review instructions](maintenance.md)

Run date: 2026-11-10. This page records the original overhaul checks and the subsequent minimalist follow-up. The overhaul merged as PR #1; the current local branch is `docs/minimal-pdf-library`, based on `a65622e`.

## Documentation checks

- The repository's link checker passes for 22 Markdown files and 126 internal links after consolidation under `docs/`, including exact path case and heading fragments. Every documented local target exists. The original overhaul had 147 internal links.
- Markdown files have one H1 each and balanced fenced blocks. Git whitespace checks pass.
- GitHub's Markdown API returned HTTP 200 for the redesigned README in GFM mode. The result contains the expected heading hierarchy, links and seven-row domain table.
- The original overhaul's API-rendered HTML was visually inspected with a local GitHub-like stylesheet at 1120 px and 390 px viewport widths. Both layouts were readable with no page-level horizontal overflow. Its merged README was subsequently confirmed visible on the public repository.
- The final minimalist README was separately rendered through GitHub's Markdown API and visually inspected at the same desktop and mobile widths. Both previews passed, with a prominent working ZIP link and Medium article and no page-level horizontal overflow.
- Topic headings, command blocks, filenames and navigation were reviewed for consistency. The seven original topic lists and command examples remain available, with documented corrections.

## External links

The minimalist follow-up's 25 distinct external URLs were requested using HTTP HEAD with redirects followed. Twenty-four returned HTTP 200, including both new release assets, the original Nmap asset, the official syllabus and exam guidance. The previous overhaul had 22 external URLs.

The retained Medium article returned HTTP 403 to the automated check, but its content was readable through web retrieval. Its current title is “How I Cleared CREST CPSA Exam (And Built the Tool That Made It Possible)”; its A–K topic description differs from the official PDF's A–J structure. It remains labelled as community experience rather than examination authority. A 403 is not evidence that the URL is dead; reader access may vary.

OWASP, IANA, OpenSSH and platform URLs followed working redirects. Stable original references were retained. HTTP success verifies availability at the check time, not every claim or nested link on a destination page. Remote fragments and logged-in training curricula were not independently checked.

## Releases and preservation

- GitHub's public API was inspected for published releases: one release, one uploaded PDF asset. Tag `v1.0.0` points to baseline `48da6e2`.
- Asset name, byte size, uploaded state, browser download URL and API digest were recorded. The Nmap PDF was subsequently downloaded for the minimalist follow-up; its opening title pages were read and its independently computed SHA-256 matched the GitHub API digest.
- All five pre-existing tracked PDFs and `.gitignore` remain byte-for-byte unchanged relative to the baseline. The existing v1.0.0 release and its asset were preserved; v1.1.0 adds the ZIP and combined checksum manifest.
- The tracked syllabus matches a fresh download from the official CREST URL by SHA-256: `91e1df0d8a551d18dd4298a4be547af3830553ef36285a43dcf955e369df0292`.
- No new tracked file approaches GitHub's 100 MiB regular Git limit. The PDF ZIP is kept outside the repository and distributed through the new v1.1.0 release.

## Local bundle checks

The local `cpsa-study-materials.zip` contains six PDFs and `PDF-SHA256SUMS.txt`. Every PDF was read back from the archive and matched to its source SHA-256; all ZIP CRCs and the internal manifest passed validation. The external `SHA256SUMS.txt` contains six PDF hashes and the ZIP hash; `cpsa-study-materials.zip.sha256` contains the ZIP hash alone.

The ZIP is 181,334,878 bytes. Its SHA-256 is `ffa03ae387845ca6656c99d4cb6ec8bf30c91506074f50b5e97f17759f36b071`. Archive checks are completed before any upload. These checks establish byte identity, not authenticity or redistribution permission.

## Factual checks and remaining limits

The examination summary is supported by [CREST's current CPSA guidance](https://www.crest-approved.org/skills-certifications-careers/crest-practitioner-security-analyst/). The coverage map uses the technical PDF linked there, v2.5; it does not use inconsistent webpage group summaries or community weightings.

The owner confirmed redistribution permission for all six PDFs on 2026-11-10; underlying permission documents were not supplied here. The release book's title and byte identity against the existing asset have been checked. The notes remain partial coverage; they do not certify readiness or provide official exam questions. Historical legal references are retained as study pointers; current legal requirements are not adjudicated by this documentation.

Release v1.1.0 is published. GitHub returned the same byte sizes and SHA-256 digests as the local ZIP and external manifest, after both were checked before upload. The SHA-256 of the uploaded manifest is `06d54190762701e155863a7252d94e2f61f1c9e6898eb0d888d3e1d7d4e185d0`. The original v1.0.0 asset inventory is unchanged. The minimalist README and documentation relocation are prepared on a feature branch; merge is subject to owner approval.
