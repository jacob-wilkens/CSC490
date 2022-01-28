from tkinter import *
import math

height = 750
width = 750

##Main Window Declaration
mainWindow = Tk()
##Canvas 1
canvasOne = Canvas(mainWindow, width=width, height= height)
canvasOne.pack()


def create_circle(x, y, r, canvasName, color):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r

    return canvasName.create_oval(x0, y0, x1, y1, outline=color)


def plot_pixel(x, y, canvasName, color):
    return create_circle(x, y, 1, canvasName, color)


corna = 6
cornb = 12
side = 32

for i in range(width):
     for j in range(height):
         x = corna + i * side / 100
         y = cornb + j * side / 100
         c = math.floor(x * x + y * y)
         if c % 5 == 0:
             plot_pixel(i, j, canvasOne, "blue")
         elif c % 5 == 1:
             plot_pixel(i, j, canvasOne, "red")
         elif c % 5 == 2:
             plot_pixel(i, j, canvasOne, "yellow")
         else:
             continue

mainWindow.mainloop()
