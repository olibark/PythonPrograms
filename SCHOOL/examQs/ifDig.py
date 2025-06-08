string = input("")

def FindDigit(string):
    for i in range(len(string)):
        if string[i].isdigit():
            return True
    return False

print(FindDigit(string))