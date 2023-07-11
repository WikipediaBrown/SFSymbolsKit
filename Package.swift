// swift-tools-version:5.9
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "SFSymbols",
    platforms: [
        .iOS(.v15),
        .macOS(.v10_15)
    ],
    products: [
        // Products define the executables and libraries a package produces, and make them visible to other packages.
        .library(name: "SFSymbols", targets: ["SFSymbols"]),
//        .library(name: "SFSymbols", type: .static, targets: ["SFSymbols"]),
//        .library(name: "SFSymbols", type: .dynamic, targets: ["SFSymbols"]),
    ],
    targets: [
        .target( name: "SFSymbols", dependencies: []),
        .testTarget( name: "SFSymbolsTests", dependencies: ["SFSymbols"]),
    ]
)
