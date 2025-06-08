import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Joy Division")
root.geometry("800x1400")
root.configure(bg="black")

# Create a canvas widget
canvas = tk.Canvas(root, width=800, height=1400, bg="black")
canvas.pack()

# Function to draw text
def draw_text():
    canvas.create_text(400, 100, text="JOY DIVISION", fill="white", font=("Arial", 50, "bold"))

# Function to draw a continuous line with wiggles
def draw_line(y, max_amplitude):
    points = []
    for x in range(-300, 301, 8):
        distanceaway = abs(x)
        amplitude = max_amplitude * (1 - distanceaway / 300)
        wiggleoffset = random.uniform(-amplitude, amplitude)
        points.append((x + 400, y + wiggleoffset))
    canvas.create_line(points, fill="white")

# Draw the text
draw_text()

# Draw multiple continuous lines with wiggles
for y in range(0, 800, 20):
    draw_line(y + 300, 50)

# Run the Tkinter event loop
root.mainloop()

# Run the Tkinter event loop
root.mainloop()