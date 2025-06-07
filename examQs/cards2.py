position = int(input("Enter card position: "))

trying = True
while trying:
    if position < 1 or position > 100:
        print("entert a valid")
        position = int(input("Enter card position: "))
    else:
        trying = False
print("valid position")