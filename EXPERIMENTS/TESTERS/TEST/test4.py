total = float(input("How much was the full bill? "))
noofopeople = int(input("How many people are paying? "))
while total >= 0:
    persopayed = float(input("How much will you pay? "))
    total = float(total) - persopayed
    if total == 0:
        print ("Bill payed ")
        exit()
    if total <= 0:
        total = str(total)
        total = total.replace("-", "")
        print (f"Tip is £{total}0")
        break 
    else:
        print (f" £{total}0 left to pay ")