# hello.py

from sys import *
from Tkinter import HIDDEN, NORMAL, Tk, Canvas
import turtle
import mod.data as me


print(version_info)
me.hello()
a = me.info("JAeHO")
a.hello()

root = Tk()
c = Canvas(root, width=500, height = 400)
c.configure(bg='dark green', highlightthickness=0)
c.pack()


painter = turtle.RawTurtle(c)
painter.pencolor("blue")
for i in range(10):
    painter.forward(10)
    painter.left(123) # Let's go counterclockwise this time 
    
painter.pencolor("red")
for i in range(10):
    painter.forward(100)
    painter.left(123)

root.mainloop()


