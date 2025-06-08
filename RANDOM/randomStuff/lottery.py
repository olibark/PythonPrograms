import random
import os

usernumbers = []
lotterynumbers = []

def lottery():
    global lotterynumbers
    lotterynumbers = []
    for i in range (1, 6):
        lotterynumbers.append(random.randint(1, 40))
    return lotterynumbers


def user_numbers():
    global usernumbers
    usernumbers = []
    for i in range(1, 6):
        usernumbers.append(int(input("Enter your number: ")))
        os.system('clear')
    return usernumbers

os.system('clear')

print("Your numbers were: " + ", ".join(map(str, user_numbers())))
print("The winning numbers are: " + ", ".join(map(str, lottery())))