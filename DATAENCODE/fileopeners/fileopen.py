

total = 0

def numbercounter():
    try:
        with open("data.txt", "w") as f:
            numbers = []
            for i in range(123456):
                numbers.append(i + 1)
                f.write(f"this is line {i+1}\n")
        with open("data.txt", "r") as f:
            total = 0
            for line in f:
                if line.startswith("this is line"):
                    number = int(line.split("line")[1].strip())
                    total = total + number
                else:
                    break
            return total
    except FileNotFoundError:
        print ("This file does not exist")
        return 0 


total = numbercounter()
print (total)
