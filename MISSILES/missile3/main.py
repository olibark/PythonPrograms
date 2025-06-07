import tkinter as tk
from turtle import xcor


class Missile:
    def __init__(self, canvas, xCo, yCo):
        self.canvas = canvas
        self.xCo = xCo
        self.yCo = yCo
        self.missile = canvas.create_circle(xCo, yCo, 6, fill= 'red')
        self.canvas.move(self.missile, xCo, yCo)
        self.canvas.bind_all('<KeyPress>', self.key_press)
        self.canvas.bind_all('<KeyRelease>', self.key_release)
        self.canvas.bind_all('<Motion>', self.mouse_move)
        self.canvas.bind_all('<Button-1>', self.mouse_click)
        self.canvas.bind_all('<ButtonRelease-1>', self.mouse_release)
        self.canvas.bind_all('<Button-3>', self.mouse_right_click)
        self.canvas.bind_all('<ButtonRelease-3>', self.mouse_right_release)
        self.canvas.bind_all('<Button-2>', self.mouse_middle_click)
        self.canvas.bind_all('<ButtonRelease-2>', self.mouse_middle_release)
        self.canvas.bind_all('<Double-Button-1>', self.mouse_double_click)
        self.canvas.bind_all('<Double-Button-2>', self.mouse_double_middle_click)
        self.canvas.bind_all('<Double-Button-3>', self.mouse_double_right_click)
        self.canvas.bind_all('<Enter>', self.mouse_enter)
        self.canvas.bind_all('<Leave>', self.mouse_leave)
        self.canvas.bind_all('<FocusIn>', self.focus_in)
        self.canvas.bind_all('<FocusOut>', self.focus_out)
        self.canvas.bind_all('<Configure>', self.configure)
        self.canvas.bind_all('<Expose>', self.expose)
        self.canvas.bind_all('<Key>', self.key)
        self.canvas.bind_all('<KeyRelease>', self.key_release)
        self.canvas.bind_all('<KeyPress>', self.key_press)
    def key_press(self, event):
        if event.keysmatch('Up'):
            self.canvas.move(self.missile, 0, -5)
        elif event.keysmatch('Down'):
            self.canvas.move(self.missile, 0, 5)
        elif event.keysmatch('Left'):
            self.canvas.move(self.missile, -5, 0)
        elif event.keysmatch('Right'):  
            self.canvas.move(self.missile, 5, 0)

root = tk.Tk()
root.title("Missile")
root.geometry("800x600")
canvas = tk.Canvas(root, width=800, height=600, bg='black')
canvas.pack()

main = tk.mainloop()
