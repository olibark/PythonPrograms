rows = 5  # Number of rows in the pyramid

for i in range(1, rows + 1):
    spaces = rows - i  # Calculate leading spaces
    stars = 2 * i - 1  # Calculate the number of stars
    print(" " * spaces + "*" * stars + " " * spaces)
