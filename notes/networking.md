# Core skills and networking

[Study roadmap](../docs/study-plan.md) · [Syllabus tracker](../syllabus/README.md) · [Home](../README.md)

Official mapping: B. These introductory notes are not exhaustive.

## Key distinctions

A TCP port number is only a convention: the application can use another port. UDP has no TCP-style handshake; silence can indicate loss, filtering or an application that did not answer. Separate host discovery from port scanning and version detection.

Cryptography is a coverage gap in the original notes. Be able to distinguish reversible encoding, encryption with keys, one-way hashing and keyed integrity checks. Learn the legacy algorithms in B11–B12 as historical assessment topics, not deployment recommendations.

## Topic reference

* **TCP/IP Protocol Suite & OSI Model**: Layer 2–7 mapping, frame/packet structures.
* **Subnetting & Addressing**: IPv4 CIDR calculations, private address ranges (RFC 1918), IPv6 structure.
* **Protocols & Common Ports**:
  * DNS (53), DHCP (67/68), SMB (445), RPC (135), SNMP (161/162), LDAP (389/636), Kerberos (88).
  * HTTP (80) / HTTPS (443), SSH (22), Telnet (23), FTP (20/21), SMTP (25), RDP (3389).
* **TCP Flags & Handshakes**:
  * 3-way handshake (`SYN` -> `SYN/ACK` -> `ACK`).
  * Teardown (`FIN`/`ACK` or `RST`).
  * TCP flag interpretation in port scanning (`FIN`, `XMAS`, `NULL`).

## Revision checklist

- [ ] Read network traffic and tool output; understand addressing, cryptography and permissions.
- [ ] Explain why a service banner is evidence to validate, rather than proof of a vulnerability.
- [ ] Explain one finding, its evidence, its limitations and a suitable mitigation.
- [ ] Compare this note with every relevant official syllabus skill ID and record missing topics.

## Apply it

Calculate a subnet and explain a saved TCP handshake. Compare encoding, hashing and encryption. See the [authorised lab workflow](../practice/README.md) and [topic references](../resources/recommended-reading.md).

Last reviewed: 2026-11-10.
