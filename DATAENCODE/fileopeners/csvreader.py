import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
df = pd.read_csv('names.csv')
# Display the first few rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(df.head())
# Get the number of rows in the DataFrame
x = len(df)
# Split the DataFrame rows into 101 parts
parts = np.array_split(df, 1000)


for i in range (x):
    y = i 
    print(parts[y])



turns = int(input("How many times would you like to search? "))

for _ in range(turns):  # Use `_` for unused variables in the loop
    # Ask for the name to search
    namesearch = input("What name would you like to search for? ")

    # Initialize a flag to indicate if the name was found
    name_found = False

    # Iterate over the split parts
    for idx, part in enumerate(parts):
        if namesearch in part.values:
            print(f"The name '{namesearch}' exists in part {idx + 1}.")
            name_found = True
            break

    if not name_found:
        print(f"The name '{namesearch}' was not found in the DataFrame.")

    # Ask the user for a row part to display
    try:
        inoo = int(input(f"Enter a part number (1-{len(parts)}) to display: "))
        if 1 <= inoo <= len(parts):
            print(parts[inoo - 1])  # Adjust for zero-based index
        else:
            print(f"Invalid part number. Please choose between 1 and {len(parts)}.")
    except ValueError:
        print("Invalid input. Please enter a number.")




