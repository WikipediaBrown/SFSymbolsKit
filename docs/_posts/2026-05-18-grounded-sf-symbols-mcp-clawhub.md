---
title: "Grounded SFSymbols for AI agents: an MCP server and a ClawHub skill"
description: "Stringly-typed SFSymbols make AI agents hallucinate icon names that compile and ship blank. SFSymbolsKit now ships the fix as agent infrastructure — an MCP server and an installable ClawHub skill that ground every symbol against the real catalog."
date: 2026-05-18
tags: [ai, mcp, sf-symbols, swift, agents]
image:
  path: /assets/og/grounded-sf-symbols-mcp-clawhub.png
  width: 1200
  height: 630
  alt: "Grounded SFSymbols for AI agents: an MCP server and a ClawHub skill — SFSymbolsKit"
---

We've <a href="{{ '/blog/sf-symbols-ai-coding-agents/' | relative_url }}">argued before</a> that stringly-typed SFSymbols are uniquely hostile to AI coding agents: `Image(systemName: "trash.bin")` compiles, ships a blank icon, and the toolchain never says a word — so the one error class an agent can't self-correct is the one it produces most confidently.

That post diagnosed the problem. This one is about the fix shipping as **infrastructure agents can actually consume**: a Model Context Protocol server and an installable ClawHub skill. The typed Swift package was always the durable answer; these put the real catalog *in front of the model at generation time* instead of hoping it remembers 7,007 irregular names.

## Two ways to ground an agent

There are two distinct moments to stop a hallucinated symbol, and we now cover both.

**1. At generation — the MCP server.** A tool-using agent (Claude, Cursor, anything speaking MCP) connects to the server and calls real tools instead of guessing:

<div class="code-card"><pre><span class="cm">// agent asks for an upload icon — and gets the verified name</span>
search_sf_symbols(<span class="st">"upload share"</span>)   <span class="cm">// → square.and.arrow.up (+ typed accessor)</span>
resolve_sf_symbol(<span class="st">"trash.bin"</span>)      <span class="cm">// → not found; nearest: trash</span>
sf_symbol_usage(<span class="st">"trash"</span>)            <span class="cm">// → String.SFSymbols.trash, UIImage form, …</span></pre></div>

`resolve_sf_symbol` is the important one: it lets the agent *check its own guess* before writing it — converting a silent production bug into a tool result it can act on, the same way a compiler error closes the loop for ordinary Swift.

**2. At authoring — the ClawHub skill.** Not every agent surface runs MCP. The skill (`sfsymbolskit`, live on [ClawHub](https://clawhub.ai)) is a one-line install that teaches the agent the rule directly:

<div class="code-card"><pre>clawhub install sfsymbolskit</pre></div>

It bundles the full catalog and instructs the agent to resolve every symbol against it, never emit a guessed `systemName:` string, and prefer the typed accessor (`String.SFSymbols.…`) so a wrong name fails at compile time rather than in your UI.

## The part that matters six months from now

The easy version of this is a static list someone hand-exports once and forgets. SFSymbols ship new names every OS release; a stale grounding source is just a slower hallucination.

So all three surfaces are generated from one place. `Sources/SFSymbolsKit/Enum.swift` is the catalog; a single generator (`generateManifests.py`, run by `generateSymbols.sh`) re-derives **every** consumer manifest from it:

<div class="code-card"><pre>Enum.swift  ──►  generateManifests.py  ──►  docs/symbols.json   <span class="cm">(site + browser)</span>
                                       ──►  mcp/symbols.json    <span class="cm">(MCP server)</span>
                                       ──►  skills/…/symbols.json <span class="cm">(ClawHub skill)</span></pre></div>

There is no second source of truth to drift. When Apple ships SFSymbols 7.3, the same regeneration that updates the typed Swift API updates what every agent sees — site, MCP, and skill — in one run. That's the whole point of the project applied to its own tooling: the catalog is generated, never hand-maintained, [end to end](https://github.com/WikipediaBrown/SFSymbolsKit).

## If you ship Swift that agents touch

You don't have to choose a surface. Use the [typed Swift package]({{ '/#install' | relative_url }}) so hallucinations become build errors; add the MCP server so they never get generated; install the skill on agent surfaces that don't speak MCP. They reinforce each other — the package makes a bad guess *loud*, the MCP/skill layer makes a bad guess *unlikely*.

Machine-readable summaries also live at <a href="https://sfsymbolskit.com/llms.txt">/llms.txt</a> and <a href="https://sfsymbolskit.com/llms-full.txt">/llms-full.txt</a>, and both point assistants at the generated <a href="https://sfsymbolskit.com/symbols.json">symbols.json</a> manifest for grounding — so even an assistant with no integration at all is steered to the typed API and the real catalog.

## FAQ

**Do I need both the MCP server and the skill?** No — they target different agent surfaces. MCP if your agent supports tools (best: it can verify before writing). The ClawHub skill for agent surfaces that don't. Both are optional on top of the typed Swift package, which is the actual compile-time guarantee.

**Is the MCP server in the Swift package?** No, deliberately. It lives in `mcp/`, outside the SwiftPM target paths, so adding the package never pulls a Node server into your app. Same for the skill in `skills/`.

**Will the agent's grounding go stale after the next iOS release?** No. The MCP and skill manifests are regenerated from the same `Enum.swift` as the typed API, in the same `generateSymbols.sh` run — there's no separately maintained list to fall behind.

**Is it production-ready?** The Swift package is MIT, zero-dependency, generated from Apple's full catalog. The skill is published and installable today; the MCP server's source ships in the repo. See the <a href="{{ '/tutorial/' | relative_url }}">tutorial</a>.

---

This is the same through-line as the rest of the blog — <a href="{{ '/blog/typed-vs-stringly-typed-sf-symbols/' | relative_url }}">stringly-typed SFSymbols are a maintenance liability</a> — extended to the surfaces writing most of the world's Swift now. Start with <a href="{{ '/blog/sf-symbols-ai-coding-agents/' | relative_url }}">why agents hallucinate icon names</a>, then ground them with the tools above.
