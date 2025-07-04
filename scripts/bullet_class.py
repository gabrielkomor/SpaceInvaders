from __future__ import annotations
import pygame
from scripts.player_class import *
from scripts.explosion_class import *
from scripts.coin_level_class import *
from scripts.settings_class import Settings
from scripts.bullet_entity_class import BulletEntity
from typing import List


# Class is responsible for creating the player's projectile and operating its mechanics
class Bullet:
    def __init__(self, player: Player):
        self.image = pygame.image.load('bullet/bullet.png').convert_alpha()
        self.player = player
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = self.player.x_cord + self.player.width // 2 - self.width // 2
        self.y_cord = self.player.y_cord
        self.hit_box = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    # Method removes the projectile if it goes beyond the map boundaries,
    # and also checks whether there has been a collision with another object,
    # in which case it generates an explosion, the absorption parameter disables receiving damage to the opponent
    def tick(self, bullet: Bullet, bullets: List[Bullet], entities: List[Entity], entity_bullets: List[BulletEntity],
             explosions: List[Explosion]) -> None:

        self.y_cord -= Settings.player_bullet_speed
        self.hit_box = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

        if self.y_cord <= 0:
            bullets.remove(bullet)

        # The try except statement prevents an error if two opponents are hit
        # with the same projectile (error deleting non-existent projectile)
        for entity in entities:
            if self.hit_box.colliderect(entity.hit_box):
                try:
                    if not entity.absorption:
                        entity.health -= 1

                    explosions.append(Explosion(entity.x_cord + entity.width // 4,
                                                entity.y_cord + entity.height // 4, 2))
                    bullets.remove(bullet)
                except Exception as error:
                    print(f'Program found following error (Bullet): {error}')
                    explosions.append(Explosion(entity.x_cord + entity.width // 4,
                                                entity.y_cord + entity.height // 4, 2))
                    entity.health -= 1

        # In the event of a player's projectile colliding with another, both are removed,
        # unless the player hits the opponent's projectile with id = 3, at the moment of collision,
        # the appropriate explosion animation is loaded
        for entity_bullet in entity_bullets:
            if self.hit_box.colliderect(entity_bullet.hit_box):
                try:
                    explosions.append(Explosion(self.x_cord, self.y_cord - 20, 1))
                    bullets.remove(bullet)
                    if entity_bullet.id != 3:
                        entity_bullets.remove(entity_bullet)
                        Settings.player_cash += 1
                    if entity_bullet.id == 3:
                        entity_bullet.y_cord -= 5
                except Exception as error:
                    print(f'Program found following error (Bullet): {error}')
                    explosions.append(Explosion(self.x_cord, self.y_cord - 20, 1))
                    entity_bullets.remove(entity_bullet)
                    Settings.player_cash += 1

    # Method draws bullets on the screen
    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.image, (self.x_cord, self.y_cord))
