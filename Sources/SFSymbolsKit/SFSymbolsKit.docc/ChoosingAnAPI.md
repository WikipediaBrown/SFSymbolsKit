# Choosing an API

SFSymbolsKit exposes the same catalog through four surfaces. Pick the one that matches the layer you're working at.

## Overview

### String — for any `systemName:` argument

Use when an Apple API wants a system-symbol name string. Drop-in; nothing else changes.

```swift
Image(systemName: String.SFSymbols.plusApp)
Label("Add", systemImage: String.SFSymbols.plus)
```

### UIImage — UIKit on iOS, iPadOS, tvOS, watchOS, visionOS

Use when you want a configured `UIImage` directly, skipping the failable `UIImage(systemName:)` round-trip.

```swift
button.setImage(UIImage.SFSymbols.squareAndPencil, for: .normal)
```

### NSImage — AppKit on macOS

Same ergonomics for macOS; the accessibility description is synthesised from the symbol name.

```swift
menuItem.image = NSImage.SFSymbols.gear
```

### SFSymbol enum — enumerate the whole catalog

`SFSymbol` is `CaseIterable`. Apple provides no built-in way to list symbols; this does.

```swift
List(SFSymbol.allCases, id: \.self) { symbol in
    Label(symbol.rawValue, systemImage: symbol.rawValue)
}
```

## See Also

- <doc:TypeSafeSymbols>
- <doc:/tutorials/SFSymbolsKit>
