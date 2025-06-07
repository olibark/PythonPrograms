"""1 Do not write
outside the
box
Figure 16 shows an incomplete Python program to create a bingo ticket for a player.
The programmer has used a two-dimensional array called ticket to represent a
bingo ticket.
The program uses a subroutine called generateKeyTerm. When called, the
subroutine will return a random key term, eg "CPU"
"ALU"
,
,
"NOT gate" etc.
Complete the Python program in Figure 16 by filling in the five gaps.
• Line numbers are included but are not part of the program.
[4 marks]
Figure 16
1 ticket = [["","",""],
            ["","",""],
            ["","",""]]
2 i = 0
3 while i < 3:
    j = 0
5 while j < 3:
6   ticket[ ____ ][ ____ ] = generateKeyTerm()
7
______________
8
______________
Question 14 continues on the next pa"""
import random

def generateRandomTicket():
    choices = ["hello", "hello1", "hello2", "hello3"]
    thing = random.choice(choices)
    return thing
ticket = [["","",""],
            ["","",""],
            ["","",""]]

i = 0
while i < 3:
    j = 0
    while j < 3:
        ticket[i][j] = generateRandomTicket()
        j += 1
    i += 1    

for i in range(3):
    print(ticket[i])