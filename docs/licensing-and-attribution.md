# Licensing and attribution review

[Home](../README.md) · [Download catalogue](downloads.md) · [Audit](audit.md)

Corrected 2026-11-10. The owner clarified that they do not have redistribution permission for the six PDFs, withdrawing the earlier confirmation. The five tracked PDFs were removed from the cleanup branch; the Nmap PDF asset was removed from v1.0.0, and v1.1.0 remains a draft. Earlier permission statements in Git history must not be relied on. No repository-wide license or downstream reuse grant is established.

## Review register

| Resource | Classification and evidence | Current disposition |
| --- | --- | --- |
| Original README and derived Markdown notes | Repository-authored educational material; authorship and inbound rights not independently established | Retained as original study links and notes; owner may choose a license for original work |
| CREST syllabus PDF | Third-party CREST document, v2.5; opening pages contain copying restrictions | Removed from the current repository; official CREST link retained |
| Gray Hat Hacking, third edition | Third-party commercial book; opening pages identify the title and carry a third-party site watermark | Removed from the current repository |
| Hacking Exposed Linux, third edition | Third-party commercial book; opening pages identify the title and carry a third-party site watermark | Removed from the current repository |
| Network Security Assessment, third edition | Third-party book; copyright page identifies Chris McNab / O'Reilly and reserved rights; third-party watermark present | Removed from the current repository |
| RTFMv3.pdf | Third-party Ben Clark work; existing copy includes a modification-without-permission notice and reserved reproduction rights | Removed from the current repository |
| Nmap release PDF | Third-party Gordon Lyon book; title and asset digest were verified | Asset removed from v1.0.0; official online book link retained |

All six PDFs are third-party works, not repository-authored works. Their authors' rights remain intact. The license of an online excerpt or tool manual must not be assumed to cover a full commercial book.

## Existing-content policy

The newly created ZIP release is a draft. The five PDFs were removed from the cleanup branch and the Nmap asset was removed from v1.0.0. Git history still contains older commits with the five PDFs. Because the v1.0.0 tag points to a commit containing those PDFs, GitHub's generated source archives remain accessible and may include them. The original mission forbids rewriting Git history; this cleanup does not erase historical Git objects. Prefer official author or publisher links, original notes and openly licensed materials.

## Source attribution

The topic notes and command reference were reorganised from this repository's README at commit `48da6e2`, with clarifications and coverage caveats. [Recommended reading](recommended-reading.md) retains its useful external references. CREST owns its syllabus and certification materials; linked authors and publishers retain their rights. No CREST endorsement is implied. Do not submit confidential engagement data, leaked exams or recalled live-exam questions.
