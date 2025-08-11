from __future__ import annotations
from random import randint
from typing import List

import pygame as pg

from src.bullet_entity_class import *
from src.explosion_class import *
from src.coin_level_class import *
from src.settings_class import Settings


class Entity:
    """
    Entity class creates an enemy in the game, it has its initial parameters, which change during the game
    """
    direction = True
    window_width = Settings.window_width

    def __init__(self, x_cord: int, y_cord: int):
        self.image = [pg.image.load(f'assets/entity1/ufo_{x}_7.png').convert_alpha() for x in range(0, 8)]
        self.health_image = pg.image.load('assets/entity1/loading_bar_1_2.png').convert_alpha()
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.draw_speed = 0.1
        self.counter = 0
        self.draw_bullet_speed = 0.12
        self.bullet_counter = 0
        self.width = self.image[0].get_width()
        self.height = self.image[0].get_height()
        self.chose_image = 0
        self.health = 2
        self.absorption = False
        self.hit_box = pg.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self, entity_bullets: List[BulletEntity], entity: Entity, entities: List[Entity]) -> None:
        """
        Method is responsible for creating new enemy projectiles,
        removes the opponent from the board, increases the player's account balance and moves the object
        :param entity_bullets:
        :param entity:
        :param entities:
        :return: None
        """
        self.bullet_counter += self.draw_bullet_speed

        if floor(self.bullet_counter) == 12:
            entity_bullets.append(BulletEntity(entity, 0))
            self.bullet_counter = 0

        if self.health <= 0:
            entities.remove(entity)
            Settings.player_cash += 22

        if self.x_cord > Entity.window_width - self.width:
            Entity.direction = False
        elif self.x_cord < 0:
            Entity.direction = True

        if Entity.direction:
            self.x_cord += 1
        else:
            self.x_cord -= 1

        self.hit_box = pg.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self, window: pg.Surface) -> None:
        """
        Method is responsible for drawing the appropriate animation frame on the screen, and also draws a health bar
        :param window:
        :return: None
        """
        self.counter += self.draw_speed
        if self.counter > 8:
            self.counter = 0

        self.chose_image = floor(self.counter)

        try:
            window.blit(self.image[self.chose_image], (self.x_cord, self.y_cord))
            if self.health == 1:
                if self.chose_image == 0 or self.chose_image == 4:
                    window.blit(self.health_image, (self.x_cord, self.y_cord - 10))
                elif self.chose_image == 1 or self.chose_image == 5:
                    window.blit(self.health_image, (self.x_cord, self.y_cord - 12))
                elif self.chose_image == 2 or self.chose_image == 6:
                    window.blit(self.health_image, (self.x_cord, self.y_cord - 14))
                elif self.chose_image == 3 or self.chose_image == 7:
                    window.blit(self.health_image, (self.x_cord, self.y_cord - 12))
        except Exception as error:
            print(f'Program found following error (Entity): {error}')
            window.blit(self.image[0], (self.x_cord, self.y_cord))


