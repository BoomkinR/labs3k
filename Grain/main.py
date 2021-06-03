import numpy
from tkinter import *
from classes.Form import Form

root = Tk()
form = Form()
root.geometry('1080x720+200+50')
label1 = Label(text='Ключ')
key = Text(width=60, height=1)
label2 = Label(text='Текст')
txt = Text(width=117, height=33)


def algoritm():
    shifr = form.algoritm(txt.get(1.0, END), key.get(1.0, END))
    f = open('text.txt','w',encoding='utf-8')
    print(shifr)
    f.write(shifr)
    f.close()


button = Button(text='Расшифровать', width=12, height=1, command=algoritm)

key.place(relx=0.06, rely=0.1)
label1.place(relx=0.11, rely=0.06, anchor='ne')
txt.place(relx=0.06, rely=0.2)
button.place(relx=0.54, rely=0.094)

root.mainloop()
