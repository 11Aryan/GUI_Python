import tkinter
from tkinter import *
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = 'Event'
)
mycursor = mydb.cursor()

root = Tk()
root.geometry("400x400")

regno= StringVar()
name = StringVar()
dept = StringVar()
age = StringVar()
male= IntVar()
female = IntVar()

regno_label = Label(root,text="Reg No.").place(x=2,y=10)
regno_entry = Entry(root,textvariable=regno).place(x=70,y=10)

name_label = Label(root,text="Name :").place(x=2,y=50)
name_entry = Entry(root,textvariable=name).place(x=70,y=50)

dept_label = Label(root,text="Dept").place(x=2,y=90)
dept_entry = Entry(root,textvariable=dept).place(x=70,y=90)

gender_label = Label(root,text="Gender").place(x=2,y=130)
male_check = Checkbutton(root,text="Male",variable=male,onvalue=1,offvalue=0).place(x=100,y=130)
female_check = Checkbutton(root,text="Female",variable=female,onvalue=1,offvalue=0).place(x=180,y=130)

age_label = Label(root,text="Age").place(x=2,y=170)
spin = Spinbox(root,textvariable=age, from_=1,to=25).place(x=70,y=170)

def insert():
  if male.get()==1:
    s="Male"
  else:
    s="Female"
  q="insert into gui3 values('{}','{}','{}','{}',{})".format(regno.get(),name.get(),dept.get(),s,int(age.get()))
  mycursor.execute(q)
  mydb.commit()
def delete():
  q="delete from gui3 where name='{}'".format(name.get())
  mycursor.execute(q)
  mydb.commit()
def select():
  q="select * from gui3"
  mycursor.execute(q)
  data=mycursor.fetchall()
  print(data)


insert_button = Button(root,text="Insert",command=insert).place(x=5,y=200)
update_button = Button(root,text="Update").place(x=100,y=200)
delete_button = Button(root,text="Delete",command=delete).place(x=5,y=250)
select_button = Button(root,text="Select",command=select).place(x=100,y=250)

root.mainloop()
