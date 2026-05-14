# Contributing to SFSymbolsKit

Thanks for your interest in contributing!

## Important: this library is generated

`Sources/SFSymbolsKit/*.swift` and `Tests/SFSymbolsKitTests/*.swift` are **generated** from `SFSymbols.txt` by the Python scripts at the repo root (`StringExtension.py`, etc.). Hand-edits to those files will be overwritten the next time the generator runs.

If you want to add or change symbol coverage, edit `SFSymbols.txt` (or the generator script that produces the Swift output), then regenerate.

## Workflow

1. Fork the repository.
2. Create your topic branch off **`develop`** (not `master`).
3. Make your changes.
4. Run the unit tests locally:
   ```
   bundle install
   bundle exec fastlane unit_test
   ```
5. Open a pull request against the **`develop`** branch. The PR template has a checklist — please fill it out.

`master` is the release branch and is updated only by merging `develop` into it; releases are cut automatically when that happens.

## Reporting bugs or requesting features

Use the appropriate issue template:

- **Bug Report** — for things that don't work as expected
- **Research** — for proposed investigations or technical questions
- **User Story** — for new feature requests framed from a user perspective

## Code of Conduct

Participation in this project is governed by the [Code of Conduct](./CODE_OF_CONDUCT.md). Be kind.
