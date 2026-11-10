# Command reference

[Home](../README.md) · [Lab workflow](practice.md)

The original commands are retained below as lab references. Replace angle-bracket values with your explicitly authorised lab targets; they are not literal shell syntax. Confirm installed tool help, permissions, scope and rate limits first.

### Nmap Scanning Modes
| Command | Scan Type | Description |
| :--- | :--- | :--- |
| `nmap -sS <target>` | TCP SYN scan | Normally does not complete the handshake; detectable and usually requires raw-packet privileges |
| `nmap -sT <target>` | Connect Scan | Uses the OS connection API; completes connections to open ports |
| `nmap -sU <target>` | UDP Scan | Probes common UDP ports (ICMP Port Unreachable = closed) |
| `nmap -sV -sC <target>` | Version & Script | Service detection and default NSE scripts; review script behaviour before use |
| `nmap -p- --min-rate 1000 <target>` | Full Port Scan | TCP ports 1–65535; requests at least 1000 probes/sec, which may affect reliability or services |

### DNS & Active Directory Recon
```bash
# DNS Zone Transfer attempt
dig axfr @<nameserver> <domain.com>

# Reverse DNS lookup for one IP address
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

## Interpretation and prerequisites

- A SYN scan is detectable; the term “stealth” does not mean invisible. A filtered result does not prove a host is absent.
- UDP silence can yield an ambiguous open-or-filtered state. Validate with protocol-aware checks within scope.
- Default NSE scripts and web scanners can send many requests. Inspect what will run and agree impact limits.
- Start with a small port set and conservative timing. The retained high-rate example is not a default recommendation.
- SMB enumeration depends on permissions and server policy. Anonymous failure does not prove no shares exist. CrackMapExec syntax is retained as a legacy reference; check the installed tool and version.
- Gobuster requires an installed wordlist; the example path is distribution-specific. Burp and ZAP are intercepting proxies; repetition of individual requests depends on the tool UI.

Primary reference: [Nmap manual](https://nmap.org/book/man.html). Use vendor documentation for current installation and syntax. Last reviewed: 2026-11-10.
