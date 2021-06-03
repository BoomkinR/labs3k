import random
import pygame
from .Player import Player


class Table(object):
    # Button +1 = small blind
    # Button +2 = Big blind

    def __init__(self):
        self.buttonId = 0
        self.bank = 0
        self.distrib = []
        self.place = []
        self.Cordinates = [(450, 290), (530, 290), (610, 290), (690, 290), (770, 290)] # координаты карт
        self.SmallBlind = 25