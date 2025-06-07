import os
os.system("clear")

word = input("Enter a word: ")
wordArray = [char for char in word]
reversedArray = wordArray[::-1]
reversedWord = "".join(reversedArray)
os.system("clear")
print("Word = ",word)
print("Reversed = ",reversedWord)
if wordArray == reversedArray:
    print("The word is a palindrome.")
else:
    print("Not a palindrome. ")