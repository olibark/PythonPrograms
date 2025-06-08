import tkinter
import time

from matplotlib.backend_bases import button_press_handler

root = tkinter.Tk()
root.title("Missile")
root.geometry("1000x1000")

canvas = tkinter.Canvas(root, width=1000, height=950, background="black")
canvas.pack(side=tkinter.TOP, expand=True)

class Missile():
    def __init__(self):
        self.missile_id = None
        self.image = tkinter.PhotoImage(file= "/Users/oliverbarkham/Documents/Python_programs/missile/RedCircle.png")
    
    def drawMissile(self):
        self.missile_id = canvas.create_image(500, 500, image= self.image)

    def moveMissile(self):
        if self.missile_id:
            canvas.move(self.missile_id, -1, 1)#thing, -1 left, 1down
            canvas.update()
    
    def startMovement(self):
        for i in range(1000):
            self.moveMissile()


def move_up(event):
    missile.moveMissile(0, -10)

def move_down(event):
    missile.moveMissile(0, 10)

def move_left(event):
    missile.moveMissile(-10, 0)

def move_right(event):
    missile.moveMissile(10, 0)

root.bind("<w>", move_up)
root.bind("<s>", move_down)
root.bind("<a>", move_left)
root.bind("<d>", move_right)

missile = Missile()
missile.drawMissile()

launch_button = tkinter.Button(
    root,  
    text="Launch Missile",
    command=missile.startMovement,
    width=15,  
    height=2  
)
launch_button.pack(side=tkinter.TOP, pady=10, anchor=tkinter.CENTER)

root.mainloop()