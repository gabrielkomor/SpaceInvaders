import pygame
import sys
from typing import List
from src.player_class import Player
from src.bullet_class import Bullet
from src.entity_class import *
from src.bar_class import *
from src.health_class import *
from src.loading_circle_class import *
from src.coin_level_class import *
from src.explosion_class import *
from src.settings_class import Settings
from src.start_end_defeat_screen import *

pygame.init()


def level_one() -> List[Entity]:
    return [
        Entity(500, 70),
        Entity(200, 70)
    ]


def level_two() -> List[Entity]:
    return [
        Entity(500, 70),
        Entity(200, 70),
        Entity(350, 150)
    ]


def level_three() -> List[Entity]:
    return [
        Entity(500, 70),
        Entity(200, 70),
        EntityTwo(350, 150),
    ]


def level_four() -> List[Entity]:
    return [
        Entity(500, 70),
        EntityTwo(200, 70),
        EntityTwo(260, 230),
    ]


def level_five() -> List[Entity]:
    return [
        Entity(500, 70),
        EntityTwo(200, 70),
        EntityTwo(260, 230),
        Entity(450, 230)
    ]


def level_six() -> List[Entity]:
    return [
        Entity(500, 70),
        EntityThree(200, 70),
        Entity(260, 230),
        Entity(450, 230)
    ]


def level_seven() -> List[Entity]:
    return [
        Entity(500, 70),
        EntityThree(200, 70),
        EntityThree(260, 230),
        Entity(450, 230)
    ]


def level_eight() -> List[Entity]:
    return [
        Entity(500, 70),
        EntityThree(200, 70),
        EntityThree(260, 230),
        EntityTwo(450, 230)
    ]


def level_nine() -> List[Entity]:
    return [
        EntityTwo(500, 70),
        EntityThree(200, 70),
        EntityThree(260, 230),
        EntityTwo(450, 230)
    ]


def level_ten() -> List[Boss]:
    return [
        Boss()
    ]


