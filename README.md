# CREST Practitioner Security Analyst (CPSA) Study Guide 🛡️

A comprehensive study repository and reference guide for preparing for the **CREST Practitioner Security Analyst (CPSA)** examination.

---

## 📌 Table of Contents
- [About the Examination](#-about-the-examination)
- [Exam Breakdown & Domains](#-exam-breakdown--domains)
  - [1. Soft Skills and Assessment Management](#1-soft-skills-and-assessment-management)
  - [2. Core Technical Skills & Networking](#2-core-technical-skills--networking)
  - [3. Information Gathering & Reconnaissance](#3-information-gathering--reconnaissance)
  - [4. Threat & Vulnerability Assessment](#4-threat--vulnerability-assessment)
  - [5. Operating System & Host Security](#5-operating-system--host-security)
  - [6. Network & Infrastructure Security](#6-network--infrastructure-security)
  - [7. Web Application Security](#7-web-application-security)
- [Essential Tooling & Quick Reference](#-essential-tooling--quick-reference)
- [Hands-on Practice & Labs](#-hands-on-practice--labs)
- [Recommended Resources](#-recommended-resources)
- [Exam Strategy & Tips](#-exam-strategy--tips)
- [Repository Structure](#-repository-structure)
- [Contributing](#-contributing)
- [Disclaimer](#-disclaimer)

---

## 🎯 About the Examination

The **CREST CPSA** is an entry-level technical examination assessing candidate knowledge in technical information security, network testing, and web application testing. It is a prerequisite for the hands-on **CREST Registered Tester (CRT)** examination.

| Detail | Specification |
| :--- | :--- |
| **Delivery Provider** | Pearson VUE test center |
| **Question Format** | 120 Multiple Choice Questions (Single-choice & Multi-select) |
| **Duration** | 2 Hours (120 minutes) |
| **Pass Mark** | ~60% |
| **Prerequisites** | None formally required (hands-on experience recommended) |
| **Validity** | 3 years |

---

## 📚 Exam Breakdown & Domains

### 1. Soft Skills and Assessment Management
* **Ethics & Professional Conduct**: CREST Code of Conduct, nondisclosure agreements (NDA), ethical boundaries.
* **Legislation & Regulations**:
  * UK Computer Misuse Act (1990) Sections 1, 2, 3, 3ZA, and 3A.
  * Data Protection Act / GDPR, Human Rights Act 1998, Police and Justice Act 2006.
* **Scoping & Rules of Engagement**:
  * In-scope vs. out-of-scope assets, testing windows, emergency escalation paths.
  * Third-party hosted environments (e.g., AWS, Azure shared responsibility models).

### 2. Core Technical Skills & Networking
* **TCP/IP Protocol Suite & OSI Model**: Layer 2–7 mapping, frame/packet structures.
* **Subnetting & Addressing**: IPv4 CIDR calculations, private address ranges (RFC 1918), IPv6 structure.
* **Protocols & Common Ports**:
  * DNS (53), DHCP (67/68), SMB (445), RPC (135), SNMP (161/162), LDAP (389/636), Kerberos (88).
  * HTTP (80) / HTTPS (443), SSH (22), Telnet (23), FTP (20/21), SMTP (25), RDP (3389).
* **TCP Flags & Handshakes**:
  * 3-way handshake (`SYN` -> `SYN/ACK` -> `ACK`).
  * Teardown (`FIN`/`ACK` or `RST`).
  * TCP flag interpretation in port scanning (`FIN`, `XMAS`, `NULL`).

### 3. Information Gathering & Reconnaissance
* **Passive Reconnaissance (OSINT)**:
  * Public registries, WHOIS, ARIN/RIPE/APNIC queries.
  * Search engine operators (Google Dorking), Shodan, Censys, certificate transparency logs (`crt.sh`).
* **DNS Interrogation**:
  * Record types: `A`, `AAAA`, `MX`, `TXT` (SPF/DKIM/DMARC), `NS`, `SOA`, `PTR`, `SRV`.
  * Zone transfers (AXFR), DNS brute-forcing, reverse lookups.
* **Active Reconnaissance**:
  * Network sweeping, host discovery (ARP, ICMP echo/timestamp), TCP/UDP service fingerprinting.

### 4. Threat & Vulnerability Assessment
* **Vulnerability Scanning**:
  * Network vs. web application vulnerability scanning.
  * Differentiating between vulnerabilities, misconfigurations, and standard configurations.
* **False Positives / Negatives**: Identification, validation methods, and verification without causing disruption.
* **CVSS Scoring**: Understanding Base, Temporal, and Environmental metrics (AV, AC, PR, UI, S, C, I, A).

### 5. Operating System & Host Security
* **Windows Security Architecture**:
  * Windows authentication protocols: NTLM vs. Kerberos (TGT, TGS, PAC).
  * Access Control Lists (ACLs), DACLs, SACLs, and Security Identifiers (SIDs).
  * SAM database vs. Active Directory NTDS.dit database.
  * Windows services, registry keys, and privilege escalation vectors.
* **Linux / Unix Security Architecture**:
  * File permissions (`rwx`, `chmod`, `chown`), SUID (`4000`), SGID (`2000`), Sticky Bit (`1000`).
  * `/etc/passwd` vs. `/etc/shadow` structure.
  * Common logging paths: `/var/log/auth.log`, `/var/log/secure`, `/var/log/syslog`.

### 6. Network & Infrastructure Security
* **Filtering & Perimeter Defense**:
  * Packet-filtering firewalls, stateful firewalls, application firewalls (WAF).
  * IDS vs. IPS (signature-based vs. anomaly-based detection).
* **Wireless Technologies**:
  * 802.11 standards and security modes (WEP, WPA-Personal, WPA-Enterprise, WPA2, WPA3).
  * 4-Way Handshake analysis and EAP methods (PEAP, EAP-TLS).
* **Network Segmentation & Routing**:
  * VLAN hopping, ARP spoofing/poisoning, DHCP starvation, rogue gateway attacks.

### 7. Web Application Security
* **OWASP Top 10 Concepts**:
  * **Injection**: SQL Injection (In-band, Error-based, Boolean/Time blind), Command Injection, LDAP injection.
  * **Broken Authentication**: Session fixation, credential stuffing, weak token generation.
  * **Cross-Site Scripting (XSS)**: Reflected, Stored, and DOM-based; exploitation & mitigation (CSP, sanitization).
  * **Cross-Site Request Forgery (CSRF)**: Mechanism, SameSite cookie attributes, anti-CSRF tokens.
  * **Insecure Direct Object References (IDOR)**: Access control verification.
  * **Server-Side Request Forgery (SSRF)**: Internal network pivoting, cloud metadata queries (`169.254.169.254`).
* **HTTP Fundamentals**:
  * Request/Response headers (`Host`, `User-Agent`, `Referer`, `Set-Cookie`, `Authorization`).
  * Security Headers (`Strict-Transport-Security`, `Content-Security-Policy`, `X-Frame-Options`).

---

## 🛠️ Essential Tooling & Quick Reference

### Nmap Scanning Modes
| Command | Scan Type | Description |
| :--- | :--- | :--- |
| `nmap -sS <target>` | SYN Stealth Scan | Half-open scan; does not complete TCP handshake |
| `nmap -sT <target>` | Connect Scan | Full TCP connection; noisy, used without raw socket privileges |
| `nmap -sU <target>` | UDP Scan | Probes common UDP ports (ICMP Port Unreachable = closed) |
| `nmap -sV -sC <target>` | Version & Script | Default NSE scripts with service version detection |
| `nmap -p- --min-rate 1000 <target>` | Full Port Scan | Scans all 65,535 TCP ports at high rate |

### DNS & Active Directory Recon
```bash
# DNS Zone Transfer attempt
dig axfr @<nameserver> <domain.com>

# Reverse DNS lookup range
dig -x <ip>

# Active Directory enumeration via SMB
enum4linux -a <target-ip>
crackmapexec smb <target-ip> -u '' -p '' --shares
```

### Web & Proxy
* **Burp Suite / OWASP ZAP**: Intercepting proxies for traffic manipulation and repeater analysis.
* **Nikto / Gobuster**:
  ```bash
  # Web server vulnerability scan
  nikto -h http://<target>

  # Directory enumeration
  gobuster dir -u http://<target> -w /usr/share/wordlists/dirb/common.txt
  ```

---

## 🧪 Hands-on Practice & Labs

1. **[PortSwigger Web Security Academy](https://portswigger.net/web-security)**: Free, industry-standard training for web application security topics.
2. **[TryHackMe](https://tryhackme.com)**:
   * *Pre-Security Path* (Networking & HTTP basics)
   * *Junior Penetration Tester Path* (Core penetration testing workflow)
3. **[Hack The Box](https://www.hackthebox.com)**:
   * "Easy" Linux and Windows machines focusing on enumeration, service exploits, and basic privilege escalation.

---

## 📖 Recommended Resources

* **Official CREST Syllabus**: [CREST CPSA Technical Syllabus](https://www.crest-approved.org/)
* **Books**:
  * *The Web Application Hacker's Handbook (2nd Edition)* — Dafydd Stuttard & Marcus Pinto
  * *Network Security Assessment (3rd Edition)* — Chris McNab
  * *RTFM: Red Team Field Manual* — Ben Clark
* **Legislation**:
  * UK Crown Legislation: Computer Misuse Act 1990

---

## 💡 Exam Strategy & Tips

1. **Pace Yourself**: You have 120 minutes for 120 questions (1 minute per question). Flag uncertain questions and return to them later.
2. **Read the Wording Carefully**: Watch out for "NOT", "MOST effective", or multi-select instructions ("Select TWO").
3. **Know Port Numbers Cold**: Expect questions requiring direct recall of obscure and common port numbers and their corresponding protocol details.
4. **Understand Output Analysis**: Be ready to interpret raw snippets of:
   * `nmap` output
   * `tcpdump` / Wireshark packet traces
   * HTTP request/response headers
   * SQL error messages

---

## 📂 Repository Structure

```text
├── README.md               # Main CPSA Overview & Study Guide
├── notes/
│   ├── legal-and-ethics.md # CMA 1990, GDPR, CREST Conduct
│   ├── networking.md       # TCP/IP, OSI, Subnetting, Ports
│   ├── os-security.md      # Windows & Linux internals
│   └── web-security.md     # OWASP Top 10 & HTTP analysis
└── cheatsheets/
    ├── nmap-cheatsheet.md  # Port scanning and flags
    └── common-ports.md     # Port to protocol mapping table
```

---

## 🤝 Contributing

Contributions, fixes, and expanded notes are welcome! Please open an issue or submit a pull request if you have revisions or additional practice resources.

---

## ⚖️ Disclaimer

*This study guide is an independent community resource created for educational purposes. It is not officially endorsed or sponsored by CREST.*
