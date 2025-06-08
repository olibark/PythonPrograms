import turtle
import time 

charge = 2
#no_of_passengers = input("How many passengers? ")
length_of_journey = float(input("What is the length of your journey? (in kilometres) "))
km_fare = (length_of_journey) * (1.50)
full_fare = float(charge) + float(km_fare)
print (("£") + str(full_fare) + ("0"))

def taxidraw():
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.color("black")
    pen.speed(100)
    distance_back = 400
    distance_to_move = full_fare * 10
    pen.back(distance_back)
    turtle.pensize(10)
    pen.forward(distance_to_move)
    pen.hideturtle()




turtle.setup(8000, 4000)

taxidraw()

turtle.done()

