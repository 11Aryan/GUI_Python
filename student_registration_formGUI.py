from tkinter import *


top = Tk()
top.geometry("450x300")

Regno = Label(top, text="Regno").place(x=40, y=60)

Regno_entry = Entry(top, width=30).place(x=110, y=60)


Name = Label(top, text="Name").place(x=40, y=90)
Name_entry = Entry(top, width=30).place(x=110, y=90)

Dept = Label(top, text="Dept").place(x=40, y=120)
Dept_entry = Entry(top, width=30).place(x=110, y=120)

Gender = Label(top, text="Gender").place(x=40, y=150)
var = IntVar()
male = Radiobutton(top, text="Male", variable=var, value=1).place(x=110, y=150)
female = Radiobutton(top, text="Female", variable=var, value=2).place(x=170, y=150)

Age = Label(top, text="Age").place(x=40, y=180)
sp = Spinbox(top, from_=0, to=20).place(x=110, y=180)


Insert = Button(top, text="Insert").place(x=40, y=210)
Insert = Button(top, text="Update").place(x=120, y=210)
Insert = Button(top, text="Delete").place(x=40, y=250)
Insert = Button(top, text="Select").place(x=120, y=250)
top.mainloop()
