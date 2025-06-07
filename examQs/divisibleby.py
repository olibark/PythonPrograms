numbers = []

for i in range(1, 10000):
    for j in range(1, 10000):
        if (i % j) == 0:
            numbers.append(i)
    else:
        continue
print(numbers)