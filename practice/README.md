# Authorised practice

[Home](../README.md) · [Study plan](../docs/study-plan.md) · [Command reference](../cheatsheets/commands.md)

These are study activities, not official CREST questions or mock exams. Use your own isolated systems or training labs that explicitly permit the activity. Agree scope and impact before sending traffic.

## Learning sequence

| Focus | Activity | What to explain afterwards |
| --- | --- | --- |
| Foundations | Calculate CIDR ranges and inspect a saved handshake | Address counts, routing and TCP flags |
| Reconnaissance | Query DNS for your own domain and inspect source HTML | Record relationships, stale data and scope |
| Assessment | Compare a limited lab scan with known host configuration | False positives, false negatives and evidence confidence |
| Host security | Review local permissions on a disposable Windows or Unix VM | Effective access, identities and least privilege |
| Infrastructure | Annotate a permitted PCAP and sample firewall rules | Allowed paths, management exposure and monitoring limits |
| Web and databases | Complete a suitable hosted web lab | Request flow, session state, access control and database trust |

## Hosted training and further practice

- [PortSwigger Web Security Academy](https://portswigger.net/web-security): choose introductory authentication, access control, XSS and SQL injection labs after learning HTTP.
- [TryHackMe](https://tryhackme.com): the original guide suggested Pre-Security and Junior Penetration Tester paths; names and availability may change, so check the provider's catalogue.
- [Hack The Box](https://www.hackthebox.com): the original guide suggested introductory Linux and Windows machines. Choose within your current ability and the platform rules.
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/): structure methodology and evidence collection.

## Record and review

For each activity, write the permission boundary, hypothesis, exact tool/version, observed output, interpretation, limitation and mitigation. Restore the lab afterwards. Keep personal data, credentials, live target information and proprietary engagement output out of public commits.
