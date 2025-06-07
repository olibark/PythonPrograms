"""Write a Python program to check if a player has a valid run of five cards within their
100 cards.
When writing your program you should assume:
• there is an array called cards that contains the values of the players 100 cards
• cards[0] will contain the value of the first card and cards[99] will contain
the value of the last card
• the values in cards are already stored in numerical order
• there is a Boolean variable called gameWon that has a value of False.
Your program should set gameWon to True if there is a valid run.
You should use indentation as appropriate, meaningful variable name(s) and Python
syntax in your answer.
The answer grid below contains vertical lines to help you indent your code."""
import random
import os

cards = []

for i in range(200):
    cards.append(random.randint(1, 100))
print(cards)
cards.sort()

def checkRun(cards):
    gameWon = False
    for i in range(len(cards)):
        if i + 4 >= len(cards):
            break
        if cards[i] == cards[i + 1]:
            if cards[i] == cards[i + 2]:
                if cards[i] == cards[i + 3]:
                    if cards[i] == cards[i + 4]:
                        gameWon = True
                        break
        
    return gameWon
gameWon = checkRun(cards)

if gameWon:
    os.system('clear')
    print("You have a valid run of five cards!")