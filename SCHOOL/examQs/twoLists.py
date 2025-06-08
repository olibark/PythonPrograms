import random

list1 = []
list2 = []
for i in range(1, 10000):
    list1.append(random.randint(1, 100000))
    list2.append(random.randint(1, 100000))
print("1: ", list1)
print("2: ", list2)
def sortMerge(list1, list2):
    binded = list1 + list2
    binded.sort()
    return binded

print("Merged and sorted: ", sortMerge(list1, list2))
