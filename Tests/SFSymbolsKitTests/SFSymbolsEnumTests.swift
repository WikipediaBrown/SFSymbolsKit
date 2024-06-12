//
//  SFSymbol.swift
//  SFSymbols
//
//  Created by Wikipedia Brown on 5/15/24.
//

import XCTest
@testable import SFSymbolsKit

final class SFSymbolsEnumTests: XCTestCase {
    func test_SFSymbols_Enum_image_found() {
        SFSymbol.allCases.forEach {
            let image = $0.image
            XCTAssertNotEqual(image, UIImage(), "Image named \($0.string).")
        }
    }
    func test_SFSymbols_Enum_string_found() {
        SFSymbol.allCases.forEach {
            let image = UIImage(systemName: $0.string)
            XCTAssertNotEqual(image, UIImage())
        }
    }
}
