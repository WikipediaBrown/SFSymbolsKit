//
//  SFSymbol.swift
//  SFSymbols
//
//  Created by Wikipedia Brown on 5/15/24.
//

import XCTest
@testable import SFSymbolsKit

final class SFSymbolsEnumTests: XCTestCase {
#if canImport(UIKit)
    func test_SFSymbols_Enum_image_found() {
        SFSymbol.allCases.forEach {
            let image = $0.image
            XCTAssertNotEqual(image, UIImage(), "Image named \($0.string).")
        }
    }
    @available(iOS 13, *)
    func test_SFSymbols_Enum_string_found() {
        SFSymbol.allCases.forEach {
            let image = UIImage(systemName: $0.string)
            XCTAssertNotEqual(image, UIImage())
        }
    }
#endif
    
#if canImport(AppKit)
    func test_SFSymbols_Enum_image_found() {
        SFSymbol.allCases.forEach {
            let image = $0.image
            XCTAssertNotEqual(image, NSImage(), "Image named \($0.string).")
        }
    }
    @available(iOS 13, *)
    func test_SFSymbols_Enum_string_found() {
        SFSymbol.allCases.forEach {
            let image = NSImage(systemSymbolName: $0.string,
                                accessibilityDescription: "This is the symbole for\($0.string)")
            XCTAssertNotEqual(image, NSImage())
        }
    }
#endif

}
