import random
import string

def random_char_generator(length=1):
    # Define the character pool
    characters = string.ascii_letters  # Only characters
    random_chars = ''.join(random.choice(characters) for _ in range(length))
    return random_chars

# Initialize an empty array
array = []

# Ask for password preferences
length_of_password = int(input("How long would you like the password to be? "))
password_type = input("Would you like your password to contain numbers, characters, or both? (num, char, both): ").lower()

# Generate password based on user input
if password_type == "num":
    for _ in range(length_of_password):
        num = str(random.randint(0, 9))  # Convert number to string for consistent printing
        array.append(num)
elif password_type == "char":
    for _ in range(length_of_password):
        random_char = random_char_generator(1)
        array.append(random_char)
elif password_type == "both":
    for _ in range(length_of_password):
        if random.choice([True, False]):  # Randomly choose between num and char
            array.append(str(random.randint(0, 9)))
        else:
            array.append(random_char_generator(1))
else:
    print("Invalid input. Please enter 'num', 'char', or 'both'.")
    exit()

# Print the password as a single line without dividers
print("Your password: ", end='')
print(*array, sep='')
