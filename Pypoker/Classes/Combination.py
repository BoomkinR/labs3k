from .Card_class import Card
from .Deck import Deck
import collections


class Combination(object):
    COMBOS = {
        0: "Hight Card",
        1: "Pare",
        2: "2 Pares",
        3: "Trips",
        4: "Straight",
        5: "Flush",
        6: "Full House",
        7: "Kare",
        8: "Straight Flush",
    }

    def __init__(self, cards, lowest_rank=2):
        # Sort the list of cards in a descending order
        self._sorted = sorted(cards, key=lambda cards: cards.rank, reverse=True)
        self._lowest_rank = lowest_rank
        self.FlushScore = []
        self.CardScore = []
        self.MaxCombo = self.Checkcombo()

    def _group_by_ranks(self):
        # Group cards by their ranks.
        # Returns a dictionary keyed by rank and valued by list of cards with the same rank.
        # Each list is sorted by card values in a descending order.
        ranks = collections.defaultdict(list)
        for card in self._sorted:
            ranks[card.rank].append(card)
        return ranks

    def _x_sorted_list(self, x):
        """
        If x = 2 returns a list of pairs, if 3 a list of trips, ...
        The list is sorted by sublist ranks.
        If x = 2 and there is a pair of J and a pair of K, the pair of K will be the first element of the list.
        Every sublist is sorted by card suit.
        If x = 4 and the there is a quads of A's, then the quad will be sorted: A of hearts, A of diamonds, ...
        :param x: dimension of every sublist
        :return: a list of a list of cards
        """
        return sorted(
            (cards for cards in self._group_by_ranks().values() if len(cards) == x),
            key=lambda cards: cards[0].rank,
            reverse=True
        )

    def Card_score(self, cards):
        score = 0

        for i in range(5):
            score += cards[i].rank
        return score + self.MaxCombo * 100

    def _merge_with_cards(self, score_cards):
        karta = score_cards + [card for card in self._sorted if card not in score_cards]
        return karta

    def Checkcombo(self):
        if self.Flush():
            if self.Straight() and self.Card_score(self.FlushScore) == self.Card_score(self.CardScore):
                return 8
            elif not self.Full_house():
                return 5
            else:
                return 6
        if self.Straight():
            return 4
        if self.Quads():
            return 7
        if self.Full_house():
            return 6
        if self.Trips():
            return 3
        else:
            return self.Pare()

    def Flush(self):
        flag = False
        scorecard = []
        ranks = collections.defaultdict(list)
        for card in self._sorted:
            i = card.suit
            ranks[i].append(card)
        for cards in ranks.values():
            if len(cards) >= 5:
                flag = True
                for i in range(5):
                    self.FlushScore.append(cards[i])
        return flag

    def Straight(self):
        sorted_cards = self._sorted
        if len(sorted_cards) < 5:
            return None

        straight = [sorted_cards[0]]

        for i in range(1, len(sorted_cards)):
            if sorted_cards[i].rank == sorted_cards[i - 1].rank - 1:
                straight.append(sorted_cards[i])
                if len(straight) == 5:
                    self.CardScore = straight
                    return True
            elif sorted_cards[i].rank != sorted_cards[i - 1].rank:
                straight = [sorted_cards[i]]

        # The Ace can go under the lowest rank card
        if len(straight) == 4 and sorted_cards[0].rank == 14 and straight[-1].rank == self._lowest_rank:
            straight.append(sorted_cards[0])
            self.CardScore = straight
            return True
        # straight = scorecard
        return False

    def Pare(self):
        pair_list = self._x_sorted_list(2)
        try:
            score_card = self._merge_with_cards(pair_list[0] + pair_list[1])[0:5]
            self.CardScore = score_card
            return 2
        except IndexError:
            try:
                score_card = self._merge_with_cards(pair_list[0])[0:5]
                self.CardScore = score_card
                return 1
            except IndexError:
                self.CardScore = self._sorted[0:5]
                return 0

        return False

    def Trips(self):
        trips_list = self._x_sorted_list(3)
        try:
            score_card = self._merge_with_cards(trips_list[0])[0:5]
            self.CardScore = score_card
            return True
        except IndexError:
            return False

    def Full_house(self):
        trips_list = self._x_sorted_list(3)
        pair_list = self._x_sorted_list(2)
        try:
            score_card = self._merge_with_cards(trips_list[0] + pair_list[0])[0:5]
            self.CardScore = score_card
            return True
        except IndexError:
            return False

    def Quads(self):
        quads_list = self._x_sorted_list(4)
        try:
            score_card = self._merge_with_cards(quads_list[0])[0:5]
            self.CardScore = score_card
            return True
        except IndexError:
            return False


class PokerMath:

    def __init__(self, cards):
        self.win_pc = 0
        self.deck = Deck()
        self._sorted = sorted(cards, key=lambda cards: cards.rank, reverse=True)

    # оценка стартовой руки
    def assessment(self):
        if len(self._sorted) == 2:
            if 24 < self.Check_rankscore() < 29:
                return 80  # гиганты = 80%
            elif self._sorted[0].rank == self._sorted[1].rank:
                return 70
            elif self._sorted[0].rank == self._sorted[1].rank + 1:
                return 60
            elif self._sorted[0].rank - self._sorted[1].rank < 3:
                return 50
            elif self._sorted[0].rank + self._sorted[1].rank > 20:
                return 40
            else:
                return 9
    # flop turn river
    def Hand_assessment(self,stad):
        combo = Combination(self._sorted)
        return combo.Checkcombo()*10 + 20 -stad*7

    def Check_rankscore(self):
        samba = 0
        for i in self._sorted:
            samba += i.rank
        return samba
