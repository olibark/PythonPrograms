import tkinter as tk
import math

# Create the main window
root = tk.Tk()
root.title("Ray")

running  = True 

LineLength = 500
LineStartX = 700
LineEndX = 700
LineEndY = 500

# Create a canvas widget
canvas = tk.Canvas(root, width=1000, height=1000, bg="black")
canvas.pack()

# Define the center point and length of the lines
center_x, center_y = 500, 500
length = 1000

# Function to check if two line segments intersect and find the intersection point
def do_intersect(p1, q1, p2, q2):
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        return 1 if val > 0 else 2

    def on_segment(p, q, r):
        if min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]):
            return True
        return False

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, p2, q1):
        return True

    if o2 == 0 and on_segment(p1, q2, q1):
        return True

    if o3 == 0 and on_segment(p2, p1, q2):
        return True

    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False

# Function to draw rays and check for intersections
def draw_rays():
    rays = [
        ((center_x, center_y), (center_x + length, center_y)),
        ((center_x, center_y), (center_x - length, center_y)),
        ((center_x, center_y), (center_x, center_y + length)),
        ((center_x, center_y), (center_x, center_y - length))
    ]

    line_start = (LineStartX, center_y)
    line_end = (LineEndX, LineEndY)

    for ray in rays:
        canvas.create_line(ray[0], ray[1], fill="white")
        if do_intersect(ray[0], ray[1], line_start, line_end):
            canvas.create_oval(ray[1][0] - 5, ray[1][1] - 5, ray[1][0] + 5, ray[1][1] + 5, fill="red")

# Draw the line
canvas.create_line(LineStartX, center_y, LineEndX, LineEndY, fill="yellow")

# Draw the rays and check for intersections
draw_rays()

# Run the Tkinter event loop
root.mainloop()