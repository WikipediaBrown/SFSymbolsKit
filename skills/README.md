# skills/

OpenClaw skills published from this repo.

> **Not part of the Swift package.** Like `mcp/`, this is a top-level
> directory outside `Sources/`, so Swift Package Manager never
> compiles or ships it. Source only — nothing here is auto-published.

## `sfsymbolskit/`

An [OpenClaw](https://docs.openclaw.ai/tools/skills) skill that grounds
SFSymbol usage for AI agents: it makes the agent resolve every symbol
against the bundled manifest (`symbols.json`, generated from
`Enum.swift` — the same single source of truth as
<https://sfsymbolskit.com/symbols.json> and the `mcp/` server) instead
of emitting hallucinated stringly-typed `systemName:` values.

`symbols.json` is regenerated automatically by `generateSymbols.sh`
(via `generateManifests.py`) whenever the catalog is regenerated, so
it can't drift from the package.

### Publishing to ClawHub (manual)

Publishing to the [ClawHub](https://github.com/openclaw/clawhub)
registry is a deliberate, authenticated step — run it yourself:

```sh
clawhub skill publish skills/sfsymbolskit
# or: clawhub sync   (scans + publishes new/updated local skills)
```

Then it's installable by OpenClaw agents and discoverable in the
registry (and listable in awesome-openclaw-skills).
