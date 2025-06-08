import turtle
import random
import time 

turtle.setup(width=800, height=1200)  # Adjust the window size
s = turtle.getscreen()
turtle.bgcolor("black")
turtle.hideturtle()
turtle.colormode(255)
turtle.color("white")

# Display text at the top
turtle.penup()
turtle.goto(0, 450)  # Center the text horizontally
turtle.write("JOY DIVISION", align="center", font=("Arial", 50, "bold"))
turtle.goto(0, 0)

turtle.tracer(0, 0)
def draw_line(y, max_amplitude):
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(-300, y)  # Start from the left edge
    turtle.pendown()
    for x in range(-300, 300, 10):  # Draw across the width of the window
        distance_from_center = abs(x)  # Distance from the center of the line
        amplitude = max_amplitude * (1 - distance_from_center / 300)  # Decrease amplitude towards the edges
        wiggleoffset = random.randint(-int(amplitude), int(amplitude))
        turtle.goto(x, y + wiggleoffset)

for i in range(80):
    y = -300 + i * 9  # Adjust the vertical spacing
    max_amplitude = random.randint(2, 7)
    draw_line(y, max_amplitude)
    turtle.update()

while True:
    turtle.update()