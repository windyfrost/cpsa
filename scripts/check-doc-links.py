"""Check this hub's inline Markdown links without network access (Python 3)."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import os
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]


def slug(text):
    text = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", text)
    text = text.replace("`", "").lower()
    return "".join(c for c in text if c in "-_ " or unicodedata.category(c)[0] in "LN").replace(" ", "-")


def body_and_anchors(text):
    lines, anchors, counts = [], set(), {}
    fence = None
    h1s = 0
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            value = marker.group(1)
            if fence is None:
                fence = value
            elif value[0] == fence[0] and len(value) >= len(fence):
                fence = None
            continue
        if fence:
            continue
        lines.append(line)
        heading = re.match(r"^(#{1,6})\s+(.+?)(?:\s+#+)?$", line)
        if heading:
            h1s += len(heading.group(1)) == 1
            anchor = slug(heading.group(2))
            occurrence = counts.get(anchor, 0)
            counts[anchor] = occurrence + 1
            anchors.add(anchor if occurrence == 0 else f"{anchor}-{occurrence}")
    return "\n".join(lines), anchors, fence, h1s


def exact_exists(target):
    try:
        relative = target.relative_to(ROOT)
    except ValueError:
        return False
    parent = ROOT
    for part in relative.parts:
        if not parent.is_dir() or part not in {p.name for p in parent.iterdir()}:
            return False
        parent = parent / part
    return parent.exists()


def main():
    files = sorted(ROOT.rglob("*.md"))
    parsed = {p: body_and_anchors(p.read_text(encoding="utf-8")) for p in files}
    errors, links, external = [], 0, set()
    for file, (body, anchors, fence, h1s) in parsed.items():
        name = file.relative_to(ROOT).as_posix()
        if fence:
            errors.append(f"{name}: unclosed code fence")
        if h1s != 1:
            errors.append(f"{name}: expected one H1, found {h1s}")
        for match in re.finditer(r"(?<!!)\[[^\]\n]+\]\((<[^>]+>|[^)\n]+)\)", body):
            url = match.group(1).strip("<>")
            parts = urlsplit(url)
            if parts.scheme in ("https", "http"):
                external.add(url)
                continue
            if parts.scheme:
                continue
            links += 1
            # Keep the spelling supplied by the link. Path.resolve() may correct
            # its case on Windows before exact_exists() can detect a mismatch.
            target = Path(os.path.abspath(file.parent / unquote(parts.path))) if parts.path else file
            if not exact_exists(target):
                errors.append(f"{name}: missing or case-mismatched path: {url}")
            elif parts.fragment and target.suffix == ".md":
                if unquote(parts.fragment) not in parsed[target][1]:
                    errors.append(f"{name}: missing anchor: {url}")
    print(f"Checked {len(files)} Markdown files, {links} internal links and {len(external)} unique external URLs.")
    print("\n".join(errors) if errors else "PASS: paths, heading anchors, H1 counts and code fences.")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
