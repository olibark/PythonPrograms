"""Ask the user how many days worth of sales data they would like to enter.
Record the sales for each day in a suitable data structure.
Calculate and display:
The total sales over the given period.
The average daily sales (rounded to 2 decimal places).
The maximum sales recorded on a single day.
The minimum sales recorded on a single day.
Optionally allow the user to display sales for a specific day if they provide the day number"""

import os

os.system("clear")

noDays = int(input("How many days would you like to enter? "))

dayArray = []
sales = []

minimum = 0 
maximum = 0
salesTotal = 0

os.system("clear")

for i in range (noDays):
    saleOfday = (int(input(f"What was the sales for day {i + 1}: ")))
    
    sales.append(saleOfday)
    dayArray.append(i + 1)
    
    salesTotal = salesTotal + saleOfday
    
    if saleOfday > maximum:
        maximum = saleOfday
    
    os.system("clear")
    
lowest = sales[noDays - 1]

for i in range(noDays):
    if sales[i] < lowest:
        lowest = sales[i]

average = salesTotal / noDays

print (f"Day  =  {dayArray}")
print (f"sales = {sales}")
print (f"Lowest = {lowest}")
print (f"Max = {maximum}")
print (f"Average = {average}")
print (f"Total sales = {salesTotal}")