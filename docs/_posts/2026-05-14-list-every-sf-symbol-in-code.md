---
title: "How to list every SFSymbol in code (without hardcoding names)"
description: "Apple doesn't give you a way to enumerate SFSymbols in Swift — because they're strings, and you can't iterate a string you never wrote down. Here's how to get all of them as a CaseIterable enum."
date: 2026-05-14
tags: [sf-symbols, swift, swiftui]
---

A question that comes up constantly: *"How do I get a list of all SFSymbols in code?"* — to build a symbol picker, a debug grid, a design-system gallery, whatever.

The uncomfortable answer with Apple's APIs: **you can't.** There is no `SFSymbol.allCases`, no `UIImage.allSystemSymbols`, no public enumeration. SFSymbols are referenced by string, and you cannot iterate a set of strings that was never written down anywhere in your code. This is the same root problem as a misspelled symbol — just viewed from the other side.

## Why there's no built-in list

`Image(systemName:)` and `UIImage(systemName:)` take a `String`. The system resolves that string against a private catalog at runtime. Your code never holds the catalog — it holds individual string literals you typed. So "give me all symbols" has no answer at the language level, because the symbols aren't *data in your program*. They're an opaque lookup keyed by strings.

People work around this in bad ways:

<div class="code-card"><pre><span class="cm">// The "I'll just hardcode the ones I need" array</span>
<span class="kw">let</span> symbols = [<span class="st">"house"</span>, <span class="st">"gear"</span>, <span class="st">"bell"</span>, <span class="st">"star"</span>, <span class="st">"trash"</span>]
<span class="cm">// ...now maintained by hand, forever, and 0.07% of the catalog</span></pre></div>

That array is the maintenance liability in its purest form: a hand-typed subset of a 7,000-symbol catalog, guaranteed to be incomplete and to drift.

## The fix: a generated CaseIterable enum

SFSymbolsKit ships an `SFSymbol` enum that is `CaseIterable` — because the symbol catalog *is* data in the package (generated from `SFSymbols.txt`), it can be enumerated:

<div class="code-card"><pre><span class="kw">import</span> <span class="ty">SwiftUI</span>
<span class="kw">import</span> <span class="ty">SFSymbolsKit</span>

<span class="kw">struct</span> <span class="ty">SymbolGallery</span>: <span class="ty">View</span> {
    <span class="kw">let</span> columns = [<span class="ty">GridItem</span>(.adaptive(minimum: <span class="st">64</span>))]

    <span class="kw">var</span> body: <span class="kw">some</span> <span class="ty">View</span> {
        <span class="ty">ScrollView</span> {
            <span class="ty">LazyVGrid</span>(columns: columns) {
                <span class="ty">ForEach</span>(<span class="ty">SFSymbol</span>.allCases, id: \.self) { symbol <span class="kw">in</span>
                    <span class="ty">Image</span>(systemName: symbol.rawValue)
                        .font(.title)
                }
            }
        }
    }
}</pre></div>

Every symbol Apple ships, enumerable, in a few lines. Build a searchable picker:

<div class="code-card"><pre><span class="kw">struct</span> <span class="ty">SymbolPicker</span>: <span class="ty">View</span> {
    <span class="kw">@State private var</span> query = <span class="st">""</span>
    <span class="kw">@Binding var</span> selection: <span class="ty">SFSymbol</span>

    <span class="kw">var</span> filtered: [<span class="ty">SFSymbol</span>] {
        query.isEmpty
            ? <span class="ty">SFSymbol</span>.allCases
            : <span class="ty">SFSymbol</span>.allCases.filter { $0.rawValue.contains(query) }
    }

    <span class="kw">var</span> body: <span class="kw">some</span> <span class="ty">View</span> {
        <span class="ty">List</span>(filtered, id: \.self, selection: <span class="kw">$</span>selection) { symbol <span class="kw">in</span>
            <span class="ty">Label</span>(symbol.rawValue, systemImage: symbol.rawValue)
        }
        .searchable(text: <span class="kw">$</span>query)
    }
}</pre></div>

No hand-maintained array. No "I only added the 40 we use." The picker covers the entire catalog and stays current when the package regenerates against a new SFSymbols release.

## The deeper point

"There's no way to list SFSymbols" and "my symbol name was misspelled" are the same bug. Both exist because the catalog lives outside your program as opaque strings. Make the catalog *typed data in your program* and both problems disappear at once: you can enumerate it, and you can't misspell it.

## FAQ

**Can I get all symbols as plain strings?** Yes — `SFSymbol.allCases.map(\.rawValue)` gives you every name as a `String` array, fully populated, no manual list.

**Is iterating 7,000 symbols slow?** `allCases` is an array of enum cases; rendering is lazy via `LazyVGrid`/`List`. Filtering 7,000 short strings is trivial on-device.

**Will the list include symbols added in the latest iOS?** It includes whatever the package's generated catalog contains — bump the dependency after a new SFSymbols release and the new symbols are in `allCases` automatically. See [keeping up with new SFSymbols]({{ '/blog/keeping-up-with-new-sf-symbols/' | relative_url }}).

---

This is the enumeration angle on the same thesis the rest of the blog covers: strings can't be iterated, validated, or refactored. The [SwiftUI]({{ '/blog/sf-symbols-swiftui-type-safe/' | relative_url }}) and [tutorial]({{ '/tutorial/' | relative_url }}) pieces cover the day-to-day usage.
