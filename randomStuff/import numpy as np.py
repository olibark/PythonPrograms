import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

try:
    x = []
    y = []
    # Reduce range to prevent overflow
    for i in range(100):  # Changed from 100 to 20
        x.append(fib(i))
        y.append(fib(i+1))

    slope, intercept, r, p, std_err = stats.linregress(x, y)

    def myfunc(x):
        return slope * x + intercept

    mymodel = list(map(myfunc, x))

    plt.figure(figsize=(10,6))
    plt.scatter(x, y, color='blue', alpha=0.5, label='Data points')
    plt.plot(x, mymodel, color='red', label='Regression line')
    plt.xlabel('Fibonacci(n)')
    plt.ylabel('Fibonacci(n+1)')
    plt.title('Fibonacci Sequence Regression')
    plt.legend()
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")