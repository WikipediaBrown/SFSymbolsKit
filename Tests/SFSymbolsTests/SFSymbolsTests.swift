import XCTest
@testable import SFSymbols

final class SFSymbolsTests: XCTestCase {
    func testExample() throws {
        for symbol in SFSymbols.allCases {
            XCTAssertTrue(symbol.image is UIImage, <#T##message: String##String#>)
            
            
            
        }
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct
        // results.
//        XCTAssertEqual(SFSymbols.text, "Hello, World!")
    }
}
