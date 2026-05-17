import SwiftUI
import SFSymbolsKit

struct ContentView: View {
    var body: some View {
        // Stringly-typed: a typo here ships a blank icon.
        Image(systemName: "square.and.arrow.up")
    }
}
