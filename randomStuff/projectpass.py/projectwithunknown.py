import string
import random 
import os
import time

#random.randint(1, lenofpass
def mainunknown():
    while True:
        import turtle
        import random

        turtle.setup(width= 800, height=1400)
        s = turtle.getscreen()
        turtle.bgcolor("black")
        turtle.hideturtle()
        turtle.colormode(255)
        turtle.color("white")
        canvas = turtle.getcanvas()


        turtle.penup()
        turtle.goto(0, 450)
        turtle.write("JOY DIVISION",align="center", font=("Arial", 50, "bold"))
        turtle.goto(0, 0)


        turtle.tracer(0, 0)
        def draw_line(y , max_amplitude):
            turtle.speed("fastest")
            turtle.penup()
            turtle.goto(-300, y)
            turtle.pendown()
            for x in range(-300, 300, 8):
                distanceaway = abs(x)
                amplitude = max_amplitude * (1 - distanceaway / 300)
                wiggleoffset = random.uniform((amplitude), 7 * (amplitude))
                turtle.goto(x, y + wiggleoffset)


        for i in range(80):
            y = -300 + i * 9
            max_amplitude = random.randint(2, 7)
            draw_line(y, max_amplitude)
            turtle.update()
            
        turtle.penup()
        turtle.goto(0, -350)
        turtle.write("Unknown Pleasures",align="center", font=("Arial", 35, "bold"))


        turtle.penup()
        turtle.goto(0, -400)
        turtle.write("Oliver Barkham",align="center", font=("Courier New", 28, "bold"))
        turtle.goto(0, 0)   

        if turtle.Terminator:
            os.system("clear")
            print ("press enter to go to menu...")
            
            return
        while True:
            turtle.update()

def openscreen():
    openarray = []
    print ("DOWLOADING........")
    time.sleep(1)
    for i in range (2):
        for j in range (i):
            openarray.append("-")
            screen = separate_array(openarray)
            print (screen)
            time.sleep(0.023)
    os.system("clear")        
    print ("DOWNLOAD COMPLETE........")
    time.sleep(1)




def separate_array(arr):
    return ' '.join(map(str, arr)).replace(',', '').replace(" ", "")

def random_letter():
    randomletter = random.choice(string.ascii_letters)
    return randomletter

def A():
    while True:
        os.system("clear")
        passwordarray = []
        characterset = ['!', '"', '#',
                        '$', '%', '&', 
                        "'", '(', ')', 
                        '*', '+', ',', 
                        '-', '.', '/', 
                        ':', ';', '<', 
                        '=', '>', '?', 
                        '@', '[', ']', 
                        '^', '_', '`', 
                        '{', '|', '}', 
                        '~']

        print("--PASWORD-GEN.OLI--")
        print ()
        lenofpass = int(input("--HOW-LONG-SHOULD-PASSWORD-BE--"))
        halflengthofpass = lenofpass//2
        for i in range (0, lenofpass):
            passwordarray.append(random.randint(1, 10))
        for i in range (0, halflengthofpass):
            randomchoice = random.choice(characterset)
            passwordarray[random.randint(0, len(passwordarray) - 1)] = randomchoice
        for i in range (0, (halflengthofpass) + (halflengthofpass // 2)+ halflengthofpass):
            passwordarray[random.randint(0, len(passwordarray) - 1)] = random_letter()
        #passwordarray.append(".oli")

        print (separate_array(passwordarray))
        print ("--Q-TO-QUIT-------- ")
        print ("--B-TO-MENU-------- ")
        print ("--C-TO-CHOOSE-NEW-- ")
        choice = input("").upper()
        if choice == "Q":
            os.system("clear")
            exit()
        if choice  == "B":
            os.system("clear")
            return
        elif choice == "C":
            continue
        else:
            print("invalid...")
            print ("Input new choice below")
            choice = input("").upper()

        
def menu():
    while True:
        print ("[----[--WELCOME-TO-PASSWORD.OLI-]-----] ")
        print()
        print ("  .---CHOICE-A--password-creator---. ")
        print ("  .---CHOICE-B--password-checker---. ")
        print ("       ._--CHOICE-C--exit--_. ")
        print()
        choice = (input("      [WHAT-IS-YOUR-WISH-SIR] ")).upper()
        
        if choice == "A":
            A()
        if choice == "B":
            mainunknown()
        elif choice == "C":
            os.system("clear")
            print("--GOODBYE-SIR--")
            exit()
        else:
            os.system("clear")
            print ("Invalid input ")
openscreen()       
os.system("clear")
menu()

