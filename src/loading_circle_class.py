import pygame
from src.bar_class import LoadingBar


# Class is responsible for drawing and animating the circular reload bar when the player is loading
class LoadingCircle:
    def __init__(self):
        self.image = [pygame.image.load(f'assets/loadingCircle/loading_circle_{x}_8.png').convert_alpha() for x in range(0, 9)]
        self.x_cord = 10
        self.y_cord = 880
        self.counter = 0
        self.choose_image = 0

    # Method selects the appropriate graphics based on the state of the game clock and the reload bar
    def tick(self, clock: float, bar: LoadingBar) -> None:
        if bar.loading >= 3:
            self.counter += clock
            if self.counter > 10:
                self.counter = 3
        else:
            self.counter = 0

        if self.counter > 2.3:
            self.choose_image = 0
        else:
            if clock <= 0.25:
                self.choose_image = 1
            elif 0.25 < clock <= 0.5:
                self.choose_image = 2
            elif 0.5 < clock <= 0.75:
                self.choose_image = 3
            elif 0.75 < clock <= 1:
                self.choose_image = 4
            elif 1 < clock <= 1.25:
                self.choose_image = 5
            elif 1.25 < clock <= 1.5:
                self.choose_image = 6
            elif 1.5 < clock <= 1.75:
                self.choose_image = 7
            elif 1.75 < clock <= 2:
                self.choose_image = 8

    # Method draws a circular reload bar on the screen has protection against unforeseen errors
    def draw(self, window: pygame.Surface) -> None:
        try:
            window.blit(self.image[self.choose_image], (self.x_cord, self.y_cord))
        except Exception as error:
            print(f'Program found the following error (LoadingCircle): {error}')
            window.blit(self.image[0], (self.x_cord, self.y_cord))
