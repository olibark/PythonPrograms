running = True
def check(word, guess, hidden):
    for i in range(0, len(word)):
        if word[i] == guess:
            hidden = hidden[:i] + guess + hidden[i+1:]
    return hidden

word = input("Enter a word: ")
hidden = ""
for i in range(0, len(word)):
    hidden += "*"    
while running:
