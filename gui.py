tkinter import *

master = Tk()

w = Canvas(master, width=40, height=60)

w.pack()

canvas_height=20

canvas_width=200

y = int(canvas_height / 2)

w.create_line(0, y, canvas_width, y )

mainloop()

from tkinter import *

from tkinter import messagebox

top = Tk()

C = Canvas(top, bg = "blue", height = 250, width = 300)

coord = 10, 50, 240, 210

arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")

line = C.create_line(10,10,200,200,fill = 'white')

C.pack()

top.mainloop()
