import numpy
from tkinter import *
from classes.Magma import Magma


root = Tk()

root.geometry('1080x720+200+50')
label1 = Label(text='Ключ')
key = Text(width=60, height=1)
label2 = Label(text='Текст')
txt = Text(width=117, height=33)


def algoritm1():
    magma = Magma(key.get(1.0,END), txt.get(1.0,END)[:-1])
    txt.delete(1.0,END)
    txt.insert(END, magma.Crypt())

def algoritm2():
    magma = Magma(key.get(1.0, END), txt.get(1.0, END)[:-1])
    txt.delete(1.0, END)
    txt.insert(END, magma.Decrypt())


button = Button(text='crypto', width=12, height=1, command=algoritm1)
button2 = Button(text='decrypt', width=12, height=1, command=algoritm2)

key.place(relx=0.06, rely=0.1)
label1.place(relx=0.11, rely=0.06, anchor='ne')
txt.place(relx=0.06, rely=0.2)
button.place(relx=0.54, rely=0.094)
button2.place(relx = 0.66, rely=0.094)

root.mainloop()
