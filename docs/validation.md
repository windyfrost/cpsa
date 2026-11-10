# Validation results

[Home](../README.md) · [Audit](audit.md) · [Review instructions](maintenance.md)

Run date: 2026-11-10. This page records the original overhaul checks and the subsequent minimalist follow-up. The overhaul merged as PR #1; the current local branch is `docs/minimal-pdf-library`, based on `a65622e`.

## Documentation checks

- The repository's link checker passes for 22 Markdown files and 110 internal links after consolidation under `docs/` and removal of withdrawn download links, including exact path case and heading fragments. Every documented local target exists. The original overhaul had 147 internal links.
- Markdown files have one H1 each and balanced fenced blocks. Git whitespace checks pass.
- GitHub's Markdown API returned HTTP 200 for the redesigned README in GFM mode. The result contains the expected heading hierarchy, links and seven-row domain table.
- The original overhaul's API-rendered HTML was visually inspected with a local GitHub-like stylesheet at 1120 px and 390 px viewport widths. Both layouts were readable with no page-level horizontal overflow. Its merged README was subsequently confirmed visible on the public repository.
- The earlier PDF-focused README was separately rendered through GitHub's Markdown API and visually inspected at the same desktop and mobile widths. Those previews passed before the release was withdrawn; the current README instead links to the Medium article and official sources.
- Topic headings, command blocks, filenames and navigation were reviewed for consistency. The seven original topic lists and command examples remain available, with documented corrections.

## External links

Before withdrawal, 25 external URLs were checked: 24 returned HTTP 200 and the Medium HEAD request returned HTTP 403. The ZIP and checksum URLs are now intentionally disabled following withdrawal of the release; do not interpret the earlier availability checks as current distribution approval.

The retained Medium article returned HTTP 403 to the automated check, but its content was readable through web retrieval. Its current title is “How I Cleared CREST CPSA Exam (And Built the Tool That Made It Possible)”; its A–K topic description differs from the official PDF's A–J structure. It remains labelled as community experience rather than examination authority. A 403 is not evidence that the URL is dead; reader access may vary.

OWASP, IANA, OpenSSH and platform URLs followed working redirects. Stable original references were retained. HTTP success verifies availability at the check time, not every claim or nested link on a destination page. Remote fragments and logged-in training curricula were not independently checked.

## Releases and preservation

- GitHub's public API was inspected for published releases: one release, one uploaded PDF asset. Tag `v1.0.0` points to baseline `48da6e2`.
- Asset name, byte size, uploaded state, browser download URL and API digest were recorded. The Nmap PDF was subsequently downloaded for the minimalist follow-up; its opening title pages were read and its independently computed SHA-256 matched the GitHub API digest.
- All five pre-existing tracked PDFs and `.gitignore` remain byte-for-byte unchanged relative to the baseline. The existing v1.0.0 release and its asset were preserved. The newly created v1.1.0 release has been returned to draft.
- The tracked syllabus matches a fresh download from the official CREST URL by SHA-256: `91e1df0d8a551d18dd4298a4be547af3830553ef36285a43dcf955e369df0292`.
- No new tracked file approaches GitHub's 100 MiB regular Git limit. The PDF ZIP is kept outside the repository. The release containing it has been withdrawn from public download.

## Local bundle checks

The local `cpsa-study-materials.zip` contains six PDFs and `PDF-SHA256SUMS.txt`. Every PDF was read back from the archive and matched to its source SHA-256; all ZIP CRCs and the internal manifest passed validation. The external `SHA256SUMS.txt` contains six PDF hashes and the ZIP hash; `cpsa-study-materials.zip.sha256` contains the ZIP hash alone.

The ZIP is 181,334,878 bytes. Its SHA-256 is `ffa03ae387845ca6656c99d4cb6ec8bf30c91506074f50b5e97f17759f36b071`. Archive checks are completed before any upload. These checks establish byte identity, not authenticity or redistribution permission.

## Factual checks and remaining limits

The examination summary is supported by [CREST's current CPSA guidance](https://www.crest-approved.org/skills-certifications-careers/crest-practitioner-security-analyst/). The coverage map uses the technical PDF linked there, v2.5; it does not use inconsistent webpage group summaries or community weightings.

The owner withdrew the earlier confirmation on 2026-11-10 and clarified that redistribution permission is not held. The release book's title and byte identity against the existing asset have been checked. The notes remain partial coverage; they do not certify readiness or provide official exam questions. Historical legal references are retained as study pointers; current legal requirements are not adjudicated by this documentation.

The five PDFs have been removed from the cleanup branch, and the Nmap PDF asset has been removed from v1.0.0. The v1.1.0 release remains a draft. GitHub-generated source archives for v1.0.0 still return HTTP 200 and contain the old tagged snapshot; Git history was not rewritten.

Earlier visual and link checks describe the pre-withdrawal draft. The current proposed README is a short links page without the combined ZIP or mirrored-book download links.
