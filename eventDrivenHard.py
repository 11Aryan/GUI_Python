from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
root = tk.Tk()
root.geometry("600x750")
root.title("Registration Form")
root.configure(bg="slate blue");

l1 = Label(root, text="FIRST NAME", bg="slate blue", fg="white").place(x=5,y=10)
t1 = Entry(root).place(x=110,y=10)
rule1 = Label(root, text="(max 30 characters a-z and A-Z)", bg="slate blue", fg="white").place(x=235,y=10)
l2 = Label(root, text="LAST NAME", bg="slate blue", fg="white").place(x=5,y=45)
t2 = Entry(root).place(x=110,y=45)
rule2 = Label(root, text="(max 30 characters a-z and A-Z)", bg="slate blue", fg="white").place(x=235,y=45)

text = tk.StringVar()
text.set("Date:")
l3 = Label(root, text="DATE OF BIRTH", bg="slate blue", fg="white").place(x=5,y=80)
day = ttk.Combobox(root, width = 5, textvariable=text)
day['values'] = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'
                 ,'25','26','27','28','29','30','31')
day.place(x=110,y=80)
day.current()

tex= tk.StringVar()
tex.set("Month:")
month = ttk.Combobox(root, width = 7, textvariable=tex)
month['values'] = (' January',' February',' March',' April',' May',' June',' July',' August',' September',' October',
                    ' November',' December')
month.place(x=165,y=80)
month.current()

te= tk.StringVar()
te.set("Year:")
month = ttk.Combobox(root, width = 6, textvariable=te)
month['values'] = ('2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010',
                   '2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021',)
month.place(x=232,y=80)
month.current()

l4 = Label(root, text="EMAIL ID", bg="slate blue", fg="white").place(x=5,y=115)
t4 = Entry(root).place(x=110,y=115)

l5 = Label(root, text="MOBILE NUMBER", bg="slate blue", fg="white").place(x=5,y=150)
t5 = Entry(root).place(x=110,y=150)
rule5 = Label(root, text="(10 digit number)", bg="slate blue", fg="white").place(x=235,y=150)

l6= Label(root, text="GENDER", bg="slate blue", fg="white").place(x=5,y=185)
rule6 = Label(root, text="Male", bg="slate blue", fg="white").place(x=110,y=185)
r1=Radiobutton(root,bg="slate blue", fg="white").place(x=145,y=185)
rule7 = Label(root, text="Female", bg="slate blue", fg="white").place(x=170,y=185)
r2=Radiobutton(root,bg="slate blue", fg="white").place(x=215,y=185)

l7= Label(root, text="ADDRESS", bg="slate blue", fg="white").place(x=5,y=220)
t7 = Entry(root).place(x=110,y=220,width=230,height=65)

l8 = Label(root, text="CITY", bg="slate blue", fg="white").place(x=5,y=305)
t8 = Entry(root).place(x=110,y=305)
rule8 = Label(root, text="(max 30 characters a-z and A-Z)", bg="slate blue", fg="white").place(x=235,y=305)

l9 = Label(root, text="PIN CODE", bg="slate blue", fg="white").place(x=5,y=340)
t9 = Entry(root).place(x=110,y=340)
rule9 = Label(root, text="(6 digit number)", bg="slate blue", fg="white").place(x=235,y=340)

l10 = Label(root, text="STATE", bg="slate blue", fg="white").place(x=5,y=375)
t10 = Entry(root).place(x=110,y=375)
rule10 = Label(root, text="(max 30 characters a-z and A-Z)", bg="slate blue", fg="white").place(x=235,y=375)

l11 = Label(root, text="COUNTRY", bg="slate blue", fg="white").place(x=5,y=410)
t = tk.StringVar()
t.set("India")
t11 = Entry(root,textvariable=t).place(x=110,y=410)

