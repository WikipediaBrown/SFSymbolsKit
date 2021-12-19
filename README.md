# SFSymbols

SFSymbols is a tiny package that provides extensions to `String` and `UIImage` to make using ~~SFSymbols~~ easy peasy. The extensions and the accompanying `Enum` are all generated using the python scripts included in this package along with a list of all of the `SFSymbols` names. 

# Usage

## String
You can use the `String` extension to get the name of all of the `SFSymbols` available. You can add an image like this
```
Image(systemName: .plusApp)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```

## UIImage
You can use the `UIImage` extension to get the image of all of the `SFSymbols` available. You can add an image like this
```
Image(uiImage: .plusApp)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```