#!/bin/bash

cd Code\ Generation\ Scripts

# Generate the UIImage extension and the unit tests for each property.
python UIImageExtension.py
python UIImageExtensionTests.py

# Generate the NSImage extension and the unit tests for each property.
python NSImageExtension.py
python NSImageExtensionTests.py

# Generate the String extension and the unit tests for each property.
python StringExtension.py
python StringExtensionTests.py

# Generate the `SFSymbol` enum that the `UIImage` & `String` extensions are
# based on.
python Enum.py
python EnumAppKitExtension.py
python EnumUIKitExtension.py
