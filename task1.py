#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""


import tkinter as tk 
from tkinter import *
win = tk.Tk()

def binary_to_decimal(binary):
    # binary is a tuple of length 8
    # return value as an integer decimal
    decimal = 0 
    for x in range(8):
        if binary[x]==1:
            decimal += (2**x)
    
    return decimal 

def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's
    binary=[0,0,0,0,0,0,0,0]
    num = [128,64,32,16,8,4,2,1]
    for x in range(8):
        if decimal- num[x] >= 0:
            binary[x] = 1
            decimal -=num[x]
    return binary


def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes
    decimal = int(entry.get())
    binary = decimal_to_binary(decimal)
    for x in range(8):
        if binary[x] == 1:
            cb[x].select()
        else:
            cb[x].deselect()


def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 tht has 1's and 0's
    # this tuple willu be sed a san input parameter for binary_to_decimal and the result updated
    # in the entry box
    binary = []
    for x in range(8):
        binary.append(a[x].get())
    binary.reverse()
    decimal = binary_to_decimal(binary)
    entry.delete(0,END)
    entry.insert(0, decimal)
    return decimal


a = []
for x in range(8):
    a.append(IntVar())
    a[x].set(0)


cb=[]

state = IntVar()
state.set(0)

buttonf = Frame()
checkf = Frame()
label1 = Label(text= "Binary/Decimal Converter")
b1 = Button(master= buttonf, text="Convert to Binary", command=get_binary)
b2 = Button(master = buttonf, text="Convert to Decimal",command=get_decimal)
entry = Entry(width = 20,)

for x in range(8):
    cb.append(Checkbutton(master=checkf, variable = a[x]))

label1.pack()
checkf.pack()
buttonf.pack()
for x in range(8):
    cb[x].pack(side=LEFT)
b1.pack(side = LEFT)
b2.pack(side = LEFT)
entry.pack()


win.mainloop()

