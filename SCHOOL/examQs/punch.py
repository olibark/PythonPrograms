from tabnanny import check

"""ticketArr = [[0, 0, "*"],
            ["*", "*", 0], 
            [0, "*", "*"],]
"""
ticketArr = [["*", "*", "*"],
            ["*", "*", "*"], 
            ["*", "*", "*"],]

def checkTicket(ticketArr):
    counter = 0
    for rows in range(len(ticketArr)):
        for columns in range(len(ticketArr[rows])):
            if ticketArr[rows][columns] == "*":
                ticketArr[rows][columns] = 1
                counter += 1
            else:
                ticketArr[rows][columns] = 0
    return counter

counter = checkTicket(ticketArr)
if counter == 9:
    print("BINGO")
else:
    print(counter)