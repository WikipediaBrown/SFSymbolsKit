# ``SFSymbolsKit``

Apple's entire SFSymbols catalog as a strongly-typed Swift API — autocompleted, refactor-safe, and compile-checked.

## Overview

Apple ships SFSymbols, but the APIs that consume them — SwiftUI's `Image(systemName:)`, UIKit's `UIImage(systemName:)`, and AppKit's `NSImage(systemSymbolName:accessibilityDescription:)` — all take a `String`. The compiler can't tell a real symbol name from a typo, so a mistake isn't a build error: it's a blank icon discovered at runtime.

SFSymbolsKit replaces those hand-typed strings with a typed Swift property for every symbol Apple ships. It's generated deterministically from Apple's catalog, ships with zero dependencies, and works on iOS, iPadOS, macOS, watchOS, tvOS, visionOS, and CarPlay.

```swift
import SFSymbolsKit

// Stringly-typed: compiles, ships blank
Image(systemName: "squer.and.arrow.up")

// SFSymbolsKit: autocompleted, compile-checked
Image(systemName: String.SFSymbols.squareAndArrowUp)
```

## Topics

### Essentials

- <doc:TypeSafeSymbols>
- <doc:ChoosingAnAPI>

### For AI Coding Agents

- <doc:ForAIAgents>

### Tutorials

- <doc:/tutorials/SFSymbolsKit>

### Reference

- ``Swift/String/SFSymbols``
