
# SFSymbols

SFSymbols is a tiny package that provides extensions to `String` and `UIImage` to make using **SFSymbols** easy peasy. The extensions and the accompanying `Enum` are all generated using the python scripts included in this package along with a list of all of the `SFSymbols` names. 


## Installation
**SFSymbols** can be installed with Swift Package Manager.
### Swift Package Manager (Xcode 12 or higher)

The preferred way of installing **SFSymbols** is via the [Swift Package Manager](https://swift.org/package-manager/).

1. In Xcode, open your project and navigate to **File** → **Swift Packages** → **Add Package Dependency...**
2. Paste the repository URL (`https://github.com/WikipediaBrown/SFSymbols.git`) and click **Next**.
3. For **Rules**, select **Version (Up to Next Major)** and click **Next**.
4. Click **Finish**.

[Adding Package Dependencies to Your App](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app)


## Usage

### String
You can use the `String` extension to get the name of all of the `SFSymbols` available. You can add an image like this
```
Image(systemName: .plusApp)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```

### UIImage
You can use the `UIImage` extension to get the image of all of the `SFSymbols` available. You can add an image like this
```
Image(uiImage: .plusApp)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```

### Enum
Additionally, there is an enum that is `CaseIterable` that provides access to all of the strings in the `String` extension and access to all of the images through an `image` property.
```
Image(uiImage: SFSymbols.plusApp.image)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```

or 

```
Image(systemName: SFSymbols.plusApp.rawValue)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```


## Generation

### Get List of Names
Get list of names of `SFSymbols` by opening the SFSymbols App (you can get it from Apple.com) and paste it into the SFSymbols.txt file. Check out this [StackOverflow](https://stackoverflow.com/a/63310093/5863650) post.

### Run Python Scripts
Run the command `python UIImageExtension.py && python StringExtension.py && python Enum.py` and the python scripts will regenerate the extension and enum.


## Test

Run `command+u` to run the unit tests.


## Contribute

Send a pull request my dude.

## Author

Wikipedia Brown


## License

**SFSymbols** is available under the MIT license. See the LICENSE file for more info.