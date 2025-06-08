import os

i = int(input(""))


while True:
    if i % 23423 == 0:
        i = i * i 
        print (i)
        break
    else:
        i += 1
        print (i)
        os.system("clear")

