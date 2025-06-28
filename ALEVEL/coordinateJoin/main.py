import math

def findHypot(x1, y1, x2, y2):
    length = x2 - x1
    height = y2 - y1
    return math.sqrt((length ** 2) + (height ** 2))

print(findHypot(1, 2, 4, 6))
