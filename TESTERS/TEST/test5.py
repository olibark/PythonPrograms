import random
total = 0

def dice_roll():
    global total
    for i in range (2):
        number = random.randint(1,6)    
        total = total + number
        print (f"Roll {i + 1}: {number}")
    print (f"Total: {total}")
def computer_roll():
    global compnumber
    compnumber = random.randint (15, 21)

while total<21:
    dice_roll()
    choice = input("Would you like to roll again? ")
    if choice == "yes":
        dice_roll()
    elif choice == "no":
        print ("End of choices ")
        break
        
if total == 21:
    print("You have won!!! ")
    exit()
elif total >21:
    print ("You have lost!!! ")
    exit()
elif total <21:
    computer_roll()
    if compnumber > total:
        print (f"You have lost, computers roll was: {compnumber}, your total was: {total}")
        exit()
    elif compnumber <= total:
        print ("You have won!!! ")
        exit()