def main():
    from src.shop_class import Shop
    from src.start_end_defeat_screen import Screens

    # Set window settings
    clock = 0
    pause = False
    shot = False
    Settings.player_exit_speed = 3
    window_height = Settings.window_height
    inactive = (120, 120, 30)
    active = (160, 160, 10)
    player_cash_temp = 0
    game_level_temp = 0

    window = pygame.display.set_mode((window_width, window_height), pygame.SCALED | pygame.FULLSCREEN)
    pygame.display.set_caption('Space invaders')
    background = pygame.image.load('assets/background/background.jpeg', '../').convert_alpha()
    icon = pygame.image.load('assets/icon/icon.png', '../').convert_alpha()
    start_stop_icon = pygame.image.load('assets/icon/playStop.png', '../').convert_alpha()
    bullet_icon = pygame.image.load('assets/icon/bulletIcon.png', '../').convert_alpha()
    left_arrow = pygame.image.load('assets/icon/leftArrow.png', '../').convert_alpha()
    right_arrow = pygame.image.load('assets/icon/rightArrow.png', '../').convert_alpha()
    pygame.display.set_icon(icon)

    # Instances
    health_bar = HealthBar()
    bar = LoadingBar()
    loading_circle = LoadingCircle()
    coin = Coin()
    level = Icon()
    player = Player()
    explosions = []
    bullets = []
    entity_bullets = []

    # Positioning opponents depending on the level
    Settings.game_level += 1
    entities = level_one()
    match Settings.game_level:
        case 1:
            entities = level_one()
        case 2:
            entities = level_two()
        case 3:
            entities = level_three()
        case 4:
            entities = level_four()
        case 5:
            entities = level_five()
        case 6:
            entities = level_six()
        case 7:
            entities = level_seven()
        case 8:
            entities = level_eight()
        case 9:
            entities = level_nine()
        case 10:
            entities = level_ten()
        case _:
            Screens.end()

    # Main game loop
    while True:
        left_button = pygame.Rect(10, 950, 190, 120)
        right_button = pygame.Rect(window_width - 200, 950, 190, 120)
        shot_button = pygame.Rect(220, 950, 120, 120)
        pause_button = pygame.Rect(360, 950, 120, 120)

        # Game events (keys)
        keys = pygame.key.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_state = pygame.mouse.get_pressed()[0]

        # Check for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause_button.collidepoint(mouse_x, mouse_y):
                    pause = not pause
                if shot_button.collidepoint(mouse_x, mouse_y):
                    shot = not shot
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_SPACE:
                    shot = not shot

        # Game clock
        clock += pygame.time.Clock().tick(60) / 350
        if clock > 2:
            clock = 0

        # Tick
        if not pause:
            player.tick(keys, bullets, player, bar, mouse_x, mouse_y, left_button, right_button, mouse_state, shot)
            bar.tick(clock)
            loading_circle.tick(clock, bar)
            health_bar.tick()
            if player_cash_temp != Settings.player_cash:
                player_cash_temp = Settings.player_cash
                coin.tick()
            if game_level_temp != Settings.game_level:
                game_level_temp = Settings.game_level
                level.tick()

            for bullet in bullets:
                bullet.tick(bullet, bullets, entities, entity_bullets, explosions)
            for explosion in explosions:
                explosion.tick(explosions, explosion)
            for entity in entities:
                entity.tick(entity_bullets, entity, entities)
            for entityBullet in entity_bullets:
                entityBullet.tick(entityBullet, entity_bullets, player, explosions)

        # Draw
        window.fill((100, 100, 100))
        window.blit(background, (0, 0))
        pygame.draw.rect(window, (120, 120, 120), (0, 870, window_width, 210))
        pygame.draw.rect(window, (0, 0, 0), (0, 930, window_width, 10))

        if shot:
            pygame.draw.rect(window, active, (220, 950, 120, 120))
        else:
            pygame.draw.rect(window, inactive, (220, 950, 120, 120))

        if (left_button.collidepoint(mouse_x, mouse_y) and mouse_state) or keys[pygame.K_LEFT] or keys[pygame.K_a]:
            pygame.draw.rect(window, active, (10, 950, 190, 120))
        else:
            pygame.draw.rect(window, inactive, (10, 950, 190, 120))

        if (right_button.collidepoint(mouse_x, mouse_y) and mouse_state) or keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            pygame.draw.rect(window, active, (window_width - 200, 950, 190, 120))
        else:
            pygame.draw.rect(window, inactive, (window_width - 200, 950, 190, 120))

        if pause:
            pygame.draw.rect(window, active, (360, 950, 120, 120))
        else:
            pygame.draw.rect(window, inactive, (360, 950, 120, 120))

        window.blit(start_stop_icon, (360, 950))
        window.blit(bullet_icon, (220, 950))
        window.blit(left_arrow, (10, 950))
        window.blit(right_arrow, (window_width - 200, 950))

        player.draw(window, clock)
        bar.draw(window)
        loading_circle.draw(window)
        health_bar.draw(window)
        coin.draw(window)
        level.draw(window)

        for bullet in bullets:
            bullet.draw(window)
        for entity in entities:
            entity.draw(window)
        for entityBullet in entity_bullets:
            entityBullet.draw(window)
        for explosion in explosions:
            explosion.draw(window)
        pygame.display.update()

        # Instruction is responsible for checking whether the player still has any health points
        if Settings.player_health < 0:
            Screens.defeat()

        # Instruction check whether the player has defeated all opponents and whether their missiles are missing
        # in this case it takes the player to the store and increases the game level
        if len(entities) == 0 and len(entity_bullets) == 0:
            player.y_cord -= Settings.player_exit_speed
            Settings.player_exit_speed += .3
            if player.y_cord < -60:
                player.y_cord = 690
                Shop.shop()


if __name__ == '__main__':
    Screens.start()
