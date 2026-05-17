---
title: "Migrating off hardcoded SFSymbol strings"
description: "A practical, incremental strategy for replacing hand-typed SFSymbol name strings with typed properties across an existing codebase — without a risky big-bang refactor."
date: 2026-05-05
tags: [refactoring, sf-symbols, swift]
image:
  path: /assets/og/migrating-off-hardcoded-sf-symbol-strings.png
  width: 1200
  height: 630
  alt: "Migrating off hardcoded SFSymbol strings — SFSymbolsKit"
---

If your app already has hundreds of `systemName:` strings scattered across it, you don't have a typo problem — you have a *maintenance* problem. Every one of those strings is a small unverified assertion ("this is a real symbol name") that no tool is checking. Migration is about converting those assertions into compiler-checked facts, incrementally, without freezing feature work.

## Step 1: find the surface area

First, see how big the problem actually is:

<div class="code-card"><pre><span class="cm"># Every SwiftUI + UIKit + AppKit symbol call site</span>
grep -rEn 'systemName:|systemSymbolName:' --include=<span class="st">"*.swift"</span> Sources/ | wc -l</pre></div>

That number is your "strings I am currently responsible for keeping correct by hand." It usually surprises people. Keep the full list — it's your migration checklist.

## Step 2: add SFSymbolsKit, change nothing else yet

Add the package. It introduces zero behavior change on its own:

<div class="code-card"><pre><span class="kw">dependencies</span>: [
    .package(url: <span class="st">"https://github.com/WikipediaBrown/SFSymbolsKit.git"</span>,
             from: <span class="st">"<span class="latest-version" data-fallback="0.1.26">0.1.26</span>"</span>)
]</pre></div>

Now you can migrate one call site at a time. Nothing forces a big-bang rewrite.

## Step 3: convert leaf-first, not all at once

Start with the smallest, most-used components — the design-system layer, shared cells, the tab bar. Replace the string with the typed property:

<div class="code-card"><pre><span class="cm">// Before</span>
<span class="ty">Image</span>(systemName: <span class="st">"chevron.right"</span>)

<span class="cm">// After</span>
<span class="ty">Image</span>(systemName: <span class="ty">String</span>.SFSymbols.chevronRight)</pre></div>

Each converted call site is permanently safe from that point on: it can't be mistyped in a future edit, and find-all-usages now actually finds it. You're not just fixing today's typos — you're removing the ability to introduce tomorrow's.

## Step 4: make new code typed by default

The migration only stays done if new strings stop appearing. A lightweight guard in CI keeps the regression count at zero:

<div class="code-card"><pre><span class="cm"># Fail CI if a raw system-symbol string is introduced</span>
<span class="kw">if</span> grep -rEn 'systemName: ?<span class="st">"</span>' --include=<span class="st">"*.swift"</span> Sources/; <span class="kw">then</span>
  <span class="kw">echo</span> <span class="st">"Use String.SFSymbols.* instead of a raw symbol string"</span>
  <span class="kw">exit</span> <span class="st">1</span>
<span class="kw">fi</span></pre></div>

Tighten the pattern to taste (allow-list legacy files during the transition). The point is to ratchet: every merged PR leaves the codebase with fewer hand-typed symbol strings, never more.

## Step 5: delete your hand-rolled constants file

If you previously built a `Symbols` enum to paper over this, it's now redundant. SFSymbolsKit is the same idea — generated from Apple's full catalog and kept current by regeneration, so it doesn't drift the way a hand-maintained file does. Delete yours, repoint usages, and stop maintaining a list by hand.

## Why incremental beats big-bang

A find-and-replace-everything PR touching 400 call sites is unreviewable, conflicts with everything in flight, and risks introducing the exact errors you're trying to eliminate. Leaf-first migration with a CI ratchet converts the codebase steadily, keeps every PR reviewable, and means the maintenance liability shrinks monotonically instead of in one scary jump.

## FAQ

**How long does this take for a large app?** It's not a project — it's a policy. Convert high-traffic components in an afternoon, add the CI guard, and let normal feature work carry the rest over weeks. There's no deadline because every step is independently safe.

**What if a designer wants a symbol that didn't exist when we adopted it?** SFSymbolsKit is generated from Apple's catalog; regenerating picks up new symbols. You're never blocked waiting for someone to hand-add a constant.

**Does the CI guard create false positives?** Only where you genuinely still have raw strings — which is the point. Allow-list during transition, then remove the allow-list once a directory is clean.

---

This is the cleanup path; the [SwiftUI]({{ '/blog/sf-symbols-swiftui-type-safe/' | relative_url }}) and [UIKit]({{ '/blog/sf-symbols-uikit-practical-guide/' | relative_url }}) posts cover the day-to-day usage once you're migrated. Staying current with Apple's releases is its own topic: [keeping up with new SFSymbols]({{ '/blog/keeping-up-with-new-sf-symbols/' | relative_url }}).
