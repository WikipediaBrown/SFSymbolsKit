# SFSymbols

[![](https://img.shields.io/endpoint?url=https%3A%2F%2Fswiftpackageindex.com%2Fapi%2Fpackages%2FWikipediaBrown%2FSFSymbols%2Fbadge%3Ftype%3Dswift-versions)](https://swiftpackageindex.com/WikipediaBrown/SFSymbols)

[![](https://img.shields.io/endpoint?url=https%3A%2F%2Fswiftpackageindex.com%2Fapi%2Fpackages%2FWikipediaBrown%2FSFSymbols%2Fbadge%3Ftype%3Dplatforms)](https://swiftpackageindex.com/WikipediaBrown/SFSymbols)


## :cloud: Overview
SFSymbols is a tiny package that provides extensions to `String` and `UIImage` to make using **SFSymbols** easy peasy. The extensions and the accompanying `Enum` are all generated using the python scripts included in this package along with a list of all of the `SFSymbols` names. 


## :hammer::wrench: Installation
**SFSymbols** can be installed with Swift Package Manager.
### Swift Package Manager (Xcode 12 or higher)

The preferred way of installing **SFSymbols** is via the [Swift Package Manager](https://swift.org/package-manager/).

1. In Xcode, open your project and navigate to **File** → **Swift Packages** → **Add Package Dependency...**
2. Paste the repository URL (`https://github.com/WikipediaBrown/SFSymbols.git`) and click **Next**.
3. For **Rules**, select **Version (Up to Next Major)** and click **Next**.
4. Click **Finish**.

[Adding Package Dependencies to Your App](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app)


## :book: Getting Started

### :thread: String
You can use the `String` extension to get the name of all of the `SFSymbols` available. You can add an image like this
```
Image(systemName: .SFSymbols.plusApp)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```

### :framed_picture: UIImage
You can use the `UIImage` extension to get the image of all of the `SFSymbols` available. You can add an image like this
```
Image(uiImage: .SFSymbols.plusApp)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```

### :file_cabinet: Enum
Additionally, there is an enum that is `CaseIterable` that provides access to all of the strings in the `String` extension and access to all of the images through an `image` property.
```
Image(uiImage: SFSymbol.plusApp.image)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```

or 

```
Image(systemName: SFSymbol.plusApp.string)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```


## :herb: Generation

The scripts used to generate the extensions and enum are written in `Python 2.7.18`. Which means you'll need Python. 

### :snake: Get Python
Assuming you're running macOS, you should first install [Homebrew](https://brew.sh) and then use Homebrew to install Python by running the command `brew install python`.

### :clipboard: Get List of Names
Get list of names of `SFSymbols` by opening the SFSymbols App (you can get it from Apple.com) and paste it into the SFSymbols.txt file. Check out this [StackOverflow](https://stackoverflow.com/a/63310093/5863650) post.

### :runner: Run Python Scripts
Run the command `python UIImageExtension.py && python UIImageExtensionTests.py && python StringExtension.py && python StringExtensionTests.py && python Enum.py` and the python scripts will regenerate the extension and enum.


## :microscope: Test

Run `command+u` to run the unit tests. Test are run automatically for all pull requests.


## :1234: Versioning

SFSymbols releases a [new version on GitHub](https://github.com/WikipediaBrown/SFSymbols/releases) automatically when a pull request is approved from the `develop` branch to the `master` branch.


## Contribute

Send a pull request my dude.


## Author

Wikipedia Brown


## License

**SFSymbols** is available under the MIT license. See the LICENSE file for more info.

Made with :evergreen_tree::evergreen_tree::evergreen_tree:🌲🌲🌲 in Cascadia
