struct Program {
    var name: String
    var version: String

    func displayInfo() { 
        print(version)
        print(name)
    }
}
let myProgram = Program(name: "MyApp", version: "1.0")
myProgram.displayInfo()


class Person {
    var name: String
    var age: Int

    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }

    func displayInfo() {
        print("Name: \(name), Age: \(age)")
    }
}
let person = Person(name: "Alice", age: 30)
person.displayInfo()