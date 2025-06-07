"""Create a Python program that converts a given decimal number to its binary equivalent."""

def binary(number):
    """Convert decimal to binary."""
    if number < 0:
        raise ValueError("Number must be non-negative")
    if number == 0:
        return "0"
    
    binary_number = ""
    while number > 0:
        binary_number = str(number % 2) + binary_number
        number //= 2 
    return binary_number

number = int(input(""))
print(binary(number))