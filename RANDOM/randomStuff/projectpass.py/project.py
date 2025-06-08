import string
import random 
import os
import time



def openscreen():
    openarray = []
    print ("DOWLOADING........")
    time.sleep(1)
    for i in range (22):
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

def PASSMAKER():
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
            PASSMAKER()
        #if choice == "B":
        #    mainunknown()
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

