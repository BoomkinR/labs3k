class Player(object):
    def __init__(self, id, name, money):
        self._id = id
        self._name = "Player "+ str(id)
        self._money = money
        self.score = 0
        self.hand = []
        self.Blind = 0
        self.fold = False

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def money(self):
        return self._money

    def dto(self):
        return {
            "id": self.id,
            "name": self.name,
            "money": self.money
        }

    def add_money(self, money):
        if money <= 0.0:
            raise ValueError("Money has to be a positive amount")
        self._money += money

    def take_blind(self):
        b = self.Blind
        self.Blind = 0
        return b

    def __str__(self):
        return self._name



    def Allin(self):
        self.Blind += self.money
        self._money = 0

    def PushMoney(self, maxblind):
        if maxblind <= self._money:
            self._money -= maxblind - self.Blind
            self.Blind = maxblind
        else:
            self.Allin()

    def Fold(self):
        self.fold = True


