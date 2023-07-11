#!/bin/bash

# Generate the UIImage extension and the unit tests for each property.
python UIImageExtension.py
python UIImageExtensionTests.py

# Generate the String extension and the unit tests for each property.
python StringExtension.py
python StringExtensionTests.py

# Generate the `SFSymbol` enum that the `UIImage` & `String` extensions are
# based on.
python Enum.py
