# Why Type-Safe Symbols

The case for replacing stringly-typed SFSymbol names with compiler-checked properties.

## Overview

Every SFSymbol reference in an Apple-platform app passes through a `String`:

```swift
Image(systemName: "square.and.arrow.up")
let icon = UIImage(systemName: "gear")
```

That string is never validated by the compiler. Three consequences follow, and all of them are maintenance costs that compound over the life of a codebase.

### No autocomplete

Xcode can't suggest symbol names, because they aren't part of your program — they're opaque keys resolved at runtime. You context-switch to the SFSymbols app, search, copy, paste.

### No compile-time check

`"gear"` (valid) and `"gears"` (not a symbol) are both just `String`. The type system has nothing to verify against, so a typo is not a build error.

### Silent runtime failure

`UIImage(systemName:)` returns `nil` for an unknown name; `Image(systemName:)` renders nothing. Neither throws. The bug ships, and the only signal is "the button looks wrong."

## The fix

SFSymbolsKit makes the catalog *data in your program*: a typed property per symbol, generated from Apple's list. Autocomplete works, typos are compile errors, refactors are safe, and the whole catalog becomes enumerable.

```swift
Image(systemName: String.SFSymbols.squareAndArrowUp)   // can't be misspelled
```

## See Also

- <doc:ChoosingAnAPI>
- <doc:ForAIAgents>
