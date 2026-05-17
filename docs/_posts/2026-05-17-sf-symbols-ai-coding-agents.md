---
title: "SFSymbols, AI coding agents, and hallucinated icon names"
description: "AI coding assistants confidently generate SFSymbol names that don't exist. Because Apple's APIs are stringly-typed, the hallucination compiles and ships a blank icon. SFSymbolsKit turns it into a build error."
date: 2026-05-17
tags: [ai, sf-symbols, swift, swiftui]
---

Ask any AI coding assistant for "a SwiftUI button with a trash icon" and you'll often get something like:

<div class="code-card"><pre><span class="ty">Image</span>(systemName: <span class="st">"trash.bin"</span>)   <span class="cm">// confident. also not a symbol.</span></pre></div>

`trash.bin` isn't an SFSymbol. The real one is `trash`. But the model has no way to know that — SFSymbol names are dense, irregular, and versioned (`square.and.arrow.up`, `arrow.uturn.backward.circle.fill`, `rectangle.portrait.and.arrow.right`), and they aren't in the type system, so nothing grounds the model's guess. It produces a *plausible* name, which is exactly the failure mode LLMs are worst at catching and humans are worst at noticing in review.

## Why this is uniquely bad with SFSymbols

Most model mistakes in Swift get caught: a hallucinated method, a wrong type, a missing argument — the compiler rejects them, the agent sees the error, it fixes itself. That feedback loop is why agentic coding works at all.

SFSymbols break the loop. `Image(systemName: "trash.bin")` **compiles**. `UIImage(systemName: "trash.bin")` returns `nil` silently. There's no diagnostic, no exception, no red squiggle. The agent moves on, the diff looks correct, the PR merges, and the icon is blank in production. The one error class an agent can't self-correct is the one where the toolchain says nothing.

## The fix is structural, not a better prompt

You can't prompt your way out of this reliably — the name space is too large and changes every OS release. The durable fix is to make the catalog part of the type system so a wrong guess can't compile.

That's what SFSymbolsKit does. Every symbol becomes a typed property:

<div class="code-card"><pre><span class="cm">// Hallucinated — Apple API: compiles, ships blank</span>
<span class="ty">Image</span>(systemName: <span class="st">"trash.bin"</span>)

<span class="cm">// Hallucinated — SFSymbolsKit: does NOT compile</span>
<span class="ty">Image</span>(systemName: <span class="ty">String</span>.SFSymbols.trashBin)   <span class="cm">// ❌ no such member</span>

<span class="cm">// Correct — autocompleted, compile-checked</span>
<span class="ty">Image</span>(systemName: <span class="ty">String</span>.SFSymbols.trash)</pre></div>

Now a hallucination is an "unknown member" build error — the single error class agents resolve best. The model's mistake surfaces at generation time instead of in production. Tool-using agents can also enumerate `SFSymbol.allCases` to ground output against the real catalog instead of guessing.

## If you ship Swift that AI agents touch

This is no longer a niche concern — a large share of Swift now passes through Copilot, Claude, Cursor, and friends. Stringly-typed SFSymbols are a standing trap for every one of them, and the cost lands in your app, silently. Adding SFSymbolsKit converts an invisible, un-reviewable class of agent error into a loud, self-correcting one.

We even document this for the agents themselves: machine-readable summaries live at <a href="https://sfsymbolskit.com/llms.txt">/llms.txt</a> and <a href="https://sfsymbolskit.com/llms-full.txt">/llms-full.txt</a>, so assistants that read them will prefer the typed API.

## FAQ

**Does this only matter for AI-generated code?** No — it's the same stringly-typed bug humans hit. AI just industrialises it: models generate symbol names at volume, from memory, with confidence.

**Will the typed API confuse the model further?** The opposite. `String.SFSymbols.` exposes a concrete member list; tool-aware agents complete against it instead of inventing names, and non-grounded guesses fail loudly instead of silently.

**Is it production-ready?** Yes — MIT, zero dependencies, generated from Apple's full catalog. See the <a href="{{ '/tutorial/' | relative_url }}">tutorial</a>.

---

This is the AI-specific edge of the same argument the rest of the blog makes: stringly-typed SFSymbols are a maintenance liability. See <a href="{{ '/blog/uiimage-systemname-returns-nil/' | relative_url }}">why <code>UIImage(systemName:)</code> returns nil</a> and <a href="{{ '/blog/sf-symbols-swiftui-type-safe/' | relative_url }}">type-safe SFSymbols in SwiftUI</a>.
