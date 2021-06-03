import pygame
import os
import random
from .Bot import Bot
from .Deck import Deck
from .GUI import TextBox
from .Combination import Combination


class Round:
    def __init__(self, players, table, win, butons, update_screen, sitter):
        self.players = players  # класс игрока + аватарка + координаты
        self.table = table
        self.win = win
        self.deck = Deck()
        self.x, self.y = pygame.display.get_surface().get_size()
        self.butons = butons
        self.update_screen = update_screen
        self.sitter = sitter
        self.MaxBlind = table.SmallBlind * 2
        self.textbox = TextBox(500, 500, 124, 45, self.win)
        self.STADY = {
        1: "Preflop",
        2: "Flop",
        3: "Turn",
        4: "River",
    }
        self.Show = False

    def StartRound(self):
        stady = 1
        # Раздача карт ready
        for i in range(len(self.players) * 2):
            self.players[i % len(self.players)][0].hand.append(self.deck.PushCard())
        self.HandCard()
        # блайнды м\б
        self.players[(self.table.buttonId + 1) % len(self.players)][0].PushMoney(self.table.SmallBlind)
        self.players[(self.table.buttonId + 2) % len(self.players)][0].PushMoney(self.table.SmallBlind * 2)
        # 4 стадии игры : префлоп флоп терн ривер
        while stady <= 4:
            active_player = 0
            for i in self.players:
                if i[0].fold == False:
                    active_player += 1
            if active_player > 1:
                print(self.STADY[stady]) # PRINT STADY
                self.DoAction(stady)
            for i in range(len(self.players)):
                self.table.bank += self.players[i][0].take_blind()  # все ставки в общий банк стола
            stady += 1
            self.MaxBlind = 0
        # если игроков больше одного, определить кто победил, иначе тот кто остался
        if active_player < 2:
            for i in self.players:
                if i[0].fold == False:
                    i[0].add_money(self.table.bank)
        else:
            self.Show =True
            self.Update_Table(
                    (self.players[0][2][0] - 38,
                     self.players[0][2][1]))
            self.WhoWin()
            self.Show = False

    def DoAction(self, sta):
        startpos = 0
        if sta == 1:
            startpos = 2
        elif sta == 2:
            for i in range(3):
                self.table.distrib.append(self.deck.PushCard())
            # Open flop
        elif sta == 3:
            self.table.distrib.append(self.deck.PushCard())
        else:
            self.table.distrib.append(self.deck.PushCard())
        # Open river
        clock = pygame.time.Clock()
        enable = False
        index_raise = -10
        while not enable:
            for i in range(len(self.players)):  # переход хода к игроку, и ожидание действия
                index = (self.table.buttonId + startpos + i + 1) % len(self.players)
                self.Update_Table(
                    (self.players[index][2][0] - 38,
                     self.players[index][2][1]))


                print("Ход игрока "+ str(self.players[index][0]))
                action = False
                if index != index_raise:
                    if type(self.players[index][0]) is not Bot and not self.players[index][0].fold and self.players[index][0].money > 0:
                        while not action:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                            mouse = pygame.mouse.get_pos()
                            click = pygame.mouse.get_pressed()
                            self.Update_Table(
                                (self.players[index][2][0] - 38,
                                 self.players[index][2][1]))

                            # чек koll
                            if self.butons[0].x < mouse[0] < self.butons[0].x + self.butons[0].width and self.butons[0].y < \
                                    mouse[1] < self.butons[0].y + self.butons[0].height:
                                if click[0] == 1:
                                    self.Check(self.players[index][0],
                                               self.MaxBlind)
                                    self.Update_Table(
                                        (self.players[index][2][0] - 38,
                                         self.players[index][2][1]))
                                    clock.tick(2)
                                    action = True

                            # фолд
                            if self.butons[1].x < mouse[0] < self.butons[1].x + self.butons[1].width and self.butons[1].y < \
                                    mouse[1] < self.butons[1].y + self.butons[1].height:
                                if click[0] == 1:
                                    self.Fold(self.players[index][0])
                                    clock.tick(1)
                                    action = True

                            # рейз
                            if self.butons[2].x < mouse[0] < self.butons[2].x + self.butons[2].width and self.butons[2].y < \
                                    mouse[1] < self.butons[2].y + self.butons[2].height:
                                if click[0] == 1:
                                    self.Rise(self.players[index])
                                    index_raise = index
                                    clock.tick(1)
                                    if not self.textbox.text == "":
                                        action = True
                            clock.tick(30)
                    elif not self.players[index][0].fold and self.players[index][0].money>0:
                        cartonki = (self.players[index][0].hand + self.table.distrib)
                        des = self.players[index][0].Desigion(sta, cartonki,
                                                              self.table.bank, self.MaxBlind)
                        if des == 1 and self.MaxBlind == 0:
                            des = 2
                        if des == 2:  # check / koll
                            self.Check(self.players[index][0],
                                       self.MaxBlind)
                            self.Update_Table(
                                (self.players[index][2][0] - 38,
                                 self.players[index][2][1]))
                            clock.tick(random.randint(30, 100) / 100)
                        elif des == 1:  # Fold
                            self.Fold(self.players[index][0])
                            clock.tick(1)
                        else:  # raise
                            print("raise")
                            if int(des) >= self.MaxBlind * 2:
                                self.players[index][0].PushMoney(int(des))
                                self.MaxBlind = self.players[index][0].Blind
                            else:
                                self.players[index][0].PushMoney(self.MaxBlind * 2)
                                self.MaxBlind = self.players[index][0].Blind
                            index_raise = index
                            clock.tick(1)

            enable = True
            for i in self.players:
                if i[0].Blind != self.MaxBlind:
                    if not i[0].fold and i[0].money>0:
                        print("ne proshel"+ i[0].name+ str(self.MaxBlind))
                        enable = False


    def WhoWin(self):
        maxscore = 0
        ind = 0
        for i in range(len(self.players)):
            if not self.players[i][0].fold:
                cards = self.players[i][0].hand + self.table.distrib
                combination = Combination(cards)
                self.players[i][0].score = combination.Card_score(combination.CardScore)
                if int(self.players[i][0].score) > int(maxscore):
                    maxscore = self.players[i][0].score
                    ind = i
                print(self.players[i][0].name)

        end = True
        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                end = False
                print("wishel")
            self._print(("Победил " + str(self.players[ind][0]) + " комбинацией " + combination.COMBOS[
                self.players[ind][0].score // 100]), 250, 450,
                        font_color=(0, 0, 0), font_size=35)
            pygame.display.update()
        self.players[ind][0].add_money(self.table.bank)

    def print_card(self, card, xy, flag):
        a = pygame.Surface((73, 124))
        if not flag:
            a.blit(pygame.image.load(os.path.join("Images\\Suits", self.deck.take_name(card))), (0, 0))
        else:
            a.blit(pygame.image.load("Images\\Back.png"), (0, 0))
        self.win.blit(a, xy)
        # pygame.display.update()

    def Check(self, player, blind):
        print('check')
        player.PushMoney(blind)

    def Fold(self, player):
        print("Fold")
        player.Fold()

    def Rise(self, player):
        self.textbox.active = True
        while self.textbox.active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_KP_ENTER]:
                if int(self.textbox.text) >= self.MaxBlind * 2:
                    player[0].PushMoney(int(self.textbox.text))
                else:
                    player[0].PushMoney(self.MaxBlind * 2)
                self.MaxBlind = player[0].Blind
                self.textbox.active = False
            self.textbox.Draw()
            print("pause")
            pygame.display.update()

        pass

    def HandCard(self):
        for i in self.players:
            if not i[0].fold:
                if type(i[0]) is Bot and not self.Show:
                    flag = True
                else :
                    flag = False
                for j in range(2):
                    self.print_card(i[0].hand[j], (i[2][0] + pow(-1, j) * 38, i[2][1]), flag)
            if not i[0].fold or i[0].Blind > 0:  # отрисовка блайндов
                if i[0].id % 4 == 1 or i[0].id == 0:
                    self._print(str(i[0].Blind), i[2][0], i[2][1] - 40)
                else:
                    self._print(str(i[0].Blind), i[2][0], i[2][1] + 140)

    def Update_Table(self, player_cord):
        self.update_screen(self.sitter)
        self.HandCard()
        if player_cord is not None:
            pygame.draw.rect(self.win, (224, 34, 34),
                             (player_cord[0], player_cord[1], 148, 126), 3)
        a = pygame.Surface((50, 50))
        a.blit(pygame.image.load("Images\\Dealler.png"), (0, 0))
        a.set_colorkey((0, 0, 0))
        xy_i = {
            0: (self.players[self.table.buttonId][2][0], self.players[self.table.buttonId][2][1] - 80),
            1: (self.players[self.table.buttonId][2][0]-40, self.players[self.table.buttonId][2][1] - 70),
            2: (self.players[self.table.buttonId][2][0] - 30, self.players[self.table.buttonId][2][1] + 130),
            3: (self.players[self.table.buttonId][2][0] + 120, self.players[self.table.buttonId][2][1] + 120),
            4: (self.players[self.table.buttonId][2][0], self.players[self.table.buttonId][2][1] + 130),
            5: (self.players[self.table.buttonId][2][0], self.players[self.table.buttonId][2][1] - 70)
        }
        xy = xy_i[self.table.buttonId]
        self.win.blit(a, xy)
        # distribution
        for i in range(len(self.table.distrib)):
            self.print_card(self.table.distrib[i], self.table.Cordinates[i], False)
        # bank
        self._print(str(self.table.bank), 610, 440)
        # textbx
        for i in self.players:
            self._print(i[0].name, i[2][0]+ 10, i[2][1]+ 15, font_color=(6,20,20))
        pygame.display.update()

    def _print(self, message, x, y, font_color=(255, 255, 255), font_type=r'Images/19281.otf', font_size=24):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        self.win.blit(text, (int(x), int(y)))
