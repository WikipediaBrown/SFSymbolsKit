
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

file = open("Tests/SFSymbolsTests/StringExtensionTests.swift", "w")

file.write("//\n")
file.write("//  StringExtensionTests.swift\n")
file.write("//  SFSymbols\n")
file.write("//\n")
file.write("//  Created by nonplus on 12/18/21.\n")
file.write("//\n")
file.write("\n")
file.write("import XCTest\n")
file.write("@testable import SFSymbols\n")
file.write("\n")
file.write("final class StringExtensionTests: XCTestCase {\n\n")

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

        file.write("        // Arrange\n")
        arrange = "        let string = String.SFSymbols.{}\n".format(camelCaseName.rstrip())
        file.write(arrange)
        file.write("        // Act\n")
        file.write("        let image = UIImage(systemName: string)\n")
        file.write("        // Assert\n")
        file.write("        XCTAssertNotEqual(image, UIImage())\n")
        file.write("    }\n\n")
file.write("}\n")
file.close()
