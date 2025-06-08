import random


One = []
Two = []
for i in range(5):
    One.append(int(random.randint(1, 100)))
    Two.append(int(random.randint(1, 100)))

print(One)
print(Two)

for i in range(5):
    if One[i] > Two[i]:
        One[i], Two[i] = Two[i], One[i]
print(One)
print(Two)