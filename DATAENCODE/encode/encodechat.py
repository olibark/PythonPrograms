import math


def encode(numi):
    # Ensure numi is treated as a number
    try:
        numi = float(numi)  # Convert to a float for mathematical operations
    except ValueError:
        print(f"Cannot encode non-numeric value: {numi}")
        return None

    numsqr = numi * numi
    n = numsqr - numi + numi / numi  # Ensure no division by zero
    try:
        n1 = n + n 
        n2 = n1 ** n
        n3 = (n2 * n1 * n/n2 + n1 * n2/n)/n2 * n1
    except (ValueError, OverflowError) as e:
        print(f"Math error during encoding: {e}")
        return None

    return n3


# Input string to encode
chain = input("What would you like to encode? ")

# Length of the string
length_of_chain = len(chain)
print(f"Length of input: {length_of_chain}")

# Split characters into a list
array = list(chain)
print(f"Character array: {array}")

# Encoded string result
encoded_result = ""

# Process each character in the array
for char in array:
    print(f"Processing character: {char}")
    encoded_value = encode(char)
    if encoded_value is not None:
        # Convert the encoded value back to a string and add to the result
        encoded_result += str(encoded_value) + " "

# Print the final encoded string
print("Encoded result:")
print(encoded_result.strip())


def decode(encoded_value):
    try:
        # Reverse the calculation for n3
        # The encoded value n3 is quite complex, but we'll attempt to reverse it based on patterns
        n3 = float(encoded_value)  # Convert encoded value to float
        
        # Reverse the final complex operation (you'll need to reverse this carefully based on the encoding)
        # This is just an approximate approach and may not work perfectly.
        
        # Based on the encoding formula, let's try to isolate n1, n2, and n (approximating for simplicity)
        n = n3 / 2  # This is an assumption based on the encoding structure
        
        # Guess the original numi value using the square root of n (this is an approximation)
        numi_approx = math.sqrt(n)
        
        # Convert numi back to a character (assuming numi was an ASCII value)
        decoded_char = chr(int(numi_approx))
        
        return decoded_char
    except (ValueError, OverflowError) as e:
        print(f"Error during decryption: {e}")
        return None

# Example encoded input (replace this with the actual encoded result)
encoded_input = "encoded_value_here"  # Example, use the actual encoded string
encoded_values = encoded_input.split()

# Decode each encoded value back to the original characters
decoded_string = ""
for encoded_value in encoded_values:
    decoded_char = decode(encoded_value)
    if decoded_char is not None:
        decoded_string += decoded_char

print(f"Decoded string: {decoded_string}")