
from datetime import datetime

# Get the current local date
current_date = datetime.now()

# Format the date as a string in the desired format
formatted_date = current_date.strftime('%-m/%-d/%Y')

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

file = open("Tests/SFSymbolsKitTests/NSImageExtensionTests.swift", "w")

file.write("//\n")
file.write("//  NSImageExtensionTests.swift\n")
file.write("//  SFSymbols\n")
file.write("//\n")
file.write(f"//  Generated by SFSymbolsKit on {formatted_date}\n")
file.write("//\n")
file.write("\n")
file.write("#if canImport(AppKit)\n")
file.write("import XCTest\n")
file.write("@testable import SFSymbolsKit\n")
file.write("\n")
file.write("final class NSImageExtensionTests: XCTestCase {\n\n")

with open('SFSymbols.txt') as topo_file:
    for line in topo_file:
        parts = line.split('.')
        camel_case_name = ""
        for part in parts:
            if part == parts[0]:
            
                if part.rstrip() in numbers:
                    camel_case_name += numbers[part.rstrip()]
                    continue
                elif part[0] in numbers:
                    camel_case_name += numbers[part[0]] + part[1:]
                    continue
                camel_case_name += part
                continue
            camel_case_name += part.capitalize()

        result = "    func test_StringExtension_{}_returnsImage() ".format(camel_case_name.rstrip())
        file.write(result)
        file.write("{\n")

        file.write("        // Arrange & Act\n")
        arrange = "        let image = NSImage.SFSymbols.{}\n".format(camel_case_name.rstrip())
        file.write(arrange)
        file.write("        // Assert\n")
        file.write("        XCTAssertNotEqual(image, NSImage())\n")
        file.write("    }\n\n")
file.write("}\n")
file.write("#endif\n")
file.close()
