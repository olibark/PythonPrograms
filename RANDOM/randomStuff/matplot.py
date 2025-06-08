import numpy as np
import matplotlib.pyplot as plt

# Generate x values in degrees
x_degrees = np.linspace(0, 360, 100)

# Convert x to radians for trigonometric functions
x_radians = np.radians(x_degrees)

# Calculate y values
y = np.sin(x_radians)
y2 = np.cos(x_radians)
y3 = np.tan(x_radians)

# Create the plot
plt.plot(x_degrees, y, label='Sine Wave')
plt.plot(x_degrees, np.zeros_like(x_degrees), label='Zero Line', linestyle='--')
plt.plot(x_degrees, y2, label='Cosine Wave')
plt.fill_between(x_degrees, y, y2, where=(y > y2), color='lightblue', alpha=0.5, label='Area between curves')
plt.plot(x_degrees, y3, label='Tangent Wave', color='orange')
plt.ylim(-1, 1)  # Set y-axis limits for tangent function

# Set x-axis ticks to go up in 90-degree intervals
plt.xticks(np.arange(0, 361, 90))

# Add labels and title
plt.xlabel('Degrees')
plt.ylabel('Y-axis')
plt.title('Demo of Matplotlib (Degrees)')

# Add a legend
plt.legend()

# Show the plot
plt.show()