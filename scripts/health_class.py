import pygame
from scripts.settings_class import Settings


# Class is responsible for drawing the player's health bar
class HealthBar:
    def __init__(self):
        self.image = [pygame.image.load(f'healthBar/healthBar_{x}_5.png').convert_alpha() for x in range(0, 6)]
        self.x_cord = 440
        self.y_cord = 877
        self.chose_image = 0

    # Method is responsible for drawing the appropriate health bar graphics
    def tick(self) -> None:
        self.chose_image = Settings.player_health

    # Method draws appropriate graphics based on the player's current life status
    def draw(self, window: pygame.Surface) -> None:
        try:
            window.blit(self.image[self.chose_image], (self.x_cord, self.y_cord))
        except Exception as error:
            print(f'Program found following error (HealthBar): {error}')
            window.blit(self.image[0], (self.x_cord, self.y_cord))
