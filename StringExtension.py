
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

file = open("Sources/SFSymbolsKit/String+Extension.swift", "w")

file.write("//\n")
file.write("//  String+Extension.swift\n")
file.write("//  SFSymbols\n")
file.write("//\n")
file.write("//  Created by Wikipedia Brown on 5/15/24.\n")
file.write("//\n")
file.write("\n")
file.write("public extension String {\n")
file.write("    enum SFSymbols {\n")

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
            
        result = "        static let {}: String = SFSymbol.{}.rawValue\n".format(camelCaseName.rstrip(), camelCaseName.rstrip())
        file.write(result)
file.write("    }\n")
file.write("}\n")
file.close()
