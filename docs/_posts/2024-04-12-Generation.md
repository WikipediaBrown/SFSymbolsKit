---
layout: post
author: Wikipedia Brown
---

The scripts used to generate the extensions and enum are written in `Python 2.7.18`. Which means you'll need Python. 

### Get Python
Assuming you're running macOS, you should first install [Homebrew](https://brew.sh) and then use Homebrew to install Python by running the command `brew install python`.

### Get List of Names
Get list of names of `SFSymbols` by opening the SFSymbols App (you can get it from [ Developer](https://developer.apple.com/sf-symbols/)) and paste it into the SFSymbols.txt file. Check out this [StackOverflow](https://stackoverflow.com/a/63310093/5863650) post.

### Run Python Scripts
Run the command `python3 UIImageExtension.py && python3 UIImageExtensionTests.py && python3 StringExtension.py && python3 StringExtensionTests.py && python3 Enum.py` and the python scripts will regenerate the extension and enum.