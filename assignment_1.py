from tkinter import *
import math

root = Tk()
myCanvas = Canvas(root, height=500, width=500)
myCanvas.pack()


def create_circle(x, y, r, canvasName):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)


def plot_pixel(x, y, canvasName):
    return create_circle(x, y, 1, canvasName)


corna = 10
cornb = 10
side = 10

for i in range(500):
    for j in range(500):
        x = corna + i * side / 100
        y = cornb + j * side / 100
        c = math.floor(x * x + y * y)
        if c % 2 == 0:
            plot_pixel(i, j, myCanvas)

root.mainloop()
