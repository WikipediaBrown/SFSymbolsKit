#!/usr/bin/env python3
"""Single source of truth for the SFSymbols catalog version.

The version (e.g. "7.2") is external knowledge: it's the SF Symbols
app release the names in SFSymbols.txt were exported from. It can't be
inferred from the flat name list, so a maintainer records it once in
the SFSYMBOLS_VERSION file when they re-export a new catalog.

This script propagates that single value everywhere it's stated so the
README and the website can't drift from the actual catalog. It is run
automatically at the end of generateSymbols.sh, so regenerating the
package always re-syncs the version.

Idempotent: safe to run repeatedly.
"""
import io, re, sys, pathlib

ROOT = pathlib.Path(__file__).parent
version = (ROOT / "SFSYMBOLS_VERSION").read_text(encoding="utf-8").strip()
if not re.fullmatch(r"\d+(\.\d+)*", version):
    sys.exit(f"SFSYMBOLS_VERSION must be a version like 7.2 (got {version!r})")

changed = []

# 1) README.md — rewrite the managed region between the markers.
readme = ROOT / "README.md"
text = readme.read_text(encoding="utf-8")
start, end = "<!-- sfsymbols-version:start -->", "<!-- sfsymbols-version:end -->"
managed = f"{start}Apple's **SFSymbols {version}** catalog{end}"
if start in text and end in text:
    new = re.sub(re.escape(start) + r".*?" + re.escape(end), managed, text, flags=re.S)
else:
    # First run: replace the existing plain phrase with the managed one.
    new = re.sub(r"Apple's \*\*SFSymbols [\d.]+\*\* catalog", managed, text, count=1)
if new != text:
    readme.write_text(new, encoding="utf-8")
    changed.append("README.md")

# 2) Jekyll site data — drives any template via {{ site.data.sfsymbols.version }}.
data = ROOT / "docs" / "_data" / "sfsymbols.yml"
desired = f'version: "{version}"\n'
if not data.exists() or data.read_text(encoding="utf-8") != desired:
    data.parent.mkdir(parents=True, exist_ok=True)
    data.write_text(desired, encoding="utf-8")
    changed.append("docs/_data/sfsymbols.yml")

print(f"SFSymbols version = {version}; synced: {changed or 'nothing (already current)'}")
