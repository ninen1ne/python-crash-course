#day 1 of learning python form uncle engineer.
# 26/3/2024

from tkinter import * # from package tkinter import all function 

GUI = Tk() # create GUI and pull function Tk()
GUI.geometry('500x500')

L = Label(GUI, text='Hello World', font=(None,30))
L.pack() # pack คือวางข้อความจากบนลงล่าง
# Label is a message of program (use capital 'L')



GUI.mainloop()

