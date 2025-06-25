from __future__ import annotations
import pygame
from scripts.bullet_class import *
from scripts.bar_class import LoadingBar
from scripts.settings_class import Settings


# Class is responsible for creating the player
class Player:
    def __init__(self):
        self.image_static = {
            0: [pygame.image.load(f'player/level_1/rocketStatic_{x}_Lvl_1.png').convert_alpha() for x in range(1, 3)],
            1: [pygame.image.load(f'player/level_2/rocketStatic_{x}_Lvl_2.png').convert_alpha() for x in range(1, 3)],
            2: [pygame.image.load(f'player/level_3/rocketStatic_{x}_Lvl_3.png').convert_alpha() for x in range(1, 3)],
            3: [pygame.image.load(f'player/level_4/rocketStatic_{x}_Lvl_4.png').convert_alpha() for x in range(1, 3)]
        }

        self.image_move_right = {
            0: [pygame.image.load(f'player/level_1/rocketRight_{x}_Lvl_1.png').convert_alpha() for x in range(1, 3)],
            1: [pygame.image.load(f'player/level_2/rocketRight_{x}_Lvl_2.png').convert_alpha() for x in range(1, 3)],
            2: [pygame.image.load(f'player/level_3/rocketRight_{x}_Lvl_3.png').convert_alpha() for x in range(1, 3)],
            3: [pygame.image.load(f'player/level_4/rocketRight_{x}_Lvl_4.png').convert_alpha() for x in range(1, 3)]
        }

        self.image_move_left = {
            0: [pygame.image.load(f'player/level_1/rocketLeft_{x}_Lvl_1.png').convert_alpha() for x in range(1, 3)],
            1: [pygame.image.load(f'player/level_2/rocketLeft_{x}_Lvl_2.png').convert_alpha() for x in range(1, 3)],
            2: [pygame.image.load(f'player/level_3/rocketLeft_{x}_Lvl_3.png').convert_alpha() for x in range(1, 3)],
            3: [pygame.image.load(f'player/level_4/rocketLeft_{x}_Lvl_4.png').convert_alpha() for x in range(1, 3)]
        }

        self.width = self.image_static[0][0].get_width()
        self.height = self.image_static[0][0].get_height()
        self.x_cord = 300
        self.y_cord = 770
        self.right_move = False
        self.left_move = False
        self.no_move = True
        self.hit_box = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    # Method is responsible for controlling the player, detecting collisions,
    # animations, shooting if the reload bar is full
    def tick(self, keys: pygame.key, bullets: List[Bullet], player: Player, bar: LoadingBar, mouse_x: int,
             mouse_y: int, left_button: pygame.Rect, right_button: pygame.Rect, mouse_state: bool, shot: bool) -> None:

        if keys[pygame.K_d] or keys[pygame.K_RIGHT] or (mouse_state and right_button.collidepoint(mouse_x, mouse_y)):
            self.x_cord += Settings.player_speed
            if self.x_cord + self.width >= Settings.window_width:
                self.x_cord = Settings.window_width - self.width
            self.no_move = False
            self.left_move = False
            self.right_move = True

        elif keys[pygame.K_a] or keys[pygame.K_LEFT] or (mouse_state and left_button.collidepoint(mouse_x, mouse_y)):
            self.x_cord -= Settings.player_speed
            if self.x_cord <= 0:
                self.x_cord = 0
            self.no_move = False
            self.left_move = True
            self.right_move = False

        elif not (keys[pygame.K_a] or keys[pygame.K_d]):
            self.no_move = True
            self.left_move = False
            self.right_move = False

        if shot:
            if bar.chose_image == 3:
                bullets.append(Bullet(player))
                bar.loading = 0
                bar.chose_image = 0
                self.y_cord += 15

        if self.y_cord > 770:
            self.y_cord -= 1

        self.hit_box = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    # Method draws a player, the displayed graphics depend on the current level of improvements and player state
    def draw(self, window: pygame.Surface, clock: float) -> None:
        clock = floor(clock)

        if clock > 1.5:
            clock = 1

        try:
            upgrade_level = min(Settings.all_player_upgrades // 3, 3)

            if 0 <= Settings.all_player_upgrades < 10:
                if self.no_move:
                    window.blit(self.image_static[upgrade_level][int(clock)], (self.x_cord, self.y_cord))
                elif self.right_move:
                    window.blit(self.image_move_right[upgrade_level][int(clock)], (self.x_cord, self.y_cord))
                elif self.left_move:
                    window.blit(self.image_move_left[upgrade_level][int(clock)], (self.x_cord, self.y_cord))
        except Exception as error:
            print(f'Program found following error (Player): {error}')
            window.blit(self.image_static[0][0], (self.x_cord, self.y_cord))
