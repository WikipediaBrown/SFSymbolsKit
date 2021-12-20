import XCTest
@testable import SFSymbols

final class SFSymbolsTests: XCTestCase {
    func test_SFSymbols_Enum_image_found() {
        for symbol in SFSymbols.allCases {
            XCTAssertNotEqual(symbol.image, UIImage(), "SFSymbols Image not found.")
        }
    }
}
