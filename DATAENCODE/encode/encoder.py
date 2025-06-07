import math
array2 = []
def encode(numi):
    """Encodes a single number using the given formula."""
    num = int(numi)  # Convert the input to an integer
    if num == 0:
        return "Cannot encode zero (division by zero)"
    
    # Perform calculations
    numsqr = (num + 1) * num + 1
    n = numsqr - num + num / num
    n1 = int(2 * n + (n * n) + (n * n * n) / n + n / math.sqrt(n))
    
    try:
        n2 = int(n1 ** n)
    except OverflowError:
        return "Result too large to compute"
    
    return n2

chain = (input("what would you like to encode "))
length_of_chain = len((chain))
split = split_characters = list(chain)
array = split

print (array)
for i in range (length_of_chain):
    if chain == 0:
        print ("no")
    numi = array[i]
    print (numi)
    print (encode())
    x = (encode())
    array2.append (x)
    print (array2)
      





