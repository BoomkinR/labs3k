import random
from .Card_class import Card


class Deck(object):

    def __init__(self):
        try:
            self.cards = [Card(rank, suit) for rank in range(2, 15) for suit in range(0, 4)]
            random.shuffle(self.cards)
        except :
            print("wtf")

    def PushCard(self):
        discard = self.cards[-1]
        del self.cards[-1]
        return discard

    def take_name(self, card):
        return str(card.suit) + str(card.rank)+".jpg"

