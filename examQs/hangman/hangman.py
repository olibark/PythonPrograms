import random
import linecache
running = True
avaliableLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
wordLetters = []
foundLetters = []

def pickWord():
    randomLine = random.randint(1, 101)
    specific_line = linecache.getline("words.txt", randomLine)
    if specific_line:
        return specific_line
    return None
word = pickWord()



for i in range(len(word) - 1):
    wordLetters.append(word[i])
print(f"Word to find: {wordLetters}")

while running:
    userLetter = str(input("enter letter")).lower()
    if len(userLetter) != 1 or userLetter not in avaliableLetters:
        print("Invlaid")
        continue
    if userLetter in wordLetters:
        foundLetters.append(userLetter)
        print("correct guess")
        print(foundLetters)
    else:
        print("incorrect")
        print(foundLetters)
    if all(letter in foundLetters for letter in wordLetters):
        print(f"word has been found word was: {word}")
        break
    