import tkinter as tk
import math

running = True 
circle_pos = [500, 500]
light_pos = [250, 250]
square_size = 100  # Define the size of the square

# Create the main window
root = tk.Tk()
root.title("Ray")

# Create a canvas widget
canvas = tk.Canvas(root, width=1000, height=1000, bg="black")
canvas.pack()

def draw_square():
    canvas.create_rectangle(circle_pos[0] - square_size // 2, circle_pos[1] - square_size // 2,
                            circle_pos[0] + square_size // 2, circle_pos[1] + square_size // 2,
                            outline="white", fill="white")

def draw_lightbulb():
    canvas.create_oval(light_pos[0] - 10, light_pos[1] - 10,
                       light_pos[0] + 10, light_pos[1] + 10,
                       outline="orange", fill="orange")

def draw_ray():
    for i in range(360):
        for length in range(1000):
            end_pos = (light_pos[0] + length * math.cos(math.radians(i)), light_pos[1] + length * math.sin(math.radians(i)))
            if check_intersection(light_pos, end_pos):
                canvas.create_line(light_pos[0], light_pos[1], end_pos[0], end_pos[1], fill="yellow")
                break
            canvas.create_line(light_pos[0], light_pos[1], end_pos[0], end_pos[1], fill="yellow")

def check_intersection(start_pos, end_pos):
    square_corners = [
        (circle_pos[0] - square_size // 2, circle_pos[1] - square_size // 2),
        (circle_pos[0] + square_size // 2, circle_pos[1] - square_size // 2),
        (circle_pos[0] + square_size // 2, circle_pos[1] + square_size // 2),
        (circle_pos[0] - square_size // 2, circle_pos[1] + square_size // 2)
    ]
     
    for i in range(4):
        next_i = (i + 1) % 4
        if line_intersection(start_pos, end_pos, square_corners[i], square_corners[next_i]):
            return True
    return False

def line_intersection(p1, p2, p3, p4):
    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
    
    return ccw(p1, p3, p4) != ccw(p2, p3, p4) and ccw(p1, p2, p3) != ccw(p1, p2, p4)

def on_click(event):
    global circle_pos
    circle_pos = [event.x, event.y]
    canvas.delete("all")
    draw_ray()
    draw_square()
    draw_lightbulb()

canvas.bind("<Button-1>", on_click)

draw_square()
draw_lightbulb()
root.mainloop()