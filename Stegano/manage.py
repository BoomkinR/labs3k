from tkinter import *
from tkinter import filedialog
import tkinter.font as tkFont
from classes.Stegano import Stegano
import os

root = Tk()
root.geometry('1080x720+130+35')

label1 = Label(text='Слово для зашифровки')
Key = Text(width=35, height=1)
text1 = Text(width=62, height=40, )
text2 = Text(width=62, height=40)
fontStyle = tkFont.Font(family="Times New Roman", size=1)


def Hide():
    stegano = Stegano(Key.get(1.0, END), text1.get(1.0, END))
    text2.delete(1.0, END)
    text2.insert(1.0, stegano.RU_ENG())
def Add_space():
    stegano = Stegano(Key.get(1.0, END), text1.get(1.0, END))
    text2.delete(1.0, END)
    text2.insert(1.0, stegano.EndSpace())
def Double_spc():
    stegano = Stegano(Key.get(1.0, END), text1.get(1.0, END))
    text2.delete(1.0, END)
    text2.insert(1.0, stegano.DoubleSpace())
def Simbol_add():
    stegano = Stegano(Key.get(1.0, END), text1.get(1.0, END))
    text2.delete(1.0, END)
    text2.insert(1.0, stegano.Simbol())


Ru_Eng = Button(text='Русс-> Англ', width=15, height=1, command = Hide)
End_space = Button(text='space  конце', width=15, height=1, command = Add_space)
Double_space= Button(text='space  x2', width=15, height=1, command = Double_spc)
Simbol_button = Button(text='Неразрывная связка', width=15, height=1, command = Simbol_add)

label1.place(relx=.07, rely=.03, anchor="c", bordermode=OUTSIDE)
Key.place(relx=.01, rely=.05)
text1.place(relx=.01, rely=.1)
text2.place(relx=.5, rely=.1)
Ru_Eng.place(relx=.5, rely=0.05)
End_space.place(relx=.35, rely=0.05)
Double_space.place(relx = .65, rely = 0.05)
Simbol_button.place(relx=0.8, rely = 0.05)

root.mainloop()
