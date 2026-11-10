# Review and publication

[Home](../README.md) · [Audit](audit.md) · [Validation results](validation.md)

## Review locally

The minimalist follow-up is on `docs/minimal-pdf-library`, based on the merged overhaul. Inspect the short root README, [catalogue](downloads.md) and [rights register](licensing-and-attribution.md). Use `git diff origin/main...HEAD --stat` and `git diff origin/main...HEAD` after the local commits are made. The original study content remains optional under `docs/`.

## Validation

Run from the repository root with Python 3:

```text
python scripts/check-doc-links.py
git diff --check origin/main...HEAD
```

The script checks inline Markdown file links, exact path case, heading fragments, fence balance and duplicate H1s. It does not implement every Markdown syntax form and does not validate remote URL fragments. Review external links separately; blocked requests require a browser check.

To inspect GitHub formatting before publication, render Markdown with GitHub's Markdown API using relative context, then preview the resulting HTML. A local render confirms generated structure; final sidebar, downloads and mobile appearance still need a post-approval GitHub review.

## Publishing after owner approval

1. Review rights concerns and confirm whether the current catalogue should remain as drafted. Any distribution changes need separate approval.
2. Recheck CREST information and release metadata if time has passed.
3. After explicit publication approval, push the feature branch and open a pull request against main. Describe the documentation changes, preservation and validation limits.
4. Review the README and relative links on the branch in GitHub, including mobile width and the Releases route.
5. Merge only after the owner approves the reviewed change. Do not rewrite tags, force-push or alter release assets.

## Build the PDF bundle locally

The builder hashes each source PDF, creates a ZIP with fixed timestamps, checks every archived PDF against its source SHA-256, and verifies the ZIP CRCs. It never uploads anything. Keep its output outside the Git tree; the ZIP exceeds the regular Git file limit.

Download the existing Nmap release PDF separately and compare its SHA-256 with the existing release digest. Pass its actual local path as `--extra-pdf`, along with a directory outside this repository as `--output-dir`:

```text
python scripts/build-pdf-bundle.py --extra-pdf PATH_TO_NMAP_PDF --output-dir OUTPUT_DIRECTORY
```

The placeholders above must be replaced with actual paths; quote paths containing spaces. The outputs are:

- `cpsa-study-materials.zip`: all six PDFs plus `PDF-SHA256SUMS.txt`.
- `PDF-SHA256SUMS.txt`: six individual PDF hashes, also stored inside the ZIP.
- `SHA256SUMS.txt`: six individual PDF hashes plus the ZIP hash; use this as the repository checksum file.
- `cpsa-study-materials.zip.sha256`: the ZIP hash alone, for checking before extraction.

The ZIP cannot contain its own checksum. Verify the ZIP against an external manifest, then extract it and verify its PDF manifest. SHA-256 confirms identical bytes, not who produced them or whether distribution is authorised. After a rebuild, the ZIP hash must be recomputed; do not reuse a previous hash.

Before a new upload, resolve the rights review and obtain publication approval. Preserve the existing release and asset. After uploading the new ZIP and checksum files, verify the uploaded size and digest, then add the actual returned download URL to the README. Never guess or publish an asset URL before upload succeeds.

## Keeping the hub current

When CREST changes the linked syllabus, compare every official skill ID and update the tracker and reviewed date. When adding a resource, record provenance, permission, exact location and size. Prefer linking to primary sources and writing original explanations over mirroring books.
