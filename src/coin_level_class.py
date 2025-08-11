import pygame as pg

from src.settings_class import Settings


class Coin:
    """
    Class is responsible for drawing the player's account balance
    """

    def __init__(self, color=(0, 0, 0)):
        self.image = pg.image.load('assets/coin/dollar.png').convert_alpha()
        self.x_cord = 320
        self.y_cord = 879
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.color = color
        self.font = pg.font.Font(None, self.height)
        self.text = self.font.render(f'{Settings.player_cash}', True, self.color)

    def tick(self) -> None:
        """
        Method updates the player's account balance
        :return: None
        """
        self.text = self.font.render(f' {Settings.player_cash}', True, self.color)

    def draw(self, window: pg.Surface) -> None:
        """
        Method draws a coin and the current balance of the player's account on the screen
        :param window:
        :return: None
        """
        window.blit(self.image, (self.x_cord, self.y_cord))
        window.blit(self.text, (self.x_cord + self.width, self.y_cord + 7))


class Icon(Coin):
    """
    Class is responsible for drawing the level icon
    """

    def __init__(self, color=(0, 0, 0)):
        super().__init__(color)
        self.image = pg.image.load('assets/level/levelIcon.png').convert_alpha()
        self.x_cord = 200
        self.y_cord = 880
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.font = pg.font.Font(None, self.height)
        self.text = self.font.render(f'{Settings.game_level}/10', True, self.color)

    def tick(self) -> None:
        """
        Method updates the displayed game level
        :return: None
        """
        self.text = self.font.render(f' {Settings.game_level}/10', True, self.color)
