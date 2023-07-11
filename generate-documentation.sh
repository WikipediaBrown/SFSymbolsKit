#!/bin/sh

xcodebuild docbuild -scheme SFSymbols \
    -destination generic/platform=iOS \
    OTHER_DOCC_FLAGS="--transform-for-static-hosting --hosting-base-path SFSymbols --output-path docs" \
