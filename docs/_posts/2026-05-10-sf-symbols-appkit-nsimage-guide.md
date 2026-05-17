---
title: "SFSymbols in AppKit (NSImage): a practical guide"
description: "macOS apps reference SFSymbols through NSImage(systemSymbolName:accessibilityDescription:) — another string-keyed API with the same maintenance problem as its iOS counterparts."
date: 2026-05-10
tags: [appkit, macos, sf-symbols, swift]
image:
  path: /assets/og/sf-symbols-appkit-nsimage-guide.png
  width: 1200
  height: 630
  alt: "SFSymbols in AppKit (NSImage): a practical guide — SFSymbolsKit"
---

SFSymbols aren't just an iOS thing. macOS has had them since Big Sur, and AppKit's entry point carries the same design — and the same liability — as the UIKit one:

<div class="code-card"><pre><span class="kw">let</span> image = <span class="ty">NSImage</span>(
    systemSymbolName: <span class="st">"externaldrive.badge.plus"</span>,
    accessibilityDescription: <span class="st">"Add drive"</span>
)</pre></div>

`systemSymbolName:` is a `String`. `NSImage(systemSymbolName:accessibilityDescription:)` is failable — it returns `NSImage?`, `nil` when the name doesn't resolve. Exactly like UIKit, the type system can't tell a real symbol name from a typo, so the failure is invisible until runtime, on macOS, where blank toolbar items are especially easy to miss.

## AppKit makes the maintenance problem slightly worse

Two AppKit-specific wrinkles compound the stringly-typed cost:

**1. The accessibility description is mandatory and also hand-written.** Every call site has *two* hand-authored strings — the symbol name and the a11y label. Miss the symbol name and you get a blank image; the a11y string is fine but pointing at nothing.

**2. macOS UIs are toolbar- and menu-heavy.** Toolbars, menu items, status-bar items, outline view cells — macOS apps tend to have a high density of symbol references per screen. More call sites means more hand-typed strings means more surface area for the silent-typo failure.

<div class="code-card"><pre><span class="cm">// A typical macOS toolbar — every symbol a hand-typed string</span>
toolbarItem.image = <span class="ty">NSImage</span>(systemSymbolName: <span class="st">"sidebar.left"</span>, accessibilityDescription: <span class="st">"Toggle Sidebar"</span>)
addButton.image   = <span class="ty">NSImage</span>(systemSymbolName: <span class="st">"plus"</span>, accessibilityDescription: <span class="st">"Add"</span>)
trashButton.image = <span class="ty">NSImage</span>(systemSymbolName: <span class="st">"trash"</span>, accessibilityDescription: <span class="st">"Delete"</span>)</pre></div>

## Typed NSImage symbols

SFSymbolsKit's `NSImage` extension gives AppKit the same compile-checked accessors as UIKit, and synthesises a sensible accessibility description from the symbol name so you can't forget it:

<div class="code-card"><pre><span class="kw">import</span> <span class="ty">AppKit</span>
<span class="kw">import</span> <span class="ty">SFSymbolsKit</span>

toolbarItem.image = <span class="ty">NSImage</span>.SFSymbols.sidebarLeft
addButton.image   = <span class="ty">NSImage</span>.SFSymbols.plus
trashButton.image = <span class="ty">NSImage</span>.SFSymbols.trash</pre></div>

Need a specific accessibility label or symbol configuration? Compose the typed name instead of hand-writing the symbol string:

<div class="code-card"><pre><span class="kw">let</span> image = <span class="ty">NSImage</span>(
    systemSymbolName: <span class="ty">String</span>.SFSymbols.externaldriveBadgePlus,
    accessibilityDescription: <span class="st">"Add external drive"</span>
)</pre></div>

The symbol identity is now compiler-checked; the accessibility string stays under your control. Autocomplete lists every symbol, refactors are safe, and a misspelling is a build error rather than an empty toolbar button a Mac user quietly works around.

## FAQ

**Does this support `NSImage.SymbolConfiguration`?** Yes — apply configuration the same way you would today; pass `String.SFSymbols.<name>` as the name instead of a literal.

**Catalyst / cross-platform code?** In a shared file, the `UIImage` extension applies under UIKit and the `NSImage` extension under AppKit — the typed `String.SFSymbols.*` names work everywhere and let you branch by platform without duplicating raw strings.

**What about menu items and status items?** Anywhere AppKit takes a system symbol name string, the typed property substitutes directly — menus, status bar, outline/table cells included.

---

This completes the framework set: [SwiftUI]({{ '/blog/sf-symbols-swiftui-type-safe/' | relative_url }}), [UIKit]({{ '/blog/sf-symbols-uikit-practical-guide/' | relative_url }}), and now AppKit — one stringly-typed problem, three Apple frameworks, one typed fix. The [tutorial]({{ '/tutorial/' | relative_url }}) covers all three end to end.
