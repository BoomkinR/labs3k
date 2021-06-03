from .Player import Player
from .Round import Round
from .Bot import Bot
from .Table import Table
import pygame


class Game:

    def __init__(self, win):
        self.win = win
        self.StartMoney = 1500
        self.Place = 6  # под замену
        self.PLAYERS = []
        self.table = Table()
        self._update = None



    def AddPlayer(self, ID):
        if len(self.PLAYERS) <= self.Place:
            self.PLAYERS.append(Player(ID, 'name', self.StartMoney))
            self.table.place.append(self.PLAYERS[-1])
        else:
            print('Все места за столом заняты')

    def AddBot(self, ID):
        if len(self.PLAYERS) <= self.Place:
            self.PLAYERS.append(Bot(ID, 'name', self.StartMoney))
            self.table.place.append(self.PLAYERS[-1])
        else:
            print('Все места за столом заняты')




