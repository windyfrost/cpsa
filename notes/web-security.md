# Web applications and databases

[Study roadmap](../docs/study-plan.md) · [Syllabus tracker](../syllabus/README.md) · [Home](../README.md)

Official mapping: G–J. These introductory notes are not exhaustive.

## Key distinctions

Authentication establishes an identity; authorisation decides which action that identity may take. A hidden URL or object identifier is not an access control. Cookies and tokens carry state but do not by themselves guarantee a secure session.

For XSS, use context-appropriate output encoding and safe APIs; sanitise intentionally allowed HTML. CSP is defence in depth. SQL parameterisation separates values from query structure. CSRF concerns unwanted authenticated requests; XSS concerns script execution in a browser context.

Study the database tier explicitly: connection identities, least privilege, patch/version evidence and application-to-database trust. J1–J3 cover database-specific issues absent from the original notes. Use vendor documentation and the web references in [recommended reading](../resources/recommended-reading.md).

## Topic reference

* **Web security concepts**:
  * **Injection**: SQL Injection (In-band, Error-based, Boolean/Time blind), Command Injection, LDAP injection.
  * **Broken Authentication**: Session fixation, credential stuffing, weak token generation.
  * **Cross-Site Scripting (XSS)**: Reflected, Stored, and DOM-based; exploitation & mitigation (context-aware output encoding, safe APIs, HTML sanitisation and CSP).
  * **Cross-Site Request Forgery (CSRF)**: Mechanism, SameSite cookie attributes, anti-CSRF tokens.
  * **Insecure Direct Object References (IDOR)**: Access control verification.
  * **Server-Side Request Forgery (SSRF)**: Internal network pivoting, cloud metadata queries (`169.254.169.254`).
* **HTTP Fundamentals**:
  * Request/Response headers (`Host`, `User-Agent`, `Referer`, `Set-Cookie`, `Authorization`).
  * Security Headers (`Strict-Transport-Security`, `Content-Security-Policy`, `X-Frame-Options`).

## Revision checklist

- [ ] Connect HTTP and application architecture to testing methodology, techniques and database access.
- [ ] Distinguish authentication, authorisation, XSS, CSRF and injection.
- [ ] Explain one finding, its evidence, its limitations and a suitable mitigation.
- [ ] Compare this note with every relevant official syllabus skill ID and record missing topics.

## Apply it

Use a hosted training lab to trace login, session state, object access and a database-backed request. See the [authorised lab workflow](../practice/README.md) and [topic references](../resources/recommended-reading.md).

Last reviewed: 2026-11-10.
