import pygame
from scripts.settingsClass import Settings


# Class is responsible for drawing the player's account balance
class Coin:
    def __init__(self, color=(0, 0, 0)):
        self.image = pygame.image.load('coin/dollar.png').convert_alpha()
        self.x_cord = 320
        self.y_cord = 879
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.color = color
        self.font = pygame.font.Font(None, self.height)
        self.text = self.font.render(f'{Settings.player_cash}', True, self.color)

    # Method updates the player's account balance
    def tick(self) -> None:
        self.text = self.font.render(f' {Settings.player_cash}', True, self.color)

    # Method draws a coin and the current balance of the player's account on the screen
    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.image, (self.x_cord, self.y_cord))
        window.blit(self.text, (self.x_cord + self.width, self.y_cord + 7))


# Class is responsible for drawing the level icon
class Icon(Coin):
    def __init__(self, color=(0, 0, 0)):
        super().__init__(color)
        self.image = pygame.image.load('level/levelIcon.png').convert_alpha()
        self.x_cord = 200
        self.y_cord = 880
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.font = pygame.font.Font(None, self.height)
        self.text = self.font.render(f'{Settings.game_level}/10', True, self.color)

    # Method updates the displayed game level
    def tick(self) -> None:
        self.text = self.font.render(f' {Settings.game_level}/10', True, self.color)
