"""Do not write
outside the
box
Write a Python program that calculates the value of a bonus payment for an employee
based on how many items they have sold and the number of years they have been
employed.
The program should:
• get the user to input the number of items sold
• get the user to input the number of years employed
• output the value of the bonus payment:
o if the years of employment is less than or equal to 2 and the number of items
sold is greater than 100, then the bonus will be the number of items sold
multiplied by 2
o if the years of employment is greater than 2, then the bonus will be the number of
items sold multiplied by 10
o otherwise, the bonus is 0
You should use indentation as appropriate, meaningful variable name(s) and Python
syntax in your answer.
The answer grid below contains vertical lines to help you indent your code."""


ItemsSold = int(input("Enter the number of items sold: "))
YearsEmployed = int(input("Enter the number of years employed: "))

if YearsEmployed <= 2 and ItemsSold > 100:
    bonus = ItemsSold * 2
elif YearsEmployed > 2:
    bonus = ItemsSold * 10
else:
    bonus = 10

print(bonus)