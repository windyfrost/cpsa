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

## PDF distribution is on hold

The owner clarified that redistribution permission is not held. The five PDFs were removed from the cleanup branch, the Nmap PDF asset was removed from v1.0.0, and v1.1.0 remains a draft. The v1.0.0 tag and earlier Git commits still contain PDF copies. History was not rewritten. Do not republish the ZIP or restore the removed assets without permission.

## Keeping the hub current

When CREST changes the linked syllabus, compare every official skill ID and update the tracker and reviewed date. When adding a resource, record provenance, permission, exact location and size. Prefer linking to primary sources and writing original explanations over mirroring books.
