struct Greet {
    func hello(name: String) {
        print("Hello, \(name)!")
    }
    func bye(name: String) {
        print("Goodbye \(name)!")
    }
}
let name: String = readLine() ?? "Name: "
Greet().hello(name: name)
Greet().bye(name: String(name.reversed()))