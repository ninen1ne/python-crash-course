# GUIBasic2-expense.py
# Norawee- 28/3/2024

from tkinter import *
from tkinter import ttk # ttk is theme of Tk
import csv # csv file use for record list of items and expense.



GUI = Tk()
GUI.title("record expense program- by Norawee")
GUI.geometry('500x300+500+50')


# B1 = Button(GUI, text='Hello')
# B1.pack(ipadx=50, ipady=20) # .pack() ติดปุ่มเข้ากับ GUI หลัก
# ipad => internal paddding in x or y coordinate like html box padding
# is space between content and border.

F1 = Frame(GUI) 
F1.place(x=100, y=50)


def save(event=None):
    """"""
    expense = v_expense.get() # .get() ดึงข้อมูลจาก v_expense = StringVar() แล้วเก็บในตัวแปร expense
    price = v_price.get()
    print(f'รายการ: {expense} ราคา {price} บาท')
    # clear ข้อมูลเก่า
    v_expense.set('')
    v_price.set('')

    # เป็นการบันทึกข้อมูลลง csv 
    with open('expense_record.csv', 'a', encoding='utf-8', newline='') as f:
        # with คือการสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
        # 'a' => append การเอาไปต่อท้ายบันทึกเรื่อยๆ เพิ่มข้อมูลลงไปต่อจากข้อมูลเก่า
        # newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
        file_writer = csv.writer(f) # สร้าง function สำหรับเขียนข้อมูล
        data = [expense, price]
        file_writer.writerow(data)

    # ทำให้ cursor กลับไปตำแหน่งช่องกรอก E1
    E1.focus()

GUI.bind('<Return>', save) # ต้องเพิ่มใน def ว่า Save(event=None) ด้วย


FONT1 = (None,20) # None ปลี่ยนเป็น 'Angsana New'

#---------text1-----------------
Label = ttk.Label(F1, text="รายการค่าใช้จ่าย", font=FONT1).pack()

v_expense = StringVar() # StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1, textvariable=v_expense, font=FONT1)
E1.pack()
#---------------------

#---------text2-----------------
Label = ttk.Label(F1, text="ราคา (บาท)", font=FONT1).pack()

v_price = StringVar() # StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1, textvariable=v_price, font=FONT1)
E2.pack()
#---------------------


B2 = ttk.Button(F1, text='Save', command=save)
B2.pack(ipadx=50, ipady=20, pady=20)



GUI.mainloop()
