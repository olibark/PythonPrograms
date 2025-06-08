// BasicSwiftFeatures.swift
// A console Swift program demonstrating fundamental language features

import Foundation
import Darwin




// MARK: - Variables and Constants
var mutableInt: Int = 42
let constantString: String = "Hello, Swift!"
let pi: Double = 3.14159
var isActive: Bool = true
let Pi: Double = 3.14159265358979323846

// MARK: - String Interpolation & Tuple
let user: (name: String, age: Int) = ("Alice", 30)
print("\(constantString) My name is \(user.name) and I am \(user.age) years old.")
print("Pi is approximately \(pi)")
print("pi is \(Pi)")
// MARK: - Collections
var numberArray: [Int] = [1, 2, 3, 4, 5]
var nameSet: Set<String> = ["Bob", "Charlie", "Diana"]
var infoDict: [String: Any] = ["score": 95, "passed": true]

// MARK: - Control Flow
if mutableInt > 0 {
    print("Positive number")
} else if mutableInt < 0 {
    print("Negative number")
} else {
    print("Zero")
}

switch user.age {
case 0:
    print("Just born!")
case 1..<18:
    print("Minor")
case 18..<65:
    print("Adult")
default:
    print("Senior")
}

// MARK: - Loops
for num in numberArray {
    print("Number: \(num)")
}

var countdown = 5
while countdown > 0 {
    print(countdown)
    countdown -= 1
}

repeat {
    print("Repeating until zero")
    countdown -= 1
} while countdown > 0

// MARK: - Optionals
var optionalString: String? = "Optional Hello"
print(optionalString ?? "No value")

if let unwrapped = optionalString {
    print("Unwrapped: \(unwrapped)")
}

// MARK: - Functions & Closures
func greet(name: String = "Guest") -> String {
    return "Welcome, \(name)!"
}
print(greet())
print(greet(name: user.name))

let squaredNumbers = numberArray.map { $0 * $0 }
print("Squared: \(squaredNumbers)")

let evenNumbers = numberArray.filter { $0 % 2 == 0 }
print("Even: \(evenNumbers)")

let sum = numberArray.reduce(0) { $0 + $1 }
print("Sum: \(sum)")

// MARK: - Error Handling
enum SampleError: Error {
    case runtimeError(String)
}

func mightThrow(_ shouldThrow: Bool) throws -> String {
    if shouldThrow {
        throw SampleError.runtimeError("An error occurred")
    }
    return "Success"
}

do {
    let result = try mightThrow(false)
    print(result)
    _ = try mightThrow(true)
} catch SampleError.runtimeError(let message) {
    print("Caught error: \(message)")
} catch {
    print("Unexpected error: \(error)")
}

// MARK: - Structs, Classes, and Protocols
protocol Describable {
    func describe() -> String
}

struct Point: Describable {
    var x: Double, y: Double
    func describe() -> String {
        return "Point at (\(x), \(y))"
    }
}

class Animal: Describable {
    var name: String
    init(name: String) {
        self.name = name
    }
    func describe() -> String {
        return "Animal named \(name)"
    }
}

let p = Point(x: 1.0, y: 2.0)
let dog = Animal(name: "Rex")
print(p.describe())
print(dog.describe())

// MARK: - Enums and Associated Values
enum Result<T> {
    case success(T)
    case failure(Error)
}

let successResult: Result<String> = .success("OK")
let failureResult: Result<String> = .failure(SampleError.runtimeError("Failed"))

switch successResult {
case .success(let value):
    print("Got value: \(value)")
case .failure(let error):
    print("Error: \(error)")
}

// MARK: - Generics & Typealias
func swapValues<T>(_ a: inout T, _ b: inout T) {
    let temp = a
    a = b
    b = temp
}

typealias StringPair = (String, String)
var a = "Hello", b = "World"
swapValues(&a, &b)
print("Swapped: \(a) \(b)")

// MARK: - Concurrency (Swift 5.5+ async/await)
#if swift(>=5.5)
func fetchData() async throws -> String {
    try await Task.sleep(nanoseconds: 500_000_000)
    return "Data fetched"
}

Task {
    do {
        let data = try await fetchData()
        print(data)
    } catch {
        print("Async error: \(error)")
    }
}
// Keep the program running to await async task
RunLoop.main.run(until: Date().addingTimeInterval(1))
#endif
