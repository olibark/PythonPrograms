import math
pot = 0
def encode(numi):
    """Encodes a single number using the given formula."""
    num = int(numi)  # Convert the input to an integer
    if num == 0:
        num = num + 1
    
    # Perform calculations
    numsqr = (num + 1) * num + 1
    n = numsqr - num + num / num
    n1 = int(2 * n + (n * n) + (n * n * n) / n + n / math.sqrt(n))
    
    try:
        n2 = int(n1 ** n)
    except OverflowError:
        return "Result too large to compute"
    
    return n2

# Main program
chain = input("What would you like to encode? ")
array2 = []  # List to store encoded results

print("Input characters:", list(chain))

for char in chain:
    if char.isdigit():  # Process only digits
        result = encode(char)
        print(f"Character: {char}, Encoded result: {result}")
        array2.append(result)
    else:
        print(f"Skipping non-digit character: {char}")

print("Final encoded results:", array2)

x = len(array2)
for i in range (x):
    full = pot + array2 [i]
    full = (int(full) / int(x))
print (str("number = ") + str(full))

