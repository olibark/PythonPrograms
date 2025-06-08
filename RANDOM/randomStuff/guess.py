import random 
import time 
import sys
sys.set_int_max_str_digits(1000000)
noturns = 0 
number = random.randint(0, 100)
game = 0 
n = 100
print (number)
while game == 0:
    guess = number 
    if guess < number:
        print ("Your guess is to low! ")
        noturns = noturns + 1 
    elif guess > number:
        print ("Your guess is to high! ")
        noturns = noturns + 1 
    elif guess == number:
        print (("Well done bud! ") + ("you took ") + str(noturns) + (" number of turns"))
        print (("This is a harder level now!") + str(n) + (" numbers to choose from"))
        game = 0 
        n = (n * n)
        number = random.randint (0, n)
        print (number)




#float(input("What is your guess? "))