class EntityTwo(Entity):
    def __init__(self, x_cord: int, y_cord: int):
        super().__init__(x_cord, y_cord)
        self.image = [pg.image.load(f'assets/entity2/ufo2_{x}_7.png').convert_alpha() for x in range(0, 8)]
        self.health_image_low = pg.image.load('assets/entity2/health_bar_0_1.png').convert_alpha()
        self.health_image_choose = self.health_image_medium = (pg.image.load('assets/entity2/health_bar_1_1.png').
                                                               convert_alpha())
        self.draw_speed = 0.1
        self.counter = 0
        self.draw_bullet_speed = 0.16
        self.bullet_counter = 0
        self.width = self.image[0].get_width()
        self.height = self.image[0].get_height()
        self.chose_image = 0
        self.health = 3
        self.absorption = False
        self.hit_box = pg.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self, entity_bullets: List[BulletEntityTwo], entity: EntityTwo, entities: List[EntityTwo]) -> None:
        self.bullet_counter += self.draw_bullet_speed

        if floor(self.bullet_counter) == 12:
            entity_bullets.append(BulletEntityTwo(entity, 0))
            self.bullet_counter = 0

        if self.health <= 0:
            entities.remove(entity)
            Settings.player_cash += 32

        if self.x_cord > Entity.window_width - self.width:
            Entity.direction = False
        elif self.x_cord < 0:
            Entity.direction = True

        if Entity.direction:
            self.x_cord += 1
        else:
            self.x_cord -= 1

        self.hit_box = pg.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self, window: pg.Surface) -> None:
        self.counter += self.draw_speed
        if self.counter > 8:
            self.counter = 0

        self.chose_image = floor(self.counter)

        try:
            window.blit(self.image[self.chose_image], (self.x_cord, self.y_cord))

            if self.health == 1:
                self.health_image_choose = self.health_image_low
            elif self.health == 2:
                self.health_image_choose = self.health_image_medium

            if self.health == 1 or self.health == 2:
                if self.chose_image == 0 or self.chose_image == 4:
                    window.blit(self.health_image_choose, (self.x_cord, self.y_cord - 10))
                elif self.chose_image == 1 or self.chose_image == 5:
                    window.blit(self.health_image_choose, (self.x_cord, self.y_cord - 12))
                elif self.chose_image == 2 or self.chose_image == 6:
                    window.blit(self.health_image_choose, (self.x_cord, self.y_cord - 14))
                elif self.chose_image == 3 or self.chose_image == 7:
                    window.blit(self.health_image_choose, (self.x_cord, self.y_cord - 12))
        except Exception as error:
            print(f'Program found following error (EntityTwo): {error}')
            window.blit(self.image[0], (self.x_cord, self.y_cord))


class EntityThree(Entity):
    def __init__(self, x_cord: int, y_cord: int):
        super().__init__(x_cord, y_cord)
        self.image = [pg.image.load(f'assets/entity3/ufo3_{x}_7.png').convert_alpha() for x in range(0, 8)]
        self.health_image = [pg.image.load(f'assets/entity3/health_{x}_2.png').convert_alpha() for x in range(0, 3)]
        self.health_image_choose = self.health_image[0]
        self.draw_speed = 0.1
        self.counter = 0
        self.draw_bullet_speed = 0.08
        self.bullet_counter = 0
        self.width = self.image[0].get_width()
        self.height = self.image[0].get_height()
        self.chose_image = 0
        self.health = 4
        self.absorption = False
        self.hit_box = pg.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self, entity_bullets: List[BulletEntityThree], entity: EntityThree, entities: List[EntityThree]) -> None:
        self.bullet_counter += self.draw_bullet_speed

        if floor(self.bullet_counter) == 12:
            entity_bullets.append(BulletEntityThree(entity, 0))
            self.bullet_counter = 0

        if self.health <= 0:
            entities.remove(entity)
            Settings.player_cash += 42

        if self.x_cord > Entity.window_width - self.width:
            Entity.direction = False
        elif self.x_cord < 0:
            Entity.direction = True

        if Entity.direction:
            self.x_cord += 1
        else:
            self.x_cord -= 1

        self.hit_box = pg.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self, window: pg.Surface) -> None:
        self.counter += self.draw_speed
        if self.counter > 8:
            self.counter = 0

        self.chose_image = floor(self.counter)

        try:
            window.blit(self.image[self.chose_image], (self.x_cord, self.y_cord))

            if self.health == 3:
                self.health_image_choose = self.health_image[2]
            elif self.health == 2:
                self.health_image_choose = self.health_image[1]
            elif self.health == 1:
                self.health_image_choose = self.health_image[0]

            if self.health == 1 or self.health == 2 or self.health == 3:
                if self.chose_image == 0 or self.chose_image == 6:
                    window.blit(self.health_image_choose, (self.x_cord, self.y_cord - 10))
                elif self.chose_image == 1 or self.chose_image == 5:
                    window.blit(self.health_image_choose, (self.x_cord, self.y_cord - 12))
                elif self.chose_image == 2 or self.chose_image == 4:
                    window.blit(self.health_image_choose, (self.x_cord, self.y_cord - 14))
                elif self.chose_image == 3:
                    window.blit(self.health_image_choose, (self.x_cord, self.y_cord - 16))
                elif self.chose_image == 7:
                    window.blit(self.health_image_choose, (self.x_cord, self.y_cord - 8))
        except Exception as error:
            print(f'Program found following error (EntityThree): {error}')
            window.blit(self.image[0], (self.x_cord, self.y_cord))


