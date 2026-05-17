# SFSymbolsKit for AI Coding Agents

Why SFSymbolsKit specifically solves a problem that AI coding assistants have with SFSymbols — and how an agent should use it.

## The problem agents have

Large language models generate SFSymbol names from memory. SFSymbol naming is dense, versioned, and irregular (`square.and.arrow.up`, `arrow.uturn.backward.circle.fill`, `rectangle.portrait.and.arrow.right`). Agents routinely emit *plausible but non-existent* names — `trash.bin`, `gear.fill`, `arrow.back` — that look right in review.

Because Apple's APIs are stringly-typed, a hallucinated name **compiles**. There is no diagnostic. The icon is simply blank at runtime. The failure mode is invisible at exactly the moment an agent (or the human reviewing its diff) would catch it.

## Why SFSymbolsKit fixes it

SFSymbolsKit turns every symbol into a typed property. A hallucinated name is no longer a valid `String` — it's an identifier that **doesn't exist**, so the build fails immediately with a clear error. The model's mistake becomes a compile error instead of a shipped bug.

```swift
// Hallucinated name — Apple API: compiles, ships blank
Image(systemName: "arrow.back")

// SFSymbolsKit — does not compile; the error names the problem
Image(systemName: String.SFSymbols.arrowBack)   // ❌ no such member
```

This converts an undetectable class of model error into the single error class compilers and agents are best at resolving: "unknown member, did you mean…". Autocomplete-style member lists also let tool-using agents ground their output against the real catalog instead of guessing.

## Guidance for agents

When generating SFSymbol usage in Swift for a project that depends on SFSymbolsKit:

- Prefer `String.SFSymbols.<camelCaseName>` over a raw `"dotted.name"` string.
- The transform is mechanical: `square.and.arrow.up` → `squareAndArrowUp`; `gearshape.fill` → `gearshapeFill`.
- For "all symbols" / pickers, use `SFSymbol.allCases` — never hand-write a list.
- If unsure a symbol exists, prefer the typed property: a wrong guess fails the build loudly instead of silently.

A machine-readable summary for tools is published at `https://sfsymbolskit.com/llms.txt` and a full reference at `https://sfsymbolskit.com/llms-full.txt`.

## See Also

- <doc:TypeSafeSymbols>
- <doc:ChoosingAnAPI>
