import math

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

def decode(encoded_value, max_attempt=1000):
    """
    Attempts to decode an encoded value by brute force.
    Tries numbers from 1 to max_attempt to find the original number.
    """
    for num in range(1, max_attempt + 1):  # Iterate through possible numbers
        if encode(num) == encoded_value:
            return num  # Return the decoded number when a match is found
    return "Decoding failed (no match found)"

# Main program
chain = input("Enter the encoded numbers separated by spaces: ")

# Remove commas and split the numbers
cleaned_chain = chain.replace(",", "")  # Remove commas
encoded_values = list(map(int, cleaned_chain.split()))  # Convert to integers
decoded_values = []

for encoded_value in encoded_values:
    decoded_result = decode(encoded_value)
    decoded_values.append(decoded_result)
    print(f"Encoded: {encoded_value}, Decoded: {decoded_result}")

print("Final decoded results:", decoded_values)




