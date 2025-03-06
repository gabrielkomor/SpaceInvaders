import pygame
from math import floor
from scripts.settingsClass import Settings


# Class is responsible for creating a bar that corresponds to the player's reload level
class LoadingBar:
    def __init__(self):
        self.image = [pygame.image.load(f'bar/loading_bar_{x}_3.png') for x in range(0, 4)]
        self.x_cord = 60
        self.y_cord = 890
        self.loading = 0
        self.chose_image = 0

    # Method loads the reload bar if it is not fully charged,
    # the reload is reset when the shot is fired (pressing the spacebar in the player's class)
    def tick(self, clock: float, player) -> None:
        self.loading += clock / Settings.player_reload_time

        if self.loading > 5:
            self.loading = 5

        if self.chose_image != 3:
            match floor(self.loading):
                case 0:
                    self.chose_image = 0
                case 1:
                    self.chose_image = 1
                case 2:
                    self.chose_image = 2
                case 3:
                    self.chose_image = 3

    # Method draws the appropriate reload image on the screen
    def draw(self, window: pygame.Surface) -> None:
        try:
            window.blit(self.image[self.chose_image], (self.x_cord, self.y_cord))
        except Exception as error:
            print(f'Program found following error (LoadingBar): {error}')
            window.blit(self.image[0], (self.x_cord, self.y_cord))