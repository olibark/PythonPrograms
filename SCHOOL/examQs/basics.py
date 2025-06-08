def PrintMessage(message):
    print(message)
    print(f"This is a message using f print: {message}")
PrintMessage("Hello world")

def Mod(x, y):
    print(f"Modulus of{x} and {y} = {x % y}")

Mod(10, 3)

def Div(x, y):
    print(f"Division of {x} and {y} = {x / y}")
    print(f"Integer Division of {x} and {y} = {x // y}")

Div(10, 3)

def Odd(x):
    if x % 2 == 0:
        return False
    else:
        return True

print(Odd(10))

for i in range(0, 3):
    print(f"i = {i}")
for i in range(3):
    print(f"i = {i}")
for i in range(3, 0, -1):
    print(f"i = {i}")
