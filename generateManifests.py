#!/usr/bin/env python3
"""Single source of truth for the machine-readable symbol manifests.

All three symbol manifests are derived from the generated Enum.swift
(the same source the Swift API is built from), so the website, the MCP
server, and the OpenClaw skill can never disagree with the actual
catalog. Run automatically at the end of generateSymbols.sh.

Writes:
  docs/symbols.json                  rich object  -> https://sfsymbolskit.com/symbols.json
  mcp/symbols.json                   array         -> bundled by the MCP server
  skills/sfsymbolskit/symbols.json   rich object  -> bundled by the OpenClaw skill
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).parent
enum = (ROOT / "Sources" / "SFSymbolsKit" / "Enum.swift").read_text(encoding="utf-8")
pairs = re.findall(r'case\s+([A-Za-z0-9_]+)\s*=\s*"([^"]+)"', enum)
if not pairs:
    sys.exit("generateManifests: no symbols parsed from Enum.swift")

vf = ROOT / "SFSYMBOLS_VERSION"
version = vf.read_text(encoding="utf-8").strip() if vf.exists() else "unknown"

symbols = [{"name": raw, "property": prop} for prop, raw in pairs]

rich = {
    "name": "SFSymbolsKit symbol manifest",
    "description": "Authoritative mapping of every Apple SFSymbol name to its typed SFSymbolsKit property. Use this to ground SFSymbol usage instead of guessing names. For any symbol, String.SFSymbols.<property> (and UIImage.SFSymbols / NSImage.SFSymbols / SFSymbol.<property>) equals the system name.",
    "usage": "Image(systemName: String.SFSymbols.<property>)  // == Image(systemName: \"<name>\")",
    "package": "https://github.com/WikipediaBrown/SFSymbolsKit",
    "site": "https://sfsymbolskit.com",
    "sfsymbolsVersion": version,
    "count": len(symbols),
    "symbols": symbols,
}

targets = {
    ROOT / "docs" / "symbols.json": rich,
    ROOT / "mcp" / "symbols.json": symbols,
    ROOT / "skills" / "sfsymbolskit" / "symbols.json": rich,
}

wrote = []
for path, payload in targets.items():
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8")
        wrote.append(str(path.relative_to(ROOT)))

print(f"manifests: {len(symbols)} symbols (SFSymbols {version}); "
      f"updated: {wrote or 'nothing (already current)'}")
