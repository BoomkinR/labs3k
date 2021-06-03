import os
import random
import datetime
from randomtimestamp import randomtimestamp


class Generator():
    def __init__(self):
        self.num = int(input('Введите количество строк:'))
        self.goods = 129
        self.customers = 240
        self.List = []

    def Generate_Leads(self):
        for i in range(self.num):
            strok = "insert into leads (date_add, Good, SellPrice, customerid) values ('"
            strok += self.randomdate() + "' , "
            strok += str(random.randint(1, self.goods)) + ","
            strok += str(self.Takeprice(random.randint(1, self.goods)) )+ ","
            strok += str(random.randint(1, self.customers) )+ ")"
            self.List.append(strok)
            strok = ''
        f = open('query.txt', 'w')
        for item in self.List:
            f.write(item + '\n')


    def Takeprice(self, n):
        if n < 45:
            return 2950
        elif 45 <= n < 56:
            return 3300
        elif 56 <= n < 66:
            return 1750
        elif 66 <= n < 100:
            return 2950
        else:
            return 5990

    def randomdate(self):
        date = randomtimestamp(start_year=2020, text = False)
        return date.strftime("%Y-%m-%d")

gen = Generator()
gen.Generate_Leads()
input()