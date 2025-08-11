import pygame as pg

from src.settings_class import Settings


class HealthBar:
    """
    Class is responsible for drawing the player's health bar
    """
    def __init__(self):
        self.image = [pg.image.load(f'assets/healthBar/healthBar_{x}_5.png').convert_alpha() for x in range(0, 6)]
        self.x_cord = 440
        self.y_cord = 877
        self.chose_image = 0

    def tick(self) -> None:
        """
        Method is responsible for drawing the appropriate health bar graphics
        :return: None
        """
        self.chose_image = Settings.player_health

    def draw(self, window: pg.Surface) -> None:
        """
        Method draws appropriate graphics based on the player's current life status
        :param window:
        :return: None
        """
        try:
            window.blit(self.image[self.chose_image], (self.x_cord, self.y_cord))
        except Exception as error:
            print(f'Program found following error (HealthBar): {error}')
            window.blit(self.image[0], (self.x_cord, self.y_cord))
