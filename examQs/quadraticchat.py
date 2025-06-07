import math

# Get inputs for A, B, and C
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

def quadratic(a, b, c):
    """Return real solutions of ax^2 + bx + c = 0, if they exist."""
    try:
        # Calculate discriminant
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            # This will raise a ValueError if we attempt sqrt of a negative number
            raise ValueError("Discriminant is negative. No real solutions.")
        
        # Calculate the square root of the discriminant
        sqrt_disc = math.sqrt(discriminant)
        
        # Two solutions:
        x1 = (-b + sqrt_disc) / (2*a)
        x2 = (-b - sqrt_disc) / (2*a)
        
        # If the discriminant is zero, both solutions are the same
        if discriminant == 0:
            return x1  # or return (x1, x1) if you want a tuple
        
        # Otherwise, return both distinct solutions
        return x1, x2
    
    except ValueError as e:
        # Handle the case where no real solutions exist
        print(f"Error: {e}")
        return None

# Calculate and display the solution(s)
solution = quadratic(a, b, c)

if solution is not None:
    print("Solution(s):", solution)