l12 = Label(root, text="HOBBIES", bg="slate blue", fg="white").place(x=5,y=445)
rule11 = Label(root, text="Drawing", bg="slate blue", fg="white").place(x=110,y=445)
c1 = tk.Checkbutton(root,bg="slate blue", fg="white",onvalue=1,offvalue=0).place(x=160,y=445)
rule12 = Label(root, text="Singing", bg="slate blue", fg="white").place(x=180,y=445)
c2 = tk.Checkbutton(root,bg="slate blue", fg="white", onvalue=1, offvalue=0).place(x=230,y=445)
rule13 = Label(root, text="Dancing", bg="slate blue", fg="white").place(x=250,y=445)
c3 = tk.Checkbutton(root,bg="slate blue", fg="white", onvalue=1, offvalue=0).place(x=300,y=445)
rule14 = Label(root, text="Sketching", bg="slate blue", fg="white").place(x=320,y=445)
c4 = tk.Checkbutton(root,bg="slate blue", fg="white", onvalue=1, offvalue=0).place(x=375,y=445)
rule15 = Label(root, text="Others", bg="slate blue", fg="white").place(x=110,y=470)
c5 = tk.Checkbutton(root,bg="slate blue", fg="white", onvalue=1, offvalue=0).place(x=150,y=470)
t15 = Entry(root).place(x=175,y=470)

l13 = Label(root, text="QUALIFICATION", bg="slate blue", fg="white").place(x=5,y=510)
l14 = Label(root, text="SI.No. Examination", bg="slate blue", fg="white").place(x=110,y=510)
l15 = Label(root, text="Board", bg="slate blue", fg="white").place(x=258,y=510)
l16 = Label(root, text="Percentage", bg="slate blue", fg="white").place(x=375,y=510)
l17 = Label(root, text="Year of Passing", bg="slate blue", fg="white").place(x=488,y=510)

l18 = Label(root, text="1          Class X", bg="slate blue", fg="white").place(x=110,y=528)
t16 = Entry(root).place(x=215,y=530)
l19 = Label(root, text="2          Class XII", bg="slate blue", fg="white").place(x=110,y=552)
t17 = Entry(root).place(x=215,y=553)
l20 = Label(root, text="3          Graduation", bg="slate blue", fg="white").place(x=110,y=574)
t18 = Entry(root).place(x=215,y=576)
l21 = Label(root, text="4          Masters", bg="slate blue", fg="white").place(x=110,y=597)
t19 = Entry(root).place(x=215,y=599)
rule16 = Label(root, text="(10 char max)", bg="slate blue", fg="white").place(x=240,y=618)

t16 = Entry(root).place(x=342,y=530)
t16 = Entry(root).place(x=342,y=553)
t16 = Entry(root).place(x=342,y=576)
t16 = Entry(root).place(x=342,y=599)
rule17 = Label(root, text="(upto 2 decimal)", bg="slate blue", fg="white").place(x=360,y=618)

t16 = Entry(root).place(x=469,y=530)
t16 = Entry(root).place(x=469,y=553)
t16 = Entry(root).place(x=469,y=576)
t16 = Entry(root).place(x=469,y=599)

l22 = Label(root, text="COURSES\nAPPLIED FOR", bg="slate blue", fg="white").place(x=5,y=655)
rule18 = Label(root, text="BCA", bg="slate blue", fg="white").place(x=110,y=665)
r3=Radiobutton(root,bg="slate blue", fg="white").place(x=137,y=665)
rule19 = Label(root, text="B.Com", bg="slate blue", fg="white").place(x=160,y=665)
r4=Radiobutton(root,bg="slate blue", fg="white").place(x=200,y=665)
rule20 = Label(root, text="B.Sc", bg="slate blue", fg="white").place(x=220,y=665)
r5=Radiobutton(root,bg="slate blue", fg="white").place(x=247,y=665)
rule21 = Label(root, text="B.A", bg="slate blue", fg="white").place(x=267,y=665)
r6=Radiobutton(root,bg="slate blue", fg="white").place(x=289,y=665)

def submit():
    msg = messagebox.showinfo("Registration Form","The form is submitted successfully!")
def reset():
    msg = messagebox.showinfo("Registration Form","The form is reset!")
b1=tk.Button(root, text='Submit', width=6,command=submit).place(x=258,y=720)
b2=tk.Button(root, text='Reset', width=5,command=reset).place(x=315,y=720)

root.mainloop()
