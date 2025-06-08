"""Write a function in Python that takes a list of integers and returns a new list with only the unique elements."""
import random

most = 0

def unique(nums):
    unique = []
    for i in range(len(nums)):
        times = 0
        checkedNum = nums[i]
        for j in range(len(nums)):
            if nums[j] == checkedNum:
                times += 1
            else:
                continue
        if times > 1:
            continue
        else:
            unique.append(checkedNum)
    return unique

for i in range(1000):
    nums = []
    mostArray = []
    for i in range(10):
        nums.append(random.randint(0, 10))
    check = len(unique(nums))
    if check > most:
        most = check
        mostArray = unique(nums)
        print(mostArray)
    
print(most)