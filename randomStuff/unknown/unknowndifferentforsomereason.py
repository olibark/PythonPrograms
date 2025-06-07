import turtle
import random


turtle.setup(width= 800, height=1400)
s = turtle.getscreen()
turtle.bgcolor("black")
turtle.hideturtle()
turtle.colormode(255)
turtle.color("white")
canvas = turtle.getcanvas()


turtle.penup()
turtle.goto(0, 450)
turtle.write("JOY DIVISION",align="center", font=("Arial", 50, "bold"))
turtle.goto(0, 0)


turtle.tracer(0, 0)
def draw_line(y , max_amplitude):
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(-300, y)
    turtle.pendown()
    for x in range(-300, 300, 8):
        distanceaway = abs(x)
        amplitude = max_amplitude * (1 - distanceaway / 300)
        wiggleoffset = random.uniform((amplitude), 7 * (amplitude))
        turtle.goto(x, y + wiggleoffset)


for i in range(80):
    y = -300 + i * 9
    max_amplitude = random.randint(2, 7)
    draw_line(y, max_amplitude)
    turtle.update()
    
turtle.penup()
turtle.goto(0, -350)
turtle.write("Unknown Pleasures",align="center", font=("Arial", 35, "bold"))


turtle.penup()
turtle.goto(0, -400)
turtle.write("Oliver Barkham",align="center", font=("Courier New", 28, "bold"))
turtle.goto(0, 0)   




while True:
    turtle.update()
