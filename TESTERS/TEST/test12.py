"""Challenge 5: Password Validator
Task:
Create a password validation program that:

Prompts the user to input a new password.
Checks that the password meets these criteria:
At least 8 characters long.
Contains both uppercase and lowercase letters.
Includes at least one digit.
If the password meets all criteria, display a success message.
If not, tell the user exactly which requirement(s) were not met."""


import os 
valid = False
os.system("clear")
while not valid:
    password = input("ENTER: ")
    if len(password) < 8:
        print("Too short: ")
    elif password.isalpha():
        print("No numbers: ")
    elif password.islower():
        print("No uppercase: ")
    elif password.isupper():
        print("No lowercase: ")
    else:
        print("Valid password: ")
        valid = True