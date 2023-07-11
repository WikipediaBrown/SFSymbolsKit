import XCTest
@testable import SFSymbols

final class SFSymbolsEnumTests: XCTestCase {
    
    func test_SFSymbols_AppKit_Enum_image_found() {
        SFSymbol.allCases.forEach {
            let image = $0.image
#if canImport(AppKit)
            let comparitor = NSImage()
#elseif canImport(UIKit)
            let comparitor = UIImage()
#endif
            XCTAssertNotEqual(image, comparitor)
        }
    }
    
    func test_SFSymbols_AppKit_Enum_string_found() {
        SFSymbol.allCases.forEach {
#if canImport(AppKit)
            let image = NSImage(named: $0.string)
            let comparitor = NSImage()
#elseif canImport(UIKit)
            let image = UIImage(systemName: $0.string)
            let comparitor = UIImage()
#endif
            XCTAssertNotEqual(image, comparitor)
        }
    }
    
    func test_SFSymbols_UIKit_Enum_image_found() {
        SFSymbol.allCases.forEach {
            let image = $0.image
#if canImport(AppKit)
            let comparitor = NSImage()
#elseif canImport(UIKit)
            let comparitor = UIImage()
#endif
            XCTAssertNotEqual(image, comparitor)
        }
    }
    
    func test_SFSymbols_UIKit_Enum_string_found() {
        SFSymbol.allCases.forEach {
#if canImport(AppKit)
            let image = NSImage(named: $0.string)
            let comparitor = NSImage()
#elseif canImport(UIKit)
            let image = UIImage(systemName: $0.string)
            let comparitor = UIImage()
#endif
            XCTAssertNotEqual(image, comparitor)
        }
    }
}
