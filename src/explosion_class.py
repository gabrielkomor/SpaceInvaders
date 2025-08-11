from __future__ import annotations
import pygame
from typing import List
from math import floor


# Class is responsible for creating an explosion object, which disappears after its animation
class Explosion:
    def __init__(self, x_cord: int, y_cord: int, choose_explosion: int):
        self.image = [pygame.image.load(f'assets/explosion/explosion_{x}_6.png').convert_alpha() for x in range(0, 7)]
        self.big_image = [pygame.image.load(f'assets/explosion/big_explosion_{x}_6.png').convert_alpha() for x in range(0, 7)]
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.choose_image = 0
        self.counter = 0
        self.drawing_speed = 0.3
        self.choose_explosion = choose_explosion

    # Method selects appropriate graphics based on the game counter and removes explosions
    def tick(self, explosions: List[Explosion], explosion: Explosion) -> None:
        self.counter += self.drawing_speed

        counter_floor = floor(self.counter)

        match counter_floor:
            case 0:
                self.choose_image = 0
            case 1:
                self.choose_image = 1
            case 2:
                self.choose_image = 2
            case 3:
                self.choose_image = 3
            case 4:
                self.choose_image = 4
            case 5:
                self.choose_image = 5
            case 6:
                self.choose_image = 6

        if self.counter > 8:
            self.counter = 0
            explosions.remove(explosion)

    # Method draws graphics based on the given parameters
    def draw(self, window: pygame.Surface) -> None:
        if self.choose_explosion == 1:
            window.blit(self.image[self.choose_image], (self.x_cord, self.y_cord))
        elif self.choose_explosion == 2:
            window.blit(self.big_image[self.choose_image], (self.x_cord, self.y_cord))
