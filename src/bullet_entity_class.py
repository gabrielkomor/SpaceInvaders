from __future__ import annotations
import pygame
from random import randint
from src.explosion_class import Explosion
from src.settings_class import Settings
from typing import List

WINDOW_HEIGHT = Settings.window_height
window_width = Settings.window_width


# Class is responsible for creating the enemy's projectile
class BulletEntity:
    def __init__(self, entity, displacement: int):
        self.image = pygame.image.load('assets/bullet/entity_bullet1.png').convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.id = 1
        self.speed = 2
        self.counter = 0
        self.drawing_speed = 0.2
        self.entity = entity
        self.displacement = displacement
        self.x_cord = self.entity.x_cord + self.entity.width // 2 - self.width // 2 + self.displacement
        self.y_cord = self.entity.y_cord + self.entity.height // 1.1
        self.hit_box = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    # Method moves the projectile, removes it upon collision,
    # generates explosions and subtracts health points when it collides with the player
    def tick(self, entity_bullet: BulletEntity, entity_bullets: List[BulletEntity], player,
             explosions: List[Explosion]) -> None:

        if self.counter <= 2:
            self.x_cord += self.speed
        elif 2 < self.counter <= 4:
            self.x_cord -= self.speed
        elif 6 < self.counter <= 8:
            self.x_cord -= self.speed
        elif 8 < self.counter <= 10:
            self.x_cord += self.speed
        elif self.counter > 10:
            self.counter = 0

        self.y_cord += self.speed
        self.counter += self.drawing_speed

        if self.y_cord > WINDOW_HEIGHT - 210 - self.height:
            entity_bullets.remove(entity_bullet)
        if self.x_cord + self.width > window_width:
            self.x_cord -= self.speed
        if self.x_cord < 0:
            self.x_cord += self.speed

        for entity_bullet in entity_bullets:
            if player.hit_box.colliderect(entity_bullet.hit_box):
                explosions.append(Explosion(player.x_cord, player.y_cord, 2))
                entity_bullets.remove(entity_bullet)
                if entity_bullet.id == 1:
                    Settings.player_health -= 1
                elif entity_bullet.id == 2:
                    Settings.player_health -= 2
                elif entity_bullet.id == 3:
                    Settings.player_health -= 3

        self.hit_box = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    # Method draws a bullet on the screen
    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.image, (self.x_cord, self.y_cord))


class BulletEntityTwo(BulletEntity):
    def __init__(self, entity, displacement: int):
        super().__init__(entity, displacement)
        self.image = pygame.image.load('assets/bullet/entity_bullet2.png').convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.id = 2
        self.speed = 2.5
        self.counter = 0
        self.drawing_speed = 0.2
        self.bullet_mode = randint(1, 3)
        self.x_cord = self.entity.x_cord + self.entity.width // 2 - self.width // 2 + self.displacement
        self.y_cord = self.entity.y_cord + self.entity.height // 1.1
        self.hit_box = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self, entity_bullet: BulletEntity, entity_bullets: List[BulletEntity], player,
             explosions: List[Explosion]) -> None:

        if self.bullet_mode == 1:
            if self.counter <= 2:
                self.x_cord += self.speed
            elif 2 < self.counter <= 4:
                self.x_cord -= self.speed
            elif 6 < self.counter <= 8:
                self.x_cord -= self.speed
            elif 8 < self.counter <= 10:
                self.x_cord += self.speed
            elif self.counter > 10:
                self.counter = 0

        if self.bullet_mode == 2:
            if self.counter <= 2:
                self.x_cord += self.speed * 2
            elif 2 < self.counter <= 4:
                self.x_cord += self.speed * 2
            elif 6 < self.counter <= 8:
                self.x_cord -= self.speed * 2
            elif 8 < self.counter <= 10:
                self.x_cord -= self.speed * 2
            elif self.counter > 10:
                self.counter = 0

        if self.bullet_mode == 3:
            if self.counter <= 2:
                self.x_cord += self.speed
            elif 2 < self.counter <= 4:
                self.x_cord += self.speed * 2
            elif 6 < self.counter <= 8:
                self.x_cord += self.speed
            elif 8 < self.counter <= 10:
                self.x_cord -= self.speed * 4
            elif self.counter > 10:
                self.counter = 0

        self.y_cord += self.speed
        self.counter += self.drawing_speed

        if self.y_cord > WINDOW_HEIGHT - 210 - self.height:
            entity_bullets.remove(entity_bullet)
        if self.x_cord + self.width > window_width:
            self.x_cord -= self.speed
        if self.x_cord < 0:
            self.x_cord += self.speed

        for entity_bullet in entity_bullets:
            if player.hit_box.colliderect(entity_bullet.hit_box):
                explosions.append(Explosion(player.x_cord, player.y_cord, 2))
                entity_bullets.remove(entity_bullet)
                if entity_bullet.id == 1:
                    Settings.player_health -= 1
                elif entity_bullet.id == 2:
                    Settings.player_health -= 2
                elif entity_bullet.id == 3:
                    Settings.player_health -= 3

        self.hit_box = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)


class BulletEntityThree(BulletEntity):
    def __init__(self, entity, displacement: int):
        super().__init__(entity, displacement)
        self.image = pygame.image.load('assets/bullet/entity_bullet3.png').convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.id = 3
        self.speed = 1
        self.counter = 0
        self.drawing_speed = 0.15
        self.x_cord = self.entity.x_cord + self.entity.width // 2 - self.width // 2 + self.displacement
        self.y_cord = self.entity.y_cord + self.entity.height // 1.1
        self.hit_box = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self, entity_bullet: BulletEntity, entity_bullets: List[BulletEntity], player,
             explosions: List[Explosion]) -> None:

        if self.counter <= 2:
            self.x_cord += self.speed
        elif 2 < self.counter <= 4:
            self.x_cord -= self.speed
        elif 6 < self.counter <= 8:
            self.x_cord -= self.speed
        elif 8 < self.counter <= 10:
            self.x_cord += self.speed
        elif self.counter > 10:
            self.counter = 0

        self.y_cord += self.speed
        self.counter += self.drawing_speed

        if self.y_cord > WINDOW_HEIGHT - 210 - self.height:
            entity_bullets.remove(entity_bullet)
        if self.x_cord + self.width > window_width:
            self.x_cord -= self.speed
        if self.x_cord < 0:
            self.x_cord += self.speed

        for entity_bullet in entity_bullets:
            if player.hit_box.colliderect(entity_bullet.hit_box):
                explosions.append(Explosion(player.x_cord, player.y_cord, 2))
                entity_bullets.remove(entity_bullet)
                if entity_bullet.id == 1:
                    Settings.player_health -= 1
                elif entity_bullet.id == 2:
                    Settings.player_health -= 2
                elif entity_bullet.id == 3:
                    Settings.player_health -= 3

        self.hit_box = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
