![SFSymbolsKit](https://github.com/WikipediaBrown/SFSymbolsKit/blob/develop/assets/SFSymbolsKitBanner.png?raw=true "SFSymbolsKit Banner")

# SFSymbolsKit

# Now Supporting ***macOS***

![Release Workflow](https://github.com/WikipediaBrown/SFSymbolsKit/actions/workflows/Release.yml/badge.svg) 
[![Swift Versions](https://img.shields.io/endpoint?url=https%3A%2F%2Fswiftpackageindex.com%2Fapi%2Fpackages%2FWikipediaBrown%2FSFSymbolsKit%2Fbadge%3Ftype%3Dswift-versions)](https://swiftpackageindex.com/WikipediaBrown/SFSymbolsKit) 
[![Platforms Supported](https://img.shields.io/endpoint?url=https%3A%2F%2Fswiftpackageindex.com%2Fapi%2Fpackages%2FWikipediaBrown%2FSFSymbolsKit%2Fbadge%3Ftype%3Dplatforms)](https://swiftpackageindex.com/WikipediaBrown/SFSymbolsKit)

SFSymbolsKit is a tiny ***Swift*** package that provides extensions to `String`, `UIImage` and `NSImage` to make using **SFSymbols** easy peasy. The extensions and the accompanying `Enum` are all generated using the python scripts included in this package along with a list of all of the `SFSymbols` names. 

## 🛠️ Installation
**SFSymbolsKit** can be installed with Swift Package Manager.
### Swift Package Manager (Xcode 15.3 or higher)

The preferred way of installing **SFSymbolsKit** is via the [Swift Package Manager](https://swift.org/package-manager/).

1. In Xcode, open your project and navigate to **File** → **Swift Packages** → **Add Package Dependency...**
2. Paste the repository URL (`https://github.com/WikipediaBrown/SFSymbolsKit.git`) and click **Next**.
3. For **Rules**, select **Version (Up to Next Major)** and click **Next**.
4. Click **Finish**.

[Adding Package Dependencies to Your App](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app)


## 👩🏽‍💻 Usage

### 🧵 String
You can use the `String` extension to get the name of all of the `SFSymbols` available. You can add an image like this:
``` Swift
Image(systemName: String.SFSymbols.plusApp)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```

### 🩻 UIImage
You can use the `UIImage` extension to get the image of all of the `SFSymbols` available. You can add an image like this:
``` Swift
Image(uiImage: UIImage.SFSymbols.plusApp)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```

### 🗾 NSImage
Uou can use the `NSImage` estnsion to get the image of all of the `SFSymbols` available. You can add an image like this:
``` Swift
Image(nsImage: NSImage.SFSymbols.plusApp)
    .resizable()
    .scaledToFit()
    .aspectRatio(contentMode: .fit)
    .foregroundColor(.primary)
```

### 📋 Enum
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
Image(nsImage: SFSymbol.plusApp.image)
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

## 🧬 Generation

The scripts used to generate the extensions and enum are written in `Python 2.7.18`. Which means you'll need Python. 

### 🐍 Get Python
Assuming you're running macOS, you should first install [`Homebrew`](https://brew.sh) and then use Homebrew to install Python by running the command `brew install python`.

### 📋 Get List of Names
Get list of names of `SFSymbols` by opening the SFSymbols App (you can get it from [ Developer](https://developer.apple.com/sf-symbols/)) and paste it into the SFSymbols.txt file. Check out this [StackOverflow](https://stackoverflow.com/a/63310093/5863650) post.

### 🏃🏽‍♀️ Run Python Scripts
Run the command `bash generateSymbols.sh`. This command runs a bash script that in turn runs the command `brew install python` and then the command `python3 UIImageExtension.py && python3 UIImageExtensionTests.py && python3 StringExtension.py && python3 StringExtensionTests.py && python3 Enum.py`. This runs the python scripts will regenerate the `String` and `UIImage` extensions and enum.

## 🧪 Test

Run `command+u` in ***Xcode*** to run the unit tests. Test are run automatically for all pull requests. When running tests locally, be sure to be using `iOS 17.2` or later or `macOS 14.5` or later. Some symbols are not included in earlier versions. Releases of `SFSymbolsKit` support ***SFSymbols 5.1***.

### 🏎️ Fastlane Scan

You can also run tests on both `iOS` & `macOS` using [`fastlane`](https://fastlane.tools). This requires installing `fastlane` which in turn requires installing [`Homebrew`](https://brew.sh). With `Homebrew` and `fastlane` installed you can open a terminal and navigate to the `SFSymbolsKit`'s root folder and run the command `fastlane unit_test`. This will run the unit tests for both `iOS` & `macOS` in succession. You should expect to see 100% code coverage for both test runs.

## 🐁 Versioning

SFSymbolsKit releases a [new version on GitHub](https://github.com/WikipediaBrown/SFSymbolsKit/releases) automatically when a pull request is approved from the `develop` branch to the `master` branch.

## 👩🏽‍💻 Contribute

Send a pull request my dude... or create an issue.

## ✍🏽 Authors

Wikipedia Brown, Adrianna

## 🪪 Licence

**SFSymbolsKit** is available under the MIT license. See the LICENSE file for more info.

<p align="center">Made with 🌲🌲🌲 in Cascadia</p>