class Boss:
    """
    Class is responsible for creating the boss,
    it has unique mechanics that are activated during the fight with him (absorption, creation of enemies, random shots)
    """

    def __init__(self):
        self.image = [pg.image.load(f'assets/boss/boss_{x}.png').convert_alpha() for x in range(0, 6)]
        self.health_image = [pg.image.load(f'assets/boss/boss_health_{x}.png').convert_alpha() for x in
                             range(0, 18)]
        self.x_cord = 300
        self.y_cord = 100
        self.start_position = 300
        self.draw_speed = 0.1
        self.counter = 0
        self.draw_bullet_speed = 0.3
        self.bullet_counter = 0
        self.width = self.image[0].get_width()
        self.height = self.image[0].get_height()
        self.chose_image = 0
        self.health = 17
        self.speed = 1
        self.direction = True
        self.stage_1 = True
        self.stage_2 = True
        self.stage_3 = True
        self.absorption = False
        self.hit_box = pg.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self, entity_bullets: List[BulletEntity], entity: Entity, entities: List[Entity]) -> None:
        """
        Method works analogously to the tick method of the above classes however, it has some mechanics such as:
        when the boss reaches a specific health value, he returns to his starting position,
        becomes insensitive to damage dealt to it, stops shooting and creates additional enemies
        this state lasts until the player destroys the created enemies, then the boss returns to its original mechanics
        :param entity_bullets:
        :param entity:
        :param entities:
        :return: None
        """
        self.bullet_counter += self.draw_bullet_speed

        if floor(self.bullet_counter) == 12:
            entity_bullet_choose = randint(0, 100)

            if entity_bullet_choose < 25:
                entity_bullets.append(BulletEntity(entity, 0))
                entity_bullets.append(BulletEntity(entity, -65))
                entity_bullets.append(BulletEntity(entity, 65))
            elif 25 <= entity_bullet_choose < 70:
                entity_bullets.append(BulletEntityTwo(entity, -50))
                entity_bullets.append(BulletEntityTwo(entity, 50))
            else:
                entity_bullets.append(BulletEntityThree(entity, 0))

            self.bullet_counter = 0

        if self.health <= 0:
            entities.remove(entity)
            Settings.player_cash += 300

        if self.x_cord > WINDOW_WIDTH - self.width:
            self.direction = False
        if self.x_cord < 0:
            self.direction = True

        if self.direction:
            self.x_cord += self.speed
        else:
            self.x_cord -= self.speed

        if self.health == 13 and self.stage_1:
            self.stage_1 = False
            entities.append(Entity(300, 300))
            entities.append(Entity(500, 300))
            entities.append(EntityTwo(400, 350))
        elif self.health == 8 and self.stage_2:
            self.stage_2 = False
            entities.append(EntityTwo(300, 300))
            entities.append(Entity(500, 300))
            entities.append(EntityThree(400, 350))
        elif self.health == 2 and self.stage_3:
            self.stage_3 = False
            entities.append(EntityThree(300, 300))
            entities.append(EntityThree(500, 300))
            entities.append(EntityTwo(400, 350))

        if len(entities) > 1:
            self.draw_bullet_speed = 0
            self.absorption = True
            self.speed = 0

            if (self.start_position - self.x_cord) < -10:
                self.x_cord -= 2
            elif (self.start_position - self.x_cord) > 10:
                self.x_cord += 2
        else:
            self.draw_bullet_speed = 0.3
            self.absorption = False
            self.speed = 1

        self.hit_box = pg.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self, window: pg.Surface) -> None:
        self.counter += self.draw_speed
        if self.counter > 6:
            self.counter = 0

        self.chose_image = floor(self.counter)

        try:
            window.blit(self.health_image[self.health], (10, 10))
            window.blit(self.image[self.chose_image], (self.x_cord, self.y_cord))
        except Exception as error:
            print(f'Program found following error (Boss): {error}')
            window.blit(self.health_image[10], (10, 10))
            window.blit(self.image[0], (self.x_cord, self.y_cord))
