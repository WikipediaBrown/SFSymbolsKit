---
title: "Keeping up with new SFSymbols every iOS release"
description: "Apple adds hundreds of SFSymbols every OS cycle. If your symbol names are hand-typed strings, your codebase silently falls behind every September. Here's how to stay current automatically."
date: 2026-05-01
tags: [sf-symbols, swift, maintenance]
---

Every major OS release, Apple ships a new SFSymbols version with hundreds of new and revised glyphs. That's great for design — and a quiet, recurring tax on any codebase that references symbols as strings.

## The annual drift

Here's the maintenance cycle nobody puts on the roadmap:

1. **September:** Apple ships SFSymbols N with ~600 new symbols.
2. Your app can't *use* any of them by name until someone knows they exist and types the (correct) string.
3. If you keep a hand-rolled constants file, it now covers symbols N-1 and earlier. It's behind by a release the day the OS ships.
4. Some symbols get renamed or deprecated across versions. Your existing strings pointing at them still compile — and silently render wrong on new OSes.

None of this surfaces as a build error. The string interface means the toolchain has nothing to check against, so "we're a version behind" is invisible until a designer asks for a symbol you "don't have" (you do — it's just not in your hand-typed list).

## Why "just add the string" doesn't scale

The naive answer is "add the new symbol's string when you need it." That's fine for one symbol. It does not scale to an organization:

- Multiple developers each maintaining ad-hoc strings → inconsistency and duplication.
- No single source of truth for "what symbols can we use."
- The set of symbols you *could* use is always smaller than what Apple ships, bounded by what someone remembered to add.

You're rate-limited on Apple's icon catalog by your team's manual data entry. That's a strange place to have a bottleneck.

## Generation, not transcription

SFSymbolsKit takes a different stance: the Swift API is *generated* from `SFSymbols.txt` — the canonical list of every symbol name — by a script, not transcribed by a human:

<div class="code-card"><pre><span class="cm"># When Apple ships a new SFSymbols version:</span>
<span class="cm"># 1. Update SFSymbols.txt with the new catalog</span>
<span class="cm"># 2. Regenerate the Swift sources</span>
<span class="cm"># 3. Every new symbol is now a typed property — all of them, at once</span></pre></div>

A human transcribing 7,000+ names would introduce typos in dozens. A generator introduces zero. And catching up to a new release is one regeneration, not an open-ended backlog of "add the symbols people ask for."

For consumers, staying current is just a version bump:

<div class="code-card"><pre><span class="kw">dependencies</span>: [
    .package(url: <span class="st">"https://github.com/WikipediaBrown/SFSymbolsKit.git"</span>,
             from: <span class="st">"<span class="latest-version" data-fallback="0.1.26">0.1.26</span>"</span>)
]</pre></div>

Update the dependency after a new SFSymbols release and the entire new catalog is available as autocompleted, compile-checked properties. No transcription, no drift, no "we don't have that icon yet."

## The compounding argument

Each individual typo from a hand-typed string is small. The reason stringly-typed symbols are a *maintenance liability* and not just an occasional annoyance is that the cost compounds: it recurs every release, scales with team size, and is invisible to your tooling the entire time. Generation collapses all of that to a dependency bump.

## FAQ

**How quickly does SFSymbolsKit pick up a new SFSymbols release?** As fast as the catalog is regenerated and tagged. Because it's generated, there's no per-symbol manual work gating the update — and contributions are welcome on [GitHub](https://github.com/WikipediaBrown/SFSymbolsKit).

**Do renamed/deprecated symbols break my build?** A regenerated catalog reflects Apple's current names. You find out about a removed symbol at compile time (the property is gone) instead of at runtime (a blank icon) — which is exactly the safety the string interface denies you.

**Is pinning to a version safe?** Yes — pin like any dependency. The point is that *catching up* is a deliberate, one-line, all-at-once action instead of an unbounded manual chore.

---

Staying current is the long-term half of the story; the day-to-day half is in the [SwiftUI]({{ '/blog/sf-symbols-swiftui-type-safe/' | relative_url }}) and [UIKit]({{ '/blog/sf-symbols-uikit-practical-guide/' | relative_url }}) guides, and the full walkthrough lives in the [tutorial]({{ '/tutorial/' | relative_url }}).
