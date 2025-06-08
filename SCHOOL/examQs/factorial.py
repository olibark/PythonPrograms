def getFact(number):
    for i in range(number - 1, 0, -1):
        number *= i
    return number
number = int(input())
print(getFact(number))