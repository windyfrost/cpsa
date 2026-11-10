# Validation results

[Home](../README.md) · [Audit](audit.md) · [Review instructions](maintenance.md)

Run date: 2026-11-10. Baseline: `48da6e2`; feature branch: `docs/cpsa-study-hub-overhaul`.

## Documentation checks

- The repository's link checker passes for 22 Markdown files and 147 internal links, including exact path case and heading fragments. Every documented local target exists.
- Markdown files have one H1 each and balanced fenced blocks. Git whitespace checks pass.
- GitHub's Markdown API returned HTTP 200 for the redesigned README in GFM mode. The result contains the expected heading hierarchy, links and seven-row domain table.
- The API-rendered HTML was visually inspected with a local GitHub-like stylesheet at 1120 px and 390 px viewport widths. Both layouts were readable with no page-level horizontal overflow. This is a local preview, not a published branch review.
- Topic headings, command blocks, filenames and navigation were reviewed for consistency. The seven original topic lists and command examples remain available, with documented corrections.

## External links

All 22 distinct external URLs were requested using HTTP HEAD with redirects followed. Twenty-one returned HTTP 200, including the release asset download, official syllabus and exam guidance.

The retained Medium article returned HTTP 403 to the automated check, but its content was readable through web retrieval. Its current title is “How I Cleared CREST CPSA Exam (And Built the Tool That Made It Possible)”; its A–K topic description differs from the official PDF's A–J structure. It remains labelled as community experience rather than examination authority. A 403 is not evidence that the URL is dead; reader access may vary.

OWASP, IANA, OpenSSH and platform URLs followed working redirects. Stable original references were retained. HTTP success verifies availability at the check time, not every claim or nested link on a destination page. Remote fragments and logged-in training curricula were not independently checked.

## Releases and preservation

- GitHub's public API was inspected for published releases: one release, one uploaded PDF asset. Tag `v1.0.0` points to baseline `48da6e2`.
- Asset name, byte size, uploaded state, browser download URL and API digest were recorded. The download endpoint returned HTTP 200 after redirects; the large PDF itself was not downloaded, parsed or independently hashed.
- All five pre-existing tracked PDFs and `.gitignore` remain byte-for-byte unchanged relative to the baseline. No release asset was uploaded, replaced or removed.
- The tracked syllabus matches a fresh download from the official CREST URL by SHA-256: `91e1df0d8a551d18dd4298a4be547af3830553ef36285a43dcf955e369df0292`.
- No new file approaches GitHub's 100 MiB regular Git limit. The handoff package contains documentation and validation code only, not copies of the third-party PDFs.

## Factual checks and remaining limits

The examination summary is supported by [CREST's current CPSA guidance](https://www.crest-approved.org/skills-certifications-careers/crest-practitioner-security-analyst/). The coverage map uses the technical PDF linked there, v2.5; it does not use inconsistent webpage group summaries or community weightings.

Redistribution permission remains unverified for all existing third-party PDFs, especially the modified RTFM copy. The release book's internal edition and integrity remain unverified. The notes remain partial coverage; they do not certify readiness or provide official exam questions. Historical legal references are retained as study pointers; current legal requirements are not adjudicated by this documentation.

A live GitHub branch preview, publication and merge are pending owner approval. Recheck dynamic information and download metadata before publication if time has passed.
