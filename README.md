
# SFSymbols

# Now Supporting ***SFSymbols 5.1***

![example workflow](https://github.com/WikipediaBrown/SFSymbols/actions/workflows/Release.yml/badge.svg)

SFSymbols is a tiny ***Swift*** package that provides extensions to `String` and `UIImage` to make using **SFSymbols** easy peasy. The extensions and the accompanying `Enum` are all generated using the python scripts included in this package along with a list of all of the `SFSymbols` names. 


## Installation
**SFSymbols** can be installed with Swift Package Manager.
### Swift Package Manager (Xcode 15.3 or higher)

The preferred way of installing **SFSymbols** is via the [Swift Package Manager](https://swift.org/package-manager/).

1. In Xcode, open your project and navigate to **File** → **Swift Packages** → **Add Package Dependency...**
2. Paste the repository URL (`https://github.com/WikipediaBrown/SFSymbols.git`) and click **Next**.
3. For **Rules**, select **Version (Up to Next Major)** and click **Next**.
4. Click **Finish**.

[Adding Package Dependencies to Your App](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app)


## Usage

### String
You can use the `String` extension to get the name of all of the `SFSymbols` available. You can add an image like this
``` Swift
Image(systemName: .SFSymbols.plusApp)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```

### UIImage
You can use the `UIImage` extension to get the image of all of the `SFSymbols` available. You can add an image like this
``` Swift
Image(uiImage: .SFSymbols.plusApp)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```

### Enum
Additionally, there is an enum that is `CaseIterable` that provides access to all of the strings in the `String` extension and access to all of the images through an `image` property.
``` Swift
Image(uiImage: SFSymbol.plusApp.image)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```

or 

``` Swift
Image(systemName: SFSymbol.plusApp.string)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```


## Generation

The scripts used to generate the extensions and enum are written in `Python 2.7.18`. Which means you'll need Python. 

### Get Python
Assuming you're running macOS, you should first install [Homebrew](https://brew.sh) and then use Homebrew to install Python by running the command `brew install python`.

### Get List of Names
Get list of names of `SFSymbols` by opening the SFSymbols App (you can get it from [ Developer](https://developer.apple.com/sf-symbols/)) and paste it into the SFSymbols.txt file. Check out this [StackOverflow](https://stackoverflow.com/a/63310093/5863650) post.

### Run Python Scripts
Run the command `python3 UIImageExtension.py && python3 UIImageExtensionTests.py && python3 StringExtension.py && python3 StringExtensionTests.py && python3 Enum.py` and the python scripts will regenerate the extension and enum.


## Test

Run `command+u` in ***Xcode*** to run the unit tests. Test are run automatically for all pull requests. When running tests locally, be sure to be using `iOS 17.2` or later. Some symbols are not included in earlier builds.


## Versioning

SFSymbols releases a [new version on GitHub](https://github.com/WikipediaBrown/SFSymbols/releases) automatically when a pull request is approved from the `develop` branch to the `master` branch.


## Contribute

Send a pull request my dude... or create an issue.


## Author

Wikipedia Brown


## License

**SFSymbols** is available under the MIT license. See the LICENSE file for more info.

Made with 🌲🌲🌲 in Cascadia
