import tkinter as tk
import math

# Create the main window
root = tk.Tk()
root.title("Ray")

# Create a canvas widget
canvas = tk.Canvas(root, width=1000, height=1000, bg="black")
canvas.pack()

# Define the center point and length of the lines
center_x, center_y = 500, 500
length = 1000

# Draw lines for each degree in 360 degrees
def draw_rays():
    for degree in range(0, 360, 2):
        radians = math.radians(degree)
        end_x = center_x + length * math.cos(radians)
        end_y = center_y + length * math.sin(radians)
        canvas.create_line(center_x, center_y, end_x, end_y, fill="yellow", width=5)

draw_rays()
root.mainloop()