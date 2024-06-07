# This program calculate price of items and record in csv.

# 29/3/2024

from tkinter import *
from tkinter import ttk
from datetime import datetime
import csv

GUI = Tk()
GUI.title("บันทึกรายการสินค้า")
GUI.geometry('500x500+500+50') 
'''
Argument in parenthesis first refer to width next is height next is how far from 
left side of screen in x coordinate last one is how far from top in y coordinate. 
''' 

F1 = Frame(GUI)
F1.place(x=100, y=50) #.place() allow you to choose any position to set F1.

FONT1 = (None, 20) # setting default font and font size of gui.

# Create dictionary for use in record.
days = {
    'Mon': 'จันทร์',
    'Tue': 'อังคาร',
    'Wed': 'พุธ',
    'Thu': 'พฤหัสบดี',
    'Fri': 'ศุกร์',
    'Sat': 'เสาร์',
    'Sun': 'อาทิตย์',
    }

def save(event=None):
    """ This function use for save the record in csv file."""
    expense = v_expense.get()
    price = v_price.get()
    quantity = v_quantity.get()
    total = int(price) * int(quantity)
    today = datetime.now().strftime('%a')
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # access dictionary to tell date at the moment.
    dt = days[today] + '-' + dt 
    record = "record at: " + str(dt)
    print(f"{record}, ชนิดสินค้า: {expense}, ราคา {price} บาท จำนวน {quantity} ชิ้น รวมเป็นเงิน {total} บาท")
    v_price.set('')
    v_expense.set('')
    v_quantity.set('')
    # .set() is set variable to what inside parenthesis in this case => ('') is an empty value.  

    # This section will save record in csv file.
    with open('yolle_shop.csv', 'a', encoding='utf-8', newline='') as f:
        file_writer = csv.writer(f)
        data = [record, expense, price, quantity]
        file_writer.writerow(data)

    E1.focus()

GUI.bind('<Return>', save)
          
#-------------------------------------------------------------
# Create label, entry and button.
label = ttk.Label(F1, text='product', font=FONT1).pack()

v_expense = StringVar()
E1 = ttk.Entry(F1, textvariable=v_expense, font=FONT1)
E1.pack()

label = ttk.Label(F1, text='quantity (piece)', font=FONT1).pack()

v_quantity = StringVar()
E2 = ttk.Entry(F1, textvariable=v_quantity, font=FONT1)
E2.pack()

label = ttk.Label(F1, text='price (baht)', font=FONT1).pack()

v_price = StringVar()
E2 = ttk.Entry(F1, textvariable=v_price, font=FONT1)
E2.pack()

B1 = ttk.Button(F1, text='Save', command=save)
B1.pack(ipadx=50, ipady=20, pady=20)

# .mainloop() tell program to running untill we close it.
GUI.mainloop()