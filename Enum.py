
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

file = open("Sources/SFSymbolsKit/Enum.swift", "w")

file.write("//\n")
file.write("//  SFSymbol.swift\n")
file.write("//  SFSymbols\n")
file.write("//\n")
file.write("//  Created by Wikipedia Brown on 5/15/24.\n")
file.write("//\n")
file.write("\n")
file.write("#if canImport(AppKit)\n")
file.write("import AppKit\n")
file.write("#endif\n")
file.write("#if canImport(UIKit)\n")
file.write("import UIKit\n")
file.write("#endif\n")
file.write("\n")
file.write("public enum SFSymbol: String, CaseIterable {\n")
file.write("\n")

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
            
        result = "    case {} = \"{}\"\n".format(camelCaseName.rstrip(), line.rstrip())
        file.write(result)
file.write("\n")
file.write("#if canImport(UIKit)\n")
file.write("    @available(iOS 13, *)\n")
file.write("    var image: UIImage {\n")
file.write("        guard let image = UIImage(systemName: self.rawValue)\n")
file.write("        else { return UIImage() }\n")
file.write("        return image\n")
file.write("    }\n")
file.write("#endif\n")
file.write("\n")
file.write("#if canImport(AppKit)\n")
file.write("    @available(macOS 11.0, *)\n")
file.write("    var image: NSImage {\n")
file.write("        guard let image = NSImage(systemSymbolName: self.rawValue, accessibilityDescription:  \"This is the symbole for\\(self.rawValue)\")\n")
file.write("        else { return NSImage() }\n")
file.write("        return image\n")
file.write("    }\n")
file.write("#endif\n")
file.write("\n")
file.write("    var string: String {\n")
file.write("        return self.rawValue\n")
file.write("    }\n")
file.write("\n")
file.write("}\n")
file.close()
