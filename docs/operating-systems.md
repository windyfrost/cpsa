# Operating systems and host security

[Study roadmap](study-plan.md) · [Syllabus tracker](syllabus.md) · [Home](../README.md)

Official mapping: E–F; B13–B14. These introductory notes are not exhaustive.

## Key distinctions

Windows effective access depends on identities, group membership and applicable access controls. SACLs relate to auditing; DACLs govern access. On Unix, directory execute permission controls traversal; file and directory permissions have different effects. The sticky bit restricts deletion in shared directories rather than making files read-only.

Unix logging locations vary by distribution and logging stack; some systems use the systemd journal. The original examples below are not universal paths. Review E1–E9 and F1–F9: these notes do not yet explain all Windows applications, patch-management history, NFS, RPC, X11, mail or r* services.

## Topic reference

* **Windows Security Architecture**:
  * Windows authentication protocols: NTLM vs. Kerberos (TGT, TGS, PAC).
  * Access Control Lists (ACLs), DACLs, SACLs, and Security Identifiers (SIDs).
  * SAM database vs. Active Directory NTDS.dit database.
  * Windows services, registry keys, and privilege escalation vectors.
* **Linux / Unix Security Architecture**:
  * File permissions (`rwx`, `chmod`, `chown`), SUID (`4000`), SGID (`2000`), Sticky Bit (`1000`).
  * `/etc/passwd` vs. `/etc/shadow` structure.
  * Common logging paths: `/var/log/auth.log`, `/var/log/secure`, `/var/log/syslog`.

## Revision checklist

- [ ] Compare Windows and Unix identities, services, permissions and audit evidence.
- [ ] Explain why local Windows accounts and domain accounts have different identity stores.
- [ ] Explain one finding, its evidence, its limitations and a suitable mitigation.
- [ ] Compare this note with every relevant official syllabus skill ID and record missing topics.

## Apply it

Review a lab file ACL or Unix permission set and trace who can read and modify the file. See the [authorised lab workflow](practice.md) and [topic references](recommended-reading.md).

Last reviewed: 2026-11-10.
