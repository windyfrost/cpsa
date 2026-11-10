# CREST CPSA PDFs

PDF references and a few useful links for CREST Practitioner Security Analyst preparation.

## PDFs

| Resource | Size | Download |
| --- | --- | --- |
| CREST CPSA syllabus v2.5 | 0.4 MiB | [PDF](CREST-CPSA-Technical-Syllabus-V2.5-.pdf) |
| Gray Hat Hacking, 3rd edition | 11.6 MiB | [PDF](Gray%20Hat%20Hacking%2C%203rd%20Edition.pdf) |
| Hacking Exposed Linux, 3rd edition | 10.8 MiB | [PDF](Hacking%20Exposed%20Linux%2C%203rd%20Edition.pdf) |
| Network Security Assessment, 3rd edition | 30.1 MiB | [PDF](Network%20Security%20Assessment%20Know%20Your%20Network%2C%203rd%20Edition.pdf) |
| RTFM (existing modified copy) | 10.2 MiB | [PDF](RTFMv3.pdf) |
| Nmap Network Scanning | 120.1 MiB | [PDF](https://github.com/windyfrost/cpsa/releases/download/v1.0.0/gordon-fyodor-lyon-nmap-network-scanning-the-official-nmap-project-guide-to-network-discovery-and-security-scanning-nmap-project-2009.pdf) |

[Release downloads](https://github.com/windyfrost/cpsa/releases) · [SHA-256 checksums](SHA256SUMS.txt)

## Helpful links

- **[sudosuraj's CPSA preparation write-up on Medium](https://sudosuraj.medium.com/how-i-cleared-crest-cpsa-in-5-days-and-built-the-tool-that-made-it-possible-7d0dab2a4689)** — practical study experience from the original README.
- [Official CREST exam information and syllabus](https://www.crest-approved.org/skills-certifications-careers/crest-practitioner-security-analyst/).
- [Optional study notes](docs/getting-started.md).

## Verify a download

Compare the file's SHA-256 with its entry in [SHA256SUMS.txt](SHA256SUMS.txt). For example, in PowerShell:

```powershell
Get-FileHash .\RTFMv3.pdf -Algorithm SHA256
```

A matching checksum confirms identical bytes. PDFs retain their authors' rights; see [attribution](docs/licensing-and-attribution.md). This is an independent project, not endorsed by CREST.
