import pygame


class TextBox:
    def __init__(self, x, y, width, height, win):
        self.win = win
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.text = ""
        self.active = False

    def Draw(self):
        if self.active:
            clock = pygame.time.Clock()
            pygame.draw.rect(self.win, (255, 255, 255), (self.x, self.y, self.width, self.height))
            pygame.draw.rect(self.win, (0, 0, 0), (self.x - 3, self.y - 3, self.width, self.height), 3)
            self._print(str(self.text), self.x + 4, self.y + 4)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_0]:
                self.text += str(0)
            if keys[pygame.K_1]:
                self.text += str(1)
            if keys[pygame.K_2]:
                self.text += str(2)
            if keys[pygame.K_3]:
                self.text += str(3)
            if keys[pygame.K_4]:
                self.text += str(4)
            if keys[pygame.K_5]:
                self.text += str(5)
            if keys[pygame.K_6]:
                self.text += str(6)
            if keys[pygame.K_7]:
                self.text += str(7)
            if keys[pygame.K_8]:
                self.text += str(8)
            if keys[pygame.K_9]:
                self.text += str(9)
            if keys[pygame.K_BACKSPACE]:
                self.text = self.text[:len(self.text) - 1]
            if keys[pygame.K_ESCAPE]:
                self.text = ""
                self.active = False
            clock.tick(5)

    def _print(self, message, x, y, font_color=(0, 0, 0,), font_type=r'Images/19281.otf', font_size=24):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        self.win.blit(text, (int(x), int(y)))
