import random
import os



running = True


while running:
    os.system('clear')
    comparedTo = random.randint(1, 10000)
    randint = random.randint(1, 10000)
    print (comparedTo)
    print (randint)

    if randint == comparedTo:
        print ("done")
        running = False