# Repository audit

Original audit snapshot, 2026-11-10. Baseline: `48da6e2` on `main`; tag `v1.0.0` points to that commit. Inspection covered every tracked path, the three-entry commit history, the tag, the public Releases API, README links and opening pages of all five tracked PDFs. No repository AGENTS.md was found. The Nmap release binary was not downloaded during that initial audit.

## Original findings

| Finding | Impact | Resolution / remaining work |
| --- | --- | --- |
| Seven tracked files: README, ignore file and five PDFs; no actual notes or cheatsheets directories | README tree promised files that did not exist | Created linked, substantive guides and references |
| Long README mixed onboarding, technical notes, commands and strategy | New readers had no clear first step or study sequence | Short front page, getting started and staged roadmap |
| No link from README to the existing release-only PDF or tracked books | Offline resources difficult to discover | Added a verified catalogue of six existing PDFs |
| Seven study domains described as exam breakdown | Could be mistaken for official syllabus structure | Mapped learning domains to ten official A–J groups |
| Generic CREST homepage used as syllabus reference | Readers had to find the actual document | Linked v2.5 from the current official CPSA page |
| Approximate pass mark and unsupported single-choice/multi-select claim | Exam information was imprecise | Used verified 72/120 and omitted unsupported question subtype claim |
| SYN scan called stealth; high-rate command lacked context; CVSS had no version | Could encourage incorrect interpretations | Retained commands with limitations; labelled CVSS v3.1 and distinguished v4.0 |
| Web topic list presented as OWASP Top 10; XSS mitigations were too broad | Taxonomy and mitigation could mislead | Renamed topic list and clarified context-aware defences |
| No contribution guide, license or attribution register | Maintenance and reuse expectations unclear | Added contribution instructions and a rights review register; no license invented |
| No verbatim duplicated study documents found in tracked tree | No deduplication needed | Moved useful README content into linked notes; all existing PDFs remain unchanged |

## Releases and large files

The API returned one published release, **v1.0.0 — Nmap Network Scanning Book & Large Guides**, with one uploaded PDF (125,904,645 bytes). The GitHub UI's three assets include two generated source archives. The uploaded PDF is over 100 MiB and is already excluded by the original .gitignore filename entry. No tracked file exceeds 100 MiB; the largest is 31,584,660 bytes. Exact inventory, URL and digest metadata appear in the [catalogue](downloads.md). No release or asset was modified.

## Syllabus comparison

CREST's current CPSA page links technical syllabus **v2.5**. Its ten groups differ from the README's seven learning buckets. The [tracker](syllabus.md) covers all official skill IDs and flags partial coverage rather than claiming a complete course. Major gaps include cryptography, historical Unix/network services, device configurations, Windows applications and patching, web architecture and database assessment. Webpage summaries contain mismatched descriptions; the technical PDF is the mapping authority.

The syllabus itself contains legacy technology and legal references. The new notes distinguish study scope from current deployment guidance. The original legal list is preserved as historical study pointers, not verified current legal advice.

## Provenance and access limitations

All five tracked PDFs are identifiable third-party works. Several contain external-site watermarks; RTFM carries an unauthorised-modification notice. Permission evidence is absent. See the [resource-by-resource review register](licensing-and-attribution.md). The release book's title/year are inferred from filename and metadata only. Its integrity and internal edition remain unverified.

The baseline README links did not reference actual nonexistent files directly; the broken promise was its directory diagram. External access and redirect findings are recorded in [validation results](validation.md), without treating access-denied responses as definitive dead links. Original community and training references remain accessible from [recommended reading](recommended-reading.md).

## Preservation

Technical topic lists moved to seven note files, tool commands to the command reference, platform suggestions to practice/recommended reading, and exam strategy to the study/exam guides. All original useful resource references remain linked. Unsupported exam predictions were removed rather than relabelled as fact. Existing PDF bytes, .gitignore and tag history were preserved.

## Minimalist follow-up

At the owner's request, the front page was reduced to PDFs, helpful links and checksum verification. The Medium preparation article is prominent again. All study and maintenance Markdown was consolidated under `docs/`, preserving its content and updating relative links. The original PDFs remain in place.

The Nmap release PDF was subsequently downloaded, its opening title pages inspected, and its SHA-256 independently matched to GitHub's existing digest. A six-PDF ZIP, an internal per-PDF manifest and external per-PDF/ZIP checksum files were prepared locally. The owner then confirmed redistribution permission for all six PDFs, enabling preparation of a new release while preserving v1.0.0.
