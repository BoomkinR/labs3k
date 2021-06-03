from .Player import Player
from .Deck import Deck
from .Combination import Combination, PokerMath
import random


class Bot(Player):

    def __init__(self, id, name, money):
        self._id = id
        self._name = "Bot" + str(id)
        self._money = money
        self.score = 0
        self.hand = []
        self.Blind = 0
        self.fold = False
        self.Blef = False
        """
        1 - fold
        2 - check / koll
        3 - raise
        bank - проценты blind / bank table
        
        """

    def Desigion(self, stadium, cards, bank, blind):  # стадия игры + карты, делаем анализ математики и го
        if stadium == 1:
            if random.randint(0, 100) < 8:
                self.Blef = True
            x = PokerMath(cards)
            ret = self.Return(x.assessment(), bank, blind)
        elif stadium == 2:
            x = PokerMath(cards)
            ret = self.Return(x.Hand_assessment(stadium), bank, blind)
        elif stadium == 3:
            x = PokerMath(cards)
            ret = self.Return(x.Hand_assessment(stadium), bank, blind)
        else:
            x = PokerMath(cards)
            ret = self.Return(x.Hand_assessment(stadium), bank, blind)
            self.Blef = False
        return ret

    def Return(self, des, bank, blind):
        if not self.Blef:
            if bank < blind * 4:
                if des < 10:
                    if blind ==0 :
                        return 2
                    elif random.randint(0, 100) < 80:
                        if self.Blind * 2 >= blind:
                            return 2
                        else:
                            return 1
                    else:
                        return 1
                else:
                    bet = [2, random.randint(2, 3) * blind]
                    return bet[random.randint(0, 1)]
            else:
                if des <= 10:
                    return 1
                if 10 < des <= 50:
                    if random.randint(0, 100) > (des - int(blind / bank / 4 * 100)):
                        return 1
                    elif random.randint(0, 100) < (des - int(blind / bank / 4 * 100)):
                        return 2
                    else:
                        return random.randint(2, 4) * blind
                if des > 50:
                    if blind / bank >= 0.5:
                        if random.randint(1, 11) > des:
                            return 2
                        else:
                            bet = random.randint(0, 10)
                            if bet < 4:
                                return 999999
                            if bet < des // 10:
                                return int(bank + 0.7)
                            else:
                                return bank
        else:
            print("blef")
            bet = [2, 2 * blind, 3 * blind, 0 / 5 * bank, 999999]
            return bet[random.randint(0, len(bet) - 1)]
