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
        .library(name: "SFSymbols", targets: ["SFSymbols"])
    ],
    targets: [
        .target( name: "SFSymbols", dependencies: []),
        .testTarget( name: "SFSymbolsTests", dependencies: ["SFSymbols"]),
    ]
)
