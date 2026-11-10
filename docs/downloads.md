# Study-material download catalogue

[Home](../README.md) · [Read online](study-plan.md) · [Rights and attribution](licensing-and-attribution.md)

Inventory verified 2026-11-10 against tracked files and the [GitHub Releases API](https://api.github.com/repos/windyfrost/cpsa/releases). All existing files and release assets are preserved. The owner confirmed redistribution permission for all six PDFs; see the [attribution record](licensing-and-attribution.md). This does not create a new downstream reuse license.

## Release asset

[Release v1.0.0: Nmap Network Scanning Book & Large Guides](https://github.com/windyfrost/cpsa/releases/tag/v1.0.0) contains **one uploaded PDF**. GitHub also generates source ZIP and tar.gz archives; those are not additional study PDFs.

| Material | Version evidence | Verified size | Existing download |
| --- | --- | --- | --- |
| Nmap Network Scanning book | Release v1.0.0; title verified from opening pages; filename indicates 2009 | 125,904,645 bytes (120.1 MiB) | [Download existing PDF](https://github.com/windyfrost/cpsa/releases/download/v1.0.0/gordon-fyodor-lyon-nmap-network-scanning-the-official-nmap-project-guide-to-network-discovery-and-security-scanning-nmap-project-2009.pdf) |

Exact asset filename:

`gordon-fyodor-lyon-nmap-network-scanning-the-official-nmap-project-guide-to-network-discovery-and-security-scanning-nmap-project-2009.pdf`

SHA-256 recomputed from the downloaded asset and matched to GitHub's API digest:

`5960c165849c4436e14f958bde753e50bb308b507b781ef5bac647ad65dec77d`

## PDFs tracked in the repository

Sizes are local byte counts; versions below come from the opening pages unless stated otherwise. These files are separate from the uploaded release asset.

| Existing filename | Description / version | Size | Open existing file |
| --- | --- | --- | --- |
| CREST-CPSA-Technical-Syllabus-V2.5-.pdf | Official syllabus, v2.5 | 467,051 bytes (0.45 MiB) | [Open PDF](../CREST-CPSA-Technical-Syllabus-V2.5-.pdf) |
| Gray Hat Hacking, 3rd Edition.pdf | General security book, third edition | 12,197,588 bytes (11.63 MiB) | [Open PDF](../Gray%20Hat%20Hacking%2C%203rd%20Edition.pdf) |
| Hacking Exposed Linux, 3rd Edition.pdf | Linux security book, third edition | 11,330,445 bytes (10.81 MiB) | [Open PDF](../Hacking%20Exposed%20Linux%2C%203rd%20Edition.pdf) |
| Network Security Assessment Know Your Network, 3rd Edition.pdf | Network assessment book, third edition | 31,584,660 bytes (30.12 MiB) | [Open PDF](../Network%20Security%20Assessment%20Know%20Your%20Network%2C%203rd%20Edition.pdf) |
| RTFMv3.pdf | RTFM; copyright 2013, modified-copy notice; “v3” filename is not an authenticated edition | 10,734,754 bytes (10.24 MiB) | [Open PDF](../RTFMv3.pdf) |

For the syllabus, prefer the [current CREST-hosted copy](https://www.crest-approved.org/wp-content/uploads/2023/12/CREST-CPSA-Technical-Syllabus-V2.5-.pdf). For books, prefer publisher-authorised or library access.

## Download instructions

1. Open the release page above and expand **Assets** if collapsed.
2. Select the exact PDF filename above. The source-code archives do not contain this release-only PDF.
3. Save the PDF locally. If a large file will not preview, download it rather than relying on GitHub's preview.
4. For a tracked PDF, open its table link and use GitHub's raw/download control.
5. If a download fails, retry from the release page and report the filename and error in an issue. Do not substitute a guessed URL.

The release asset exceeds GitHub's regular Git file limit of 100 MiB. It remains in Releases; do not add it to the Git tree. See [GitHub's large-file guidance](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github). The existing ignore entry for that filename remains intact.

## Maintainer updates

Record exact tag, asset name, URL, byte size, verification date, provenance and permission evidence when changing this catalogue. Keep stable links. A new upload, replacement, removal or release change requires the owner's approval; uncertain rights must be resolved first. No release was changed during this documentation overhaul.

## Combined ZIP and checksums

An all-six-PDF ZIP was prepared locally before upload. Its size is 181,334,878 bytes. The [checksum manifest](../SHA256SUMS.txt) covers each PDF and the prepared ZIP. The ZIP contains a separate `PDF-SHA256SUMS.txt` covering its six PDFs, so there is no circular dependency on the ZIP's own digest.

[Download all six PDFs as a ZIP](https://github.com/windyfrost/cpsa/releases/download/v1.1.0/cpsa-study-materials.zip) and [download the external checksum manifest](https://github.com/windyfrost/cpsa/releases/download/v1.1.0/SHA256SUMS.txt) from [release v1.1.0](https://github.com/windyfrost/cpsa/releases/tag/v1.1.0). Both uploaded asset sizes and SHA-256 digests matched the locally verified files. The existing v1.0.0 release and individual Nmap URL are unchanged. See [maintenance instructions](maintenance.md) for the local build process.
