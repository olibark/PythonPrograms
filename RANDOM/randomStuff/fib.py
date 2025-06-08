x = 0 


def fib(n: int, memo={}) -> int:
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[n]


for i in range(10):
    print(fib(i))