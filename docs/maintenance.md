# Review and publication

[Home](../README.md) · [Audit](audit.md) · [Validation results](validation.md)

## Review locally

The changes are on `docs/cpsa-study-hub-overhaul`. Inspect the [audit](audit.md), [catalogue](../resources/downloads.md), [syllabus tracker](../syllabus/README.md) and [rights register](../resources/licensing-and-attribution.md) first. Use `git diff main...HEAD --stat` and `git diff main...HEAD` after the local commits are made. No push, pull request, merge or release change is part of this local handoff.

## Validation

Run from the repository root with Python 3:

```text
python scripts/check-doc-links.py
git diff --check main...HEAD
```

The script checks inline Markdown file links, exact path case, heading fragments, fence balance and duplicate H1s. It does not implement every Markdown syntax form and does not validate remote URL fragments. Review external links separately; blocked requests require a browser check.

To inspect GitHub formatting before publication, render Markdown with GitHub's Markdown API using relative context, then preview the resulting HTML. A local render confirms generated structure; final sidebar, downloads and mobile appearance still need a post-approval GitHub review.

## Publishing after owner approval

1. Review rights concerns and confirm whether the current catalogue should remain as drafted. Any distribution changes need separate approval.
2. Recheck CREST information and release metadata if time has passed.
3. After explicit publication approval, push the feature branch and open a pull request against main. Describe the documentation changes, preservation and validation limits.
4. Review the README and relative links on the branch in GitHub, including mobile width and the Releases route.
5. Merge only after the owner approves the reviewed change. Do not rewrite tags, force-push or alter release assets.

## Keeping the hub current

When CREST changes the linked syllabus, compare every official skill ID and update the tracker and reviewed date. When adding a resource, record provenance, permission, exact location and size. Prefer linking to primary sources and writing original explanations over mirroring books.
