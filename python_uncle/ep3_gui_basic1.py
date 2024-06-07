# GUIBasic1.py
# Norawee- 28/3/2024

from tkinter import *
from tkinter import ttk
# ttk is theme of Tk


GUI = Tk()
GUI.geometry('500x300+500+50')


# B1 = Button(GUI, text='Hello')
# B1.pack(ipadx=50, ipady=20) # .pack() ติดปุ่มเข้ากับ GUI หลัก
# ipad => internal paddding in x or y coordinate like html box padding
# is space between content and border.

F1 = Frame(GUI) 
F1.place(x=150, y=50)


def hello():
    print("Hello")



B2 = ttk.Button(F1, text='Hello', command=hello)
B2.pack(ipadx=50, ipady=20)



GUI.mainloop()
