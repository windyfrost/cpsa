# Network and infrastructure security

[Study roadmap](study-plan.md) · [Syllabus tracker](syllabus.md) · [Home](../README.md)

Official mapping: D; B6, B10–B12. These introductory notes are not exhaustive.

## Key distinctions

Segmentation reduces reachable paths but does not itself authenticate users or encrypt traffic. Review ingress and egress rules in context, including order, defaults and management interfaces. A passive IDS detects; an inline IPS can block. A WAF focuses on application traffic and does not replace application access controls.

WEP, TKIP and older wireless mechanisms remain syllabus study topics; inclusion is not a recommendation to deploy them. Device configuration analysis, SIP/VoIP and IPsec need additional study beyond these notes.

## Topic reference

* **Filtering & Perimeter Defense**:
  * Packet-filtering firewalls, stateful firewalls, application firewalls (WAF).
  * IDS vs. IPS (signature-based vs. anomaly-based detection).
* **Wireless Technologies**:
  * 802.11 standards and security modes (WEP, WPA-Personal, WPA-Enterprise, WPA2, WPA3).
  * 4-Way Handshake analysis and EAP methods (PEAP, EAP-TLS).
* **Network Segmentation & Routing**:
  * VLAN hopping, ARP spoofing/poisoning, DHCP starvation, rogue gateway attacks.

## Revision checklist

- [ ] Review device management, segmentation, wireless security and traffic.
- [ ] Distinguish a firewall decision from IDS observation and IPS enforcement.
- [ ] Explain one finding, its evidence, its limitations and a suitable mitigation.
- [ ] Compare this note with every relevant official syllabus skill ID and record missing topics.

## Apply it

Review a fictional firewall rule set and a supplied PCAP; identify allowed paths and management exposure. See the [authorised lab workflow](practice.md) and [topic references](recommended-reading.md).

Last reviewed: 2026-11-10.
