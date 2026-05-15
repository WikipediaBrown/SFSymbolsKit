---
title: "Typed vs stringly-typed SF Symbols in Swift"
description: "Comparing the ways to reference SF Symbols safely in Swift — raw strings, hand-rolled enums, SFSafeSymbols, and SFSymbolsKit — and what the maintenance cost of each actually is."
date: 2026-05-06
tags: [sf-symbols, swift, comparison]
---

If you've decided hand-typed symbol strings are a liability (they are — that's the rest of this blog), the next question is *which* typed approach to use. There are a few, they're not equivalent, and the differences are about maintenance, not syntax.

## The options

**1. Raw strings.** The default. `Image(systemName: "gear")`. No autocomplete, no compile check, silent runtime failure. This is the baseline everything else improves on.

**2. A hand-rolled `enum`.** You write `enum Symbols { static let gear = "gear" }`. Typed at the call site, but you maintain the list by hand. It covers what you remembered; it drifts behind Apple's releases; new symbols need manual entry. Moves the maintenance cost, doesn't remove it.

**3. [SFSafeSymbols](https://github.com/SFSafeSymbols/SFSafeSymbols).** A well-established, well-maintained package that gives you a generated enum of symbol names with availability annotations. It solves the core problem — no more raw strings — and it's a solid, popular choice. Credit where due: it's been doing this longer than most.

**4. [SFSymbolsKit](https://github.com/WikipediaBrown/SFSymbolsKit).** Also generated from Apple's full catalog, with a slightly different surface area: typed `String`, ready `UIImage`, and ready `NSImage` accessors plus a `CaseIterable` enum — the goal being one package that covers the name *and* the image on every Apple framework.

## What actually differs

The raw-string and hand-rolled options fail for reasons covered elsewhere on this blog. Between the two *generated* approaches (SFSafeSymbols and SFSymbolsKit), the honest differences are surface area and ergonomics, not "one is safe and one isn't" — both eliminate the stringly-typed failure mode:

<div class="code-card"><pre><span class="cm">// Hand-rolled enum — you maintain this list forever</span>
<span class="ty">Image</span>(systemName: <span class="ty">MySymbols</span>.gear)

<span class="cm">// SFSafeSymbols — generated, enum-based</span>
<span class="ty">Image</span>(systemSymbol: .gear)

<span class="cm">// SFSymbolsKit — generated; typed String + UIImage + NSImage</span>
<span class="ty">Image</span>(systemName: <span class="ty">String</span>.SFSymbols.gear)
<span class="kw">let</span> ui = <span class="ty">UIImage</span>.SFSymbols.gear
<span class="kw">let</span> ns = <span class="ty">NSImage</span>.SFSymbols.gear</pre></div>

How to choose:

- **You want the longest track record and a large community already using it:** SFSafeSymbols is a great, safe pick.
- **You want one dependency that hands you the typed name *and* a configured `UIImage`/`NSImage` across UIKit and AppKit, plus `CaseIterable` enumeration:** that's the surface SFSymbolsKit aims at.
- **You're tempted to hand-roll your own enum:** don't. Both generated packages exist precisely so you don't maintain a 7,000-entry list by hand. That's the option with the real long-term cost.

## The point that matters more than the comparison

Whichever generated package you pick, the win is the same and it's large: the symbol catalog becomes typed data in your program instead of opaque strings. Autocomplete works. Typos are compile errors. Refactors are safe. Enumeration is possible. The choice between SFSafeSymbols and SFSymbolsKit is real but secondary — the choice that actually costs you is *staying on raw strings or hand-maintained lists*.

## FAQ

**Can I migrate between typed packages later?** Yes — both replace raw strings with typed references, so moving from one to the other is mechanical (and far easier than the original raw-string mess). The hard, valuable migration is getting off raw strings in the first place; see [migrating off hardcoded SF Symbol strings]({{ '/blog/migrating-off-hardcoded-sf-symbol-strings/' | relative_url }}).

**Is a hand-rolled enum ever the right call?** For a toy app with five icons, sure. At any real scale, you're signing up to manually track Apple's catalog forever — the exact chore generated packages remove.

**Does adding a package for this bloat my app?** Generated symbol packages are static name data; there's no runtime engine. The footprint is negligible relative to the class of bugs removed.

---

This is the "which fix" question; the rest of the blog is the "why you need a fix at all" argument — [SwiftUI]({{ '/blog/sf-symbols-swiftui-type-safe/' | relative_url }}), [UIKit]({{ '/blog/sf-symbols-uikit-practical-guide/' | relative_url }}), [AppKit]({{ '/blog/sf-symbols-appkit-nsimage-guide/' | relative_url }}), and the full [tutorial]({{ '/tutorial/' | relative_url }}).
