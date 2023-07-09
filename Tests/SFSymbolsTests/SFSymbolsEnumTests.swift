import XCTest
@testable import SFSymbols

final class SFSymbolsEnumTests: XCTestCase {
    func test_SFSymbols_Enum_image_found() {
        SFSymbol.allCases.forEach {
            let image = $0.image
            XCTAssertNotEqual(image, UIImage())
        }
    }
    func test_SFSymbols_Enum_string_found() {
        SFSymbol.allCases.forEach {
            let image = UIImage(systemName: $0.string)
            XCTAssertNotEqual(image, UIImage())
        }
    }
}
