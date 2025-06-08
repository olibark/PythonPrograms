// Example 1: Hello World
print("Hello, World!")

// Example 2: Variables and Constants
var variable = 10
let constant = 20
variable = 15
print("Variable: \(variable), Constant: \(constant)")

// Example 3: Functions
func greet(name: String) -> String {
    return "Hello, \(name)!"
}
print(greet(name: "Oliver"))

// Example 4: Control Flow
let number = 5
if number % 2 == 0 {
    print("\(number) is even")
} else {
    print("\(number) is odd")
}

// Example 5: Loops
for i in 1...5 {
    print("Iteration \(i)")
}

// Example 6: Arrays
var fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Date")
print(fruits)

// Example 7: Dictionaries
var capitals = ["France": "Paris", "Japan": "Tokyo"]
capitals["USA"] = "Washington, D.C."
print(capitals)

// Example 8: Classes and Objects
class Person {
    var name: String
    init(name: String) {
        self.name = name
    }
    func introduce() {
        print("Hi, my name is \(name).")
    }
}
let person = Person(name: "Oliver")
person.introduce()

// Example 9: Optionals
var optionalString: String? = "Hello"
if let unwrappedString = optionalString {
    print(unwrappedString)
}

// Example 10: Closures
let numbers = [1, 2, 3, 4, 5]
let squaredNumbers = numbers.map { $0 * $0 }
print(squaredNumbers)

// Example 11: Enumerations
enum Direction {
    case north, south, east, west
}
let travelDirection = Direction.north
print("Traveling \(travelDirection)")

// Example 12: Structs
struct Point {
    var x: Int
    var y: Int
}
let point = Point(x: 10, y: 20)
print("Point: (\(point.x), \(point.y))")

// Example 13: Protocols
protocol Greetable {
    func greet()
}
class FriendlyPerson: Greetable {
    func greet() {
        print("Hello!")
    }
}
let friendlyPerson = FriendlyPerson()
friendlyPerson.greet()

// Example 14: Error Handling
enum CustomError: Error {
    case invalidInput
}
func checkInput(_ input: Int) throws {
    if input < 0 {
        throw CustomError.invalidInput
    }
}
do {
    try checkInput(-1)
} catch {
    print("Caught an error: \(error)")
}

// Example 15: Generics
func swapValues<T>(_ a: inout T, _ b: inout T) {
    let temp = a
    a = b
    b = temp
}
var a = 1, b = 2
swapValues(&a, &b)
print("a: \(a), b: \(b)")