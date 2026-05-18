# sfsymbolskit-mcp

An [MCP](https://modelcontextprotocol.io) server that lets AI coding agents **search and validate Apple SFSymbol names** so they stop hallucinating them.

SFSymbol names are dense, irregular, and not in the Swift type system, so models routinely emit *plausible but non-existent* names (`trash.bin`, `arrow.back`). Because Apple's APIs are stringly-typed, the hallucination compiles and ships a blank icon. This server gives an agent the real catalog to ground against — the same catalog [SFSymbolsKit](https://sfsymbolskit.com) generates (SFSymbols 7.2, 7,007 symbols).

> **Not part of the Swift package.** This lives in the repo's top-level `mcp/` directory, outside `Sources/`, so Swift Package Manager never compiles or ships it. It's a standalone Node tool. This repository contains its **source only**; it is not auto-published to any registry.

## Tools

| Tool | Purpose |
|---|---|
| `search_sf_symbols` | Find symbols by free-text query → real names + typed `String.SFSymbols.*` / `UIImage` / `NSImage` / `SFSymbol` accessors |
| `resolve_sf_symbol` | Validate a candidate (dotted name or camelCase property). Real → canonical accessors. Not real → `valid:false` + closest suggestions (the anti-hallucination check) |
| `sf_symbol_usage` | Exact Swift snippets for a verified symbol |

## Run it

Requires Node ≥ 18.

```sh
cd mcp
npm install
node index.js        # stdio MCP server
```

## Use it from an MCP client

Example client config (e.g. Claude Desktop / any MCP-capable agent):

```json
{
  "mcpServers": {
    "sfsymbolskit": {
      "command": "node",
      "args": ["/absolute/path/to/SFSymbolsKit/mcp/index.js"]
    }
  }
}
```

Then an agent can call `resolve_sf_symbol("arrow.back")` and get back `valid:false` with the real alternatives, instead of shipping a blank icon.

## Catalog source

`symbols.json` is generated from SFSymbolsKit's `Enum.swift` — the same single source of truth as <https://sfsymbolskit.com/symbols.json>. Regenerate it alongside the package when the catalog changes.

MIT · <https://sfsymbolskit.com>
