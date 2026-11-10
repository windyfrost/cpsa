# Common ports

[Networking notes](../notes/networking.md) · [Home](../README.md)

These are conventional assignments, not proof of which application is running. Transport matters; validate with service evidence.

| Service | Port / transport | Revision cue |
| --- | --- | --- |
| DNS | 53 UDP and TCP | TCP also supports queries; it is not only for transfers |
| DHCPv4 | 67 server / 68 client, UDP | Address configuration |
| SMB | 445 TCP | File sharing and related services |
| RPC endpoint mapper | 135 TCP/UDP | Other RPC services may use dynamic ports |
| SNMP | 161 UDP; notifications 162 UDP | Device management |
| LDAP / LDAP over TLS | 389 / 636 TCP | Directory access; 389 can support StartTLS |
| Kerberos | 88 TCP/UDP | Ticket-based authentication |
| HTTP / HTTPS | 80 / 443 TCP | Web traffic can use other ports; HTTP/3 uses QUIC over UDP |
| SSH / Telnet | 22 / 23 TCP | Secure shell / legacy clear-text terminal |
| FTP | 21 TCP control; 20 TCP conventional active-mode data source | Passive-mode data uses negotiated ports |
| SMTP | 25 TCP | Mail relay; submission has separate conventions |
| RDP | 3389 TCP/UDP | Remote desktop |

Verify assignments against the [IANA service registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml), and explain the traffic rather than memorising numbers alone.
