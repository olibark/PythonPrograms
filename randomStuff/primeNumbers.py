def check_prime(num):
    if num <= 1:
        return False
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            return False
    return True
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:  # 1 and negative numbers are not prime
        return False
    if n <= 3:  # 2 and 3 are prime numbers
        return True
    if n % 2 == 0 or n % 3 == 0:  # Eliminate multiples of 2 and 3
        return False

    # Check divisors from 5 to √n, skipping multiples of 2 and 3
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:  # Check i and i + 2
            return False
        i += 6  # Only test numbers in the form of 6k ± 1

    return True
for i in range (50):
    
    n = (((i * i) + i ) + 1)
    number = n 
    if check_prime(number):
        print((i) + number, "is a prime number.")
    else:
        print(number, "is not a prime number.")
    


number = n 
if check_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")