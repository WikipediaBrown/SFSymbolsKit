---
title: "Using SFSymbols in SwiftUI: the type-safe way"
description: "SwiftUI's Image(systemName:) takes a String, so every icon in your app is a hand-typed name with no compiler safety net. Here's why that's a maintenance liability and how to fix it."
date: 2026-05-15
tags: [swiftui, sf-symbols, swift]
---

Every SFSymbol you put in a SwiftUI view goes through one initializer:

<div class="code-card"><pre><span class="ty">Image</span>(systemName: <span class="st">"square.and.arrow.up"</span>)</pre></div>

That argument is a `String`. Not an enum, not a generated constant — a string literal you typed by hand or pasted from the SFSymbols app. SwiftUI will happily compile `Image(systemName: "square.and.arow.up")` and render *nothing* at runtime. No warning. No crash. Just a blank space where your share icon should be.

In a toy project that's fine. In an app with a few hundred icons across dozens of screens, "is every one of these strings spelled correctly, today and after the next refactor" becomes a real, recurring maintenance cost.

## Why strings are the actual problem

The issue isn't that SFSymbols are bad — they're great. The issue is the *interface*. A `String` parameter means:

- **No autocomplete.** Xcode can't suggest symbol names. You context-switch to the SFSymbols app, search, copy, paste.
- **No compile-time validation.** The type system can't tell `"gear"` (valid) from `"gears"` (not a symbol). Both are `String`.
- **No refactor safety.** Rename a symbol usage with find-and-replace and fat-finger it? The compiler shrugs.
- **Silent runtime failure.** A wrong name doesn't throw. It renders empty. Your QA team finds it, or your users do.

This is the textbook definition of [stringly-typed code](https://wiki.c2.com/?StringlyTyped): using strings where a real type belongs, and paying for it in bugs that the compiler should have caught.

## The hand-rolled fix, and why it decays

The common senior-engineer response is a constants file:

<div class="code-card"><pre><span class="kw">enum</span> <span class="ty">Symbols</span> {
    <span class="kw">static let</span> share = <span class="st">"square.and.arrow.up"</span>
    <span class="kw">static let</span> settings = <span class="st">"gear"</span>
    <span class="cm">// ...however many your app touches</span>
}

<span class="ty">Image</span>(systemName: <span class="ty">Symbols</span>.share)</pre></div>

This works — until it doesn't. Someone adds a feature, needs a new icon, and now hand-maintains another constant. The file covers the symbols you've thought of; the other ~7,000 are still raw strings the moment you need one. And when Apple ships new symbols next OS cycle, your file silently falls behind. You've moved the maintenance burden, not removed it.

## The type-safe way

SFSymbolsKit is that constants file — except generated from Apple's entire catalog, kept current by regeneration, and shipped as a Swift Package:

<div class="code-card"><pre><span class="kw">import</span> <span class="ty">SwiftUI</span>
<span class="kw">import</span> <span class="ty">SFSymbolsKit</span>

<span class="kw">struct</span> <span class="ty">Toolbar</span>: <span class="ty">View</span> {
    <span class="kw">var</span> body: <span class="kw">some</span> <span class="ty">View</span> {
        <span class="ty">HStack</span> {
            <span class="ty">Image</span>(systemName: <span class="ty">String</span>.SFSymbols.squareAndArrowUp)
            <span class="ty">Image</span>(systemName: <span class="ty">String</span>.SFSymbols.gear)
            <span class="ty">Image</span>(systemName: <span class="ty">String</span>.SFSymbols.trash)
        }
    }
}</pre></div>

Now `String.SFSymbols.` triggers autocomplete listing every symbol Apple ships. A typo is a compile error, not a blank icon in production. Rename safely, jump-to-definition, find-all-usages — everything the type system gives you for normal Swift, now applied to icons.

You can also skip the `systemName:` round-trip entirely with the `Image` you actually want:

<div class="code-card"><pre><span class="ty">Label</span>(<span class="st">"Share"</span>, systemImage: <span class="ty">String</span>.SFSymbols.squareAndArrowUp)</pre></div>

## FAQ

**Does this change how SwiftUI renders the symbol?** No. `String.SFSymbols.gear` *is* the string `"gear"` — a typed binding to the same literal. SwiftUI does exactly what it did before; you just can't misspell it.

**What about symbol variants (`.fill`, `.circle`)?** Those are distinct symbols with their own names (`gearshape.fill`, `xmark.circle`), so they're distinct typed properties too. Same safety, all variants.

**Is there a runtime cost?** No. Static `let` bindings to string literals compile away to the literal at the call site.

---

This is the SwiftUI-specific version of a broader argument. For UIKit, see [SFSymbols in UIKit: a practical guide]({{ '/blog/sf-symbols-uikit-practical-guide/' | relative_url }}); for macOS, [SFSymbols in AppKit (NSImage)]({{ '/blog/sf-symbols-appkit-nsimage-guide/' | relative_url }}); for the full picture across every Apple framework, the [tutorial]({{ '/tutorial/' | relative_url }}) covers all three APIs.
