print ("hello world")
ballno = 0
over = 6 
ball = 1
dot = 0 
onerun = 1 
tworuns = 2 
threeruns = 3
four = 4 
fiveruns = 5
six = 6 
score = 0 
wickets = 0
noofbat = 11
noofovers = 0 
noball = 1


while over > 0:
    outcome = input ("what is the outcome? ")
    if outcome == ".":
        ballno += 1
        over = over - 1
        print (str(over) + (" to come"))
        score = score + 0 
        print (str(score) + (" for ")+ str(wickets) + (" from ") + str(noofovers))
    elif outcome == "1":
        ballno += 1 
        over = over - 1
        score = score + onerun
        print (str(over) + (" to come"))
        print (str(score) + (" for ")+ str(wickets) + (" from ") + str(noofovers))
    elif outcome == "2":
        ballno += 1 
        over = over - 1
        score = score + tworuns
        print (str(over) + (" to come"))
        print (str(score) + (" for ")+ str(wickets) + (" from ") + str(noofovers))
    elif outcome == "3":
        ballno += 1 
        over = over - 1
        score = score + threeruns
        print (str(over) + (" to come"))
        print (str(score) + (" for ")+ str(wickets) + (" from ") + str(noofovers))
    elif outcome == "4":
        ballno += 1 
        over = over - 1
        score = score + four
        print (str(over) + (" to come"))
        print (str(score) + (" for ")+ str(wickets) + (" from ") + str(noofovers))
    elif outcome == "5":
        ballno += 1 
        over = over - 1
        score = score + fiveruns
        print (str(over) + (" to come"))
        print (str(score) + (" for ")+ str(wickets) + (" from ") + str(noofovers))
    elif outcome == "6":
        ballno += 1 
        over = over - 1
        score = score + six
        print (str(over) + (" to come"))
        print (str(score) + (" for ")+ str(wickets) + (" from ") + str(noofovers))
    elif outcome == "w":
        ballno += 1 
        over = over - 1
        score = score
        wickets = wickets + 1
        noofbat = noofbat - 1 
        print (str(over) + (" to come"))
        print (str(score) + (" for ")+ str(wickets) + (" from ") + str(noofovers))
        print (str("number of bats = ") + str(noofbat))
    elif outcome == "!":
        ballno = ballno 
        over = over
        score = score + noball
        print (str(over) + (" to come"))
        print (str(score) + (" for ")+ str(wickets) + (" from ") + str(noofovers))
    
    
    if ballno % 6 == 0:
            yes = input("Start a new over? (./no): ").lower()
            if yes == ".":
                over += 6
                print("New over started!")
                ballno = ballno + 6
                noofovers = noofovers + 1 
            else:
                 yes = input("Start a new over? (./no): ").lower()
    if noofbat == 0:
            print(f"Game Over: {score} for {wickets} from {noofovers}")
    


