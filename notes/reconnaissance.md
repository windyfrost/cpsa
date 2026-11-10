# Information gathering

[Study roadmap](../docs/study-plan.md) · [Syllabus tracker](../syllabus/README.md) · [Home](../README.md)

Official mapping: C; B4, B8–B9. These introductory notes are not exhaustive.

## Key distinctions

Passive reconnaissance uses existing information; active reconnaissance sends traffic to systems or services. DNS queries still contact a resolver or server. Validate domain ownership, stale records and shared hosting before adding an address to a target list.

A zone transfer is not a reverse lookup. An AXFR request asks an authoritative server for zone contents; a PTR lookup resolves a reverse-DNS name.

## Topic reference

* **Passive Reconnaissance (OSINT)**:
  * Public registries, WHOIS, ARIN/RIPE/APNIC queries.
  * Search engine operators (Google Dorking), Shodan, Censys, certificate transparency logs (`crt.sh`).
* **DNS Interrogation**:
  * Record types: `A`, `AAAA`, `MX`, `TXT` (SPF/DKIM/DMARC), `NS`, `SOA`, `PTR`, `SRV`.
  * Zone transfers (AXFR), DNS brute-forcing, reverse lookups.
* **Active Reconnaissance**:
  * Network sweeping, host discovery (ARP, ICMP echo/timestamp), TCP/UDP service fingerprinting.

## Revision checklist

- [ ] Build an asset picture from public information and permitted discovery.
- [ ] Explain why missing discovery responses do not prove that a host is absent.
- [ ] Explain one finding, its evidence, its limitations and a suitable mitigation.
- [ ] Compare this note with every relevant official syllabus skill ID and record missing topics.

## Apply it

Draw a DNS record relationship map for a domain you control. Separate public observations from active requests. See the [authorised lab workflow](../practice/README.md) and [topic references](../resources/recommended-reading.md).

Last reviewed: 2026-11-10.
