import pygame
from Classes.Game import Game
from Classes.Round import Round
from Classes.Deck import Deck
from Classes.Table import Table

pygame.init()
clock = pygame.time.Clock()
quality_players = 0
disp_width = 1256
disp_height = 800
win = pygame.display.set_mode((disp_width, disp_height))


class Sitter:
    def __init__(self, game):
        self.num = 0
        self.win = win
        self.players = []
        self.game = game
        self.pl_width = 118

    def Add_Player(self):
        # Сделать связь с кодом
        if self.num < 6:
            place = pygame.Surface((self.pl_width, self.pl_width))
            place.blit(pygame.image.load(r'Images/avatar.png'), (0, 0))
            place.set_colorkey((0, 0, 0))
            Player_cord = [
                (disp_width // 2 - self.pl_width / 2, disp_height // 2 + 550 // 2 - self.pl_width / 6),
                (disp_width // 2 - 950 // 4 - self.pl_width, disp_height // 2 + 550 // 4 + self.pl_width // 5),
                (disp_width // 2 - 950 // 4 - self.pl_width, disp_height // 2 - 550 // 4 - self.pl_width // 1.5),
                (disp_width // 2 - self.pl_width / 2, disp_height // 2 - 550 // 2 - self.pl_width / 6),
                (disp_width // 2 + 950 // 4 + self.pl_width / 2, disp_height // 2 - 550 // 4 - self.pl_width // 2),
                (disp_width // 2 + 950 // 4 + self.pl_width / 2, disp_height // 2 + 550 // 4 + self.pl_width // 6)
            ]
            self.win.blit(place, Player_cord[self.num])
            if self.num == 0:
                self.game.AddPlayer(self.num)
            else:
                self.game.AddBot(self.num)
            self.players.append([self.game.PLAYERS[self.num], place, Player_cord[self.num]])
            self.num += 1
            pygame.display.update()

    def update_pl(self):
        try:
            for gamer in self.players:
                self.win.blit(gamer[1], gamer[2])
                _print(str(gamer[0].money), gamer[2][0] + self.pl_width, gamer[2][1] + self.pl_width / 1.5,
                       font_color=(255, 255, 255))
        except IndexError:
            pass


class Button:
    def __init__(self, name, width, height, x, y, Action):
        self.active_collor = (255, 246, 0)
        self.unactive_collor = (0, 92, 0)
        self.width = width
        self.height = height
        self.Action = Action
        self.x = x
        self.y = y
        self.win = win
        self.name = name
        self.Active_Game = True

    def Draw(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            pygame.draw.rect(win, self.active_collor, (self.x, self.y, self.width, self.height))
            if click[0] == 1:
                if self.Action is not None:
                    self.Action()
                else:
                    self.Active_Game = False
                clock.tick(3)
        else:
            pygame.draw.rect(win, self.unactive_collor, (int(self.x), int(self.y), int(self.width), int(self.height)))
        _print(self.name, self.x + 10, self.y + 10)


# --------------------------------------------------------------------
# ______________GAME GUI______________________________________________
# ---------------------------------------------------------------------


def _update_screen(sitter):
    # отрисовка макета
    win.fill([255, 255, 255])
    back = pygame.image.load(r'Images/Mars.jpg')
    win.blit(back, (0, 0))
    # Table
    a = pygame.Surface((950, 550))
    a.blit(pygame.image.load(r'Images/Table1.png'), (0, 0))
    a.set_colorkey((0, 0, 0))
    win.blit(a, (disp_width // 2 - 950 // 2, disp_height // 2 - 550 // 2))
    a = pygame.Surface((73, 124))
    a.blit(pygame.image.load(r'Images/Back.png'), (0, 0))
    for i in range(5):
        win.blit(a, game.table.Cordinates[i])
    # Players
    sitter.update_pl()
    # Buttons
    if buttons[-1].Active_Game:
        buttons[-1].Draw()
        buttons[-2].Draw()
    else:
        for b in range(3):
            buttons[b].Draw()


game = Game(win)
player = Sitter(game)
buttons = [
    Button('Check/Call', 150, 40, (disp_width - 950) / 2 + 700, (disp_height - 550) / 2 + 550, None),
    Button('Fold', 150, 40, (disp_width - 950) / 2 + 700 - 160, (disp_height - 550) / 2 + 550, None),
    Button('Raise', 150, 40, (disp_width - 950) / 2 + 700 + 160, (disp_height - 550) / 2 + 550, None),
    Button('Добавить игрока', 250, 40, 20, 20, player.Add_Player),
    Button('Start game', 250, 40, 20, 65, None)
]


def Run_game():
    flag = True
    while flag:
        if not buttons[-1].Active_Game:
            StartGame()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # обработка кнопки добавить игрока
        # Обработка кнопки удалить игрока
        # Начало игры
        # Запрет всех кнопок и игра
        # Табличка ввода цифр, чтобы повышать ставки и чек рейс колл
        # Вывод игры
        clock.tick(6)
        _update_screen(player)
        pygame.display.update()


def StartGame():
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # logical

        # Цикл раунда
        while len(player.players) > 1:
            table = game.table
            table.distrib = []
            table.bank = 0
            rnd = Round(player.players, table, game.win, buttons[0:3], _update_screen, player)
            # GameLogic
            rnd.StartRound()
            # after round
            table.buttonId = (table.buttonId + 1) % len(player.players)
            i = 0
            while i < len(player.players):
                print(str(i) + "index player")
                player.players[i][0].fold = False
                player.players[i][0].hand = []
                if player.players[i][0].money < game.table.SmallBlind:
                    print('delete')
                    del player.players[i]
                    i -= 1
                i += 1
            _update_screen(player)
            pygame.display.update()
        # Конец раунда
        clock.tick(150)
        _print(str(len(game.PLAYERS)), 500, 320)
        _update_screen(player)


def _print(message, x, y, font_color=(0, 0, 0,), font_type=r'Images/19281.otf', font_size=24):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    win.blit(text, (int(x), int(y)))


#    pygame.display.update() - из-за этого мерцает


Run_game()
