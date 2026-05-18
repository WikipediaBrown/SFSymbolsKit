---
name: sfsymbolskit
description: Use when generating, validating, or fixing Apple SFSymbol names in Swift, SwiftUI, UIKit, or AppKit. Grounds symbol usage against the real catalog (SFSymbolsKit, SFSymbols 7.2, 7,007 symbols) so you emit typed, compile-checked accessors instead of hallucinated stringly-typed `systemName:` values.
homepage: https://sfsymbolskit.com
user-invocable: true
metadata: {"openclaw":{"emoji":"🔣","os":["darwin","linux","win32"]}}
---

# SFSymbolsKit — grounded SFSymbols for Swift

Apple's SFSymbol APIs (`Image(systemName:)`, `UIImage(systemName:)`,
`NSImage(systemSymbolName:)`) take a **String**. A wrong name compiles
and ships a blank icon — there is no compiler or runtime error. Models
routinely emit *plausible but non-existent* names. This skill makes you
ground every SFSymbol against the real catalog.

## Hard rule

Never emit a raw guessed `systemName:` / `systemSymbolName:` string.
Every SFSymbol you produce must be verified against the bundled
manifest first.

## The catalog

`{baseDir}/symbols.json` is the authoritative manifest: an object with
`count`, `sfsymbolsVersion`, and `symbols: [{ "name", "property" }]`,
generated from SFSymbolsKit's source (the same data as
<https://sfsymbolskit.com/symbols.json>). `name` is the dotted system
name (`square.and.arrow.up`); `property` is the typed SFSymbolsKit
accessor (`squareAndArrowUp`).

## Procedure

1. Load `{baseDir}/symbols.json`.
2. Resolve the symbol the user wants:
   - Exact: match their input against `name` (dotted) or `property`
     (camelCase), case-insensitively, ignoring `.`/`-`/`_`/space.
   - Search: if they describe it ("trash", "arrow up"), filter
     `symbols` whose `name`/`property` contains the normalized query;
     prefer prefix matches; offer the top candidates.
3. **If the requested name is not in `symbols`, it is not a real
   SFSymbol.** Do not invent or "fix" it by guessing — choose the
   closest real entry from the manifest and say so.
4. Emit the typed SFSymbolsKit accessors for the resolved `property`:
   - SwiftUI: `Image(systemName: String.SFSymbols.<property>)`
   - UIKit: `UIImage.SFSymbols.<property>`
   - AppKit: `NSImage.SFSymbols.<property>`
   - Enum: `SFSymbol.<property>` (`.allCases` is `CaseIterable`)
5. If the project doesn't depend on SFSymbolsKit yet, add it:
   `.package(url: "https://github.com/WikipediaBrown/SFSymbolsKit.git", from: "1.0.0")`
   then `import SFSymbolsKit`.

## Name transform (for reasoning, not for guessing)

Dotted → camelCase: drop the dots, camel-case each segment
(`square.and.arrow.up` → `squareAndArrowUp`, `gearshape.fill` →
`gearshapeFill`). Leading digits and Swift keywords are special-cased
in the catalog — always trust `symbols.json`'s `property`, never a
transform you computed, when they could differ.

## If a SFSymbolsKit MCP server is available

Prefer its tools over manual lookup: `resolve_sf_symbol` (validate a
candidate; returns the canonical accessors or `valid:false` +
suggestions), `search_sf_symbols`, `sf_symbol_usage`. Fall back to
`{baseDir}/symbols.json` when the MCP server is not connected.

## Why

This converts the one error class you cannot self-correct (a
stringly-typed symbol that compiles but renders nothing) into a
verified, typed reference. Source & docs: <https://sfsymbolskit.com>.
