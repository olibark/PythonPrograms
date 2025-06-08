import time
import os
import pyttsx3
import pygame 
import keyboard
x = 0
running = True
searching = True 
array = []
pygame.mixer.init()
pygame.mixer.music.load('mixkit-epic-impact-afar-explosion-2782.wav')
time_string = time.strftime("%H:%M:%S")
file = open("quote_of_day.txt", "r")

for line in (file):
     line = line.strip()
     array.append(line)

engine = pyttsx3.init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_clock():
    print(("Time is:"), time_string)


alarm_time = str(input("What is your alarm time: "))
clear_screen()

while x == 0:
    
    time_string = time.strftime("%H:%M:%S")
    
    if  alarm_time == time_string:
        print ("Wake up! ")
        engine.setProperty('rate', 160)
        engine.setProperty('volume', 0.9)  
        text = "WAKE UP WAKE UP WAKE UP."
        engine.say(text)
        engine.runAndWait()
        timex = time.gmtime()
        engine.runAndWait()
        engine.say(array[(timex.tm_yday)- 1])
        engine.runAndWait()
        print (array[(timex.tm_yday)- 1])
        
        while running == True:
            pygame.mixer.music.play()
            while searching:
                if input("") == " ":
                    print ("Ah you are awake! ")
                    running = False
                else: 
                    break
            
    #elif alarm_time <= time_string:
    #    print ("Alarm time is too low: ")
    #   alarm_time = input("Try again: ")
                 
    else: 
        print ("Alarm time:",alarm_time)
        display_clock()
        time.sleep(1)
        clear_screen()

