---
title: "SF Symbols in UIKit: a practical guide"
description: "Using SF Symbols across UIKit — buttons, bar items, image views, configurations — and why every one of those call sites is a hand-typed string you have to keep correct forever."
date: 2026-05-08
tags: [uikit, sf-symbols, swift]
---

UIKit has more surface area for SF Symbols than SwiftUI, and every entry point shares the same weakness: it's keyed by a string.

<div class="code-card"><pre><span class="cm">// Image view</span>
imageView.image = <span class="ty">UIImage</span>(systemName: <span class="st">"photo"</span>)

<span class="cm">// Bar button item</span>
<span class="kw">let</span> item = <span class="ty">UIBarButtonItem</span>(
    image: <span class="ty">UIImage</span>(systemName: <span class="st">"square.and.pencil"</span>),
    style: .plain, target: self, action: #selector(compose)
)

<span class="cm">// Button configuration (iOS 15+)</span>
<span class="kw">var</span> config = <span class="ty">UIButton</span>.<span class="ty">Configuration</span>.plain()
config.image = <span class="ty">UIImage</span>(systemName: <span class="st">"trash"</span>)</pre></div>

Three call sites, three hand-typed strings, three independent chances to misspell something the compiler will never flag. Multiply across a real UIKit codebase and the count of "string I have to keep correct forever" runs into the hundreds.

## The maintenance math

Think about the lifecycle of one icon string:

1. A designer picks an icon. You find its name in the SF Symbols app, copy it, paste it.
2. Six months later someone refactors that view controller. The string survives the move — or gets mangled in a merge and nobody notices because it still *compiles*.
3. A year later the icon should change. Someone updates the string. They get the new name slightly wrong. It ships blank.
4. Apple deprecates or renames the symbol in a major release. Your string is now pointing at nothing on new OSes. Still compiles. Still ships.

At no point in that lifecycle did a tool tell you something was wrong. Every safeguard was "a human carefully reading a string." That's the maintenance liability — not any single typo, but that the *whole category* of error is invisible to your toolchain.

## Symbol configurations don't help

UIKit's `UIImage.SymbolConfiguration` lets you tune weight, scale, and color:

<div class="code-card"><pre><span class="kw">let</span> config = <span class="ty">UIImage</span>.<span class="ty">SymbolConfiguration</span>(pointSize: <span class="st">17</span>, weight: .semibold)
<span class="kw">let</span> image = <span class="ty">UIImage</span>(systemName: <span class="st">"bell.badge"</span>, withConfiguration: config)</pre></div>

That's a richer rendering API, but the *identity* of the symbol is still the string `"bell.badge"`. All the configuration power in the world doesn't help if the name is wrong — you get a perfectly weighted, perfectly scaled nothing.

## Typed symbols across UIKit

SFSymbolsKit gives UIKit the same treatment everywhere a symbol is referenced:

<div class="code-card"><pre><span class="kw">import</span> <span class="ty">SFSymbolsKit</span>

imageView.image = <span class="ty">UIImage</span>.SFSymbols.photo

<span class="kw">let</span> item = <span class="ty">UIBarButtonItem</span>(
    image: <span class="ty">UIImage</span>.SFSymbols.squareAndPencil,
    style: .plain, target: self, action: #selector(compose)
)

<span class="kw">var</span> config = <span class="ty">UIButton</span>.<span class="ty">Configuration</span>.plain()
config.image = <span class="ty">UIImage</span>.SFSymbols.trash</pre></div>

Need a configured variant? Compose the typed name with the configuration instead of hand-writing the string:

<div class="code-card"><pre><span class="kw">let</span> cfg = <span class="ty">UIImage</span>.<span class="ty">SymbolConfiguration</span>(pointSize: <span class="st">17</span>, weight: .semibold)
<span class="kw">let</span> image = <span class="ty">UIImage</span>(systemName: <span class="ty">String</span>.SFSymbols.bellBadge,
                      withConfiguration: cfg)</pre></div>

The configuration story is unchanged; the symbol identity is now a compiler-checked property. Refactors stay safe, autocomplete lists every option, and "blank icon in production because of a typo" stops being a category of bug you can ship.

## FAQ

**Does this work with `UIListContentConfiguration` / cell content configs?** Yes — anywhere you'd pass `UIImage(systemName:)` or a system image name string, you pass the typed property or `UIImage.SFSymbols.*` instead.

**Objective-C interop?** SFSymbolsKit is a Swift API. For mixed targets, use it from the Swift side; the resulting `UIImage` bridges to Objective-C normally.

**What about tvOS / watchOS / visionOS?** The `UIImage` extension is available wherever UIKit is, so the same typed accessors work across those platforms.

---

The UIKit story and the [SwiftUI story]({{ '/blog/sf-symbols-swiftui-type-safe/' | relative_url }}) are the same problem in different frameworks: a string where a type belongs. If you already have a codebase full of these strings, the [migration guide]({{ '/blog/migrating-off-hardcoded-sf-symbol-strings/' | relative_url }}) covers moving over without a big-bang rewrite.
