items = int(input("how many items have you sold?"))
noofyears = int(input("How long have you worked? "))

if noofyears <= 2 and items > 100:
    bonus = items * 2
elif noofyears > 2:
    bonus = items * 10
else:
    bonus = 0

print (f"bonus ={bonus} ")
