#!/usr/bin/env node
// SFSymbolsKit MCP server.
//
// NOT part of the SFSymbolsKit Swift package. It lives in the repo's
// top-level `mcp/` directory, outside `Sources/`, so Swift Package
// Manager never compiles or ships it. Standalone Node tool; this repo
// contains its source only — it is not auto-published anywhere.
//
// Purpose: AI coding agents hallucinate SFSymbol names because the
// names are dense, irregular, and not in the type system. This server
// lets an agent GROUND its output against the real catalog:
//   - search_sf_symbols : find symbols by query
//   - resolve_sf_symbol : validate a candidate; if not real, return the
//                         closest real suggestions
//   - sf_symbol_usage   : exact Swift snippets for a verified symbol
//
// Catalog source: symbols.json, generated from SFSymbolsKit's Enum.swift
// (same single source of truth as https://sfsymbolskit.com/symbols.json).

import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const here = dirname(fileURLToPath(import.meta.url));
/** @type {{name:string,property:string}[]} */
const SYMBOLS = JSON.parse(readFileSync(join(here, "symbols.json"), "utf8"));

const byName = new Map(SYMBOLS.map((s) => [s.name, s]));
const byProp = new Map(SYMBOLS.map((s) => [s.property.toLowerCase(), s]));

const snippets = (s) => ({
  name: s.name,
  property: s.property,
  swiftui: `Image(systemName: String.SFSymbols.${s.property})`,
  uikit: `UIImage.SFSymbols.${s.property}`,
  appkit: `NSImage.SFSymbols.${s.property}`,
  enum: `SFSymbol.${s.property}`,
});

// Cheap edit-distance for "did you mean" suggestions.
function lev(a, b) {
  const m = a.length, n = b.length;
  const d = Array.from({ length: m + 1 }, (_, i) => [i, ...Array(n).fill(0)]);
  for (let j = 0; j <= n; j++) d[0][j] = j;
  for (let i = 1; i <= m; i++)
    for (let j = 1; j <= n; j++)
      d[i][j] = Math.min(
        d[i - 1][j] + 1,
        d[i][j - 1] + 1,
        d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1)
      );
  return d[m][n];
}

function suggest(input, k = 5) {
  const q = input.toLowerCase().replace(/[.\s_-]/g, "");
  return SYMBOLS.map((s) => {
    const keyN = s.name.replace(/[.\s_-]/g, "");
    const keyP = s.property.toLowerCase();
    const dist = Math.min(lev(q, keyN), lev(q, keyP));
    return { s, dist };
  })
    .sort((a, b) => a.dist - b.dist)
    .slice(0, k)
    .map((x) => snippets(x.s));
}

const server = new McpServer({ name: "sfsymbolskit", version: "1.0.0" });

server.tool(
  "search_sf_symbols",
  "Search Apple SFSymbols by free-text query. Returns real symbols with their typed SFSymbolsKit accessors. Use this to find a symbol instead of guessing its name.",
  { query: z.string().describe("e.g. 'trash', 'arrow up', 'gear'"), limit: z.number().int().min(1).max(50).optional() },
  async ({ query, limit = 15 }) => {
    const q = query.toLowerCase().replace(/[.\s_-]/g, "");
    const scored = [];
    for (const s of SYMBOLS) {
      const n = s.name.replace(/[.\s_-]/g, "");
      const p = s.property.toLowerCase();
      let score = -1;
      if (n === q || p === q) score = 0;
      else if (n.startsWith(q) || p.startsWith(q)) score = 1;
      else if (n.includes(q) || p.includes(q)) score = 2;
      if (score >= 0) scored.push({ s, score, len: s.name.length });
    }
    scored.sort((a, b) => a.score - b.score || a.len - b.len);
    const hits = scored.slice(0, limit).map((x) => snippets(x.s));
    return {
      content: [{ type: "text", text: JSON.stringify({ query, count: hits.length, total: scored.length, results: hits }, null, 2) }],
    };
  }
);

server.tool(
  "resolve_sf_symbol",
  "Validate a candidate SFSymbol. Accepts a dotted name (square.and.arrow.up) OR a camelCase property (squareAndArrowUp). If it is a real symbol, returns the canonical typed accessors. If it is NOT real (a likely hallucination), returns valid:false plus the closest real suggestions. Call this before emitting any SFSymbol name you are not certain exists.",
  { input: z.string().describe("dotted name or camelCase property to verify") },
  async ({ input }) => {
    const exact = byName.get(input) || byProp.get(input.toLowerCase());
    if (exact) {
      return { content: [{ type: "text", text: JSON.stringify({ valid: true, ...snippets(exact) }, null, 2) }] };
    }
    return {
      content: [{ type: "text", text: JSON.stringify({ valid: false, input, message: "Not a real SFSymbol. Use one of the suggestions or search_sf_symbols.", suggestions: suggest(input) }, null, 2) }],
    };
  }
);

server.tool(
  "sf_symbol_usage",
  "Given a verified SFSymbol (dotted name or property), return exact Swift usage snippets for SwiftUI, UIKit, AppKit, and the SFSymbol enum.",
  { symbol: z.string().describe("a verified dotted name or camelCase property") },
  async ({ symbol }) => {
    const s = byName.get(symbol) || byProp.get(symbol.toLowerCase());
    if (!s) {
      return { content: [{ type: "text", text: JSON.stringify({ error: "Unknown symbol — resolve it first with resolve_sf_symbol.", suggestions: suggest(symbol) }, null, 2) }] };
    }
    return { content: [{ type: "text", text: JSON.stringify(snippets(s), null, 2) }] };
  }
);

const transport = new StdioServerTransport();
await server.connect(transport);
console.error(`sfsymbolskit-mcp ready — ${SYMBOLS.length} symbols (SFSymbols 7.2)`);
