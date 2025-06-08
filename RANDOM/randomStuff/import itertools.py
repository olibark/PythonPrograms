import itertools
import string

def password_guesser(target_password):
    characters = string.ascii_letters + string.digits + string.punctuation
    password_length = len(target_password)

    print("Attempting to guess the password...")

    # Try every combination of characters up to the length of the target password
    for guess_length in range(1, password_length + 1):
        for guess in itertools.product(characters, repeat=guess_length):
            guess = ''.join(guess)
            if guess == target_password:
                print(f"Password guessed successfully! The password is: {guess}")
                return guess
    
    print("Password could not be guessed.")

# Example usage
target_password = "hello"
password_guesser(target_password)