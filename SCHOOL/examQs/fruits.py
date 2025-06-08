"""The program should:
• ask the user what word they would like to find
• output the message True if the word is found
• output the message False if the word is not found."""


fruits = ["banana", "apple", "orange", "pear", "grape" ,"pineapple"]

choice = input("What would you like to search for? ")

for i in range(len(fruits)):
    if choice == fruits[i]:
        print(f"Succes, fruit was found in at point {i + 1}")
        exit()

print("Your word was not found in array: ")
