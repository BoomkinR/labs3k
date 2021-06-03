from tkinter import *
from .Grain import Grain
import string


class Form:

    def algoritm(self, text, key):

        text=text.rstrip()
        stroka = ""
        grain = Grain(text, key)
        for z in grain.binary:
            stroka += (grain.TakeBit(z))
        return grain.ToString(stroka)

