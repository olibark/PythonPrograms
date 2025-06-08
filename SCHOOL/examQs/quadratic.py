import math
from os import error

abc = ['A', 'B', 'C']

for i in range(3):
    abc[i] = int(input(f"{abc[i]}: "))

a, b, c = abc[0], abc[1], abc[2]

def quadratic(a, b, c):
    try:
        x = ((-1 * b) + (math.sqrt((b * b) - (4 * (a * c))))/ (2 * a))
    except error as e:
        print (f"Error has occured: {e}")
    
    
    return x

print(quadratic(a, b, c))