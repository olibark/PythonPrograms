import tkinter as tk
import math
running  = True 
# Create the main window
root = tk.Tk()
root.title("Ray")

LineLength = 500
LineStartX = 700
LineEndX = 700




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


def draw_line(LineX, LineY, LineEndY, LineEndX):
    canvas.create_line(LineX, LineY, LineEndX, LineEndY, fill="white", width= 30)





    

while running:
    #UP
    for LineStartY in range(512, 0, -10):
        canvas.delete("all") 
        draw_line(LineStartX, LineStartY, LineLength + LineStartY, LineEndX)
        draw_rays()
        canvas.update() 
        #root.after(50)  # Pause for 50 milliseconds
    #DOWN
    for LineStartY in range(0, 512, 10):
        canvas.delete("all")
        draw_line(LineStartX, LineStartY, LineLength + LineStartY, LineEndX)
        draw_rays()
        canvas.update()  
        #root.after(50)  # Pause for 50 milliseconds
    


root.mainloop()


