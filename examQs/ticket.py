"""The program must:
• get the user to enter the number of people in a group
• calculate the total charge by:
o charging £15 per person
o reducing the total charge by £5 if there are six or more people
• output the total charge."""
ticketPrice = 15
noPeople = int(input("How many people in your group? "))

totalCharge = noPeople * ticketPrice

if noPeople >= 6:
    totalCharge = totalCharge - 5

print(f"Total charge = {totalCharge}")