def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else: 
        return fib(num - 1) + fib(num - 2)
def fib_iter(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a + b
    return a

def fib_memo(num, memo={}):
    if num in memo:
        return memo[num]
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else: 
        memo[num] = fib_memo(num - 1, memo) + fib_memo(num - 2, memo)
        return memo[num]
    
print (fib(10))
print (fib_iter(10))
print (fib_memo(10))
