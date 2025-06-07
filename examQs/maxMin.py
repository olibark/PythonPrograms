import random

numbers = []
for i in range(1000):
    numbers.append(random.randint(1, 10000))

def MinMax(numbers):
    min = numbers[0]
    max = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
        elif numbers[i] < min:
            min = numbers[i]
    return min, max

print(MinMax(numbers))