from datetime import date

numbers = {
  "case": "caseImage",
  "repeat": "repeatImage",
  "return": "returnImage",
  "0": "zero",
  "1": "one",
  "2": "two",
  "3": "three",
  "4": "four",
  "5": "five",
  "6": "six",
  "7": "seven",
  "8": "eight",
  "9": "nine"
}

file = open("../Tests/SFSymbolsTests/NSImageExtensionTests.swift", "w")

file.write("//\n")
file.write("//  NSImageExtensionTests.swift\n")
file.write("//  SFSymbols\n")
file.write("//\n")
file.write("//  Generated by NSImageExtensionTests.py on ")
file.write(date.today().strftime('%m/%d/%y'))
file.write(".\n")
file.write("//\n")
file.write("\n")
file.write("#if canImport(AppKit)\n")
file.write("import XCTest\n")
file.write("@testable import SFSymbols\n")
file.write("\n")
file.write("final class NSImageExtensionTests: XCTestCase {\n\n")

with open('SFSymbols.txt') as topo_file:
    for line in topo_file:
        parts = line.split('.')
        camelCaseName = ""
        
        for part in parts:
            if part == parts[0]:
            
                if part.rstrip() in numbers:
                    camelCaseName += numbers[part.rstrip()]
                    continue
                elif part[0] in numbers:
                    camelCaseName += numbers[part[0]] + part[1:]
                    continue
                camelCaseName += part
                continue
            camelCaseName += part.capitalize()

        result = "    func test_StringExtension_{}_returnsImage() ".format(camelCaseName.rstrip())
        file.write(result)
        file.write("{\n")

        file.write("        // Arrange & Act\n")
        arrange = "        let image = NSImage.SFSymbols.{}\n".format(camelCaseName.rstrip())
        file.write(arrange)
        file.write("        // Assert\n")
        file.write("        XCTAssertNotEqual(image, NSImage())\n")
        file.write("    }\n\n")
file.write("}\n")
file.write("#endif\n")
file.close()
