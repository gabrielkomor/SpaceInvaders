import time

from main import *
from src.start_end_defeat_screen import Screens
from src.settings_class import Settings


class Shop:
    # Method invokes the store window after the level is completed
    @staticmethod
    def shop() -> None:
        background = pygame.image.load('assets/background/background.jpeg').convert_alpha()
        icon = pygame.image.load('assets/icon/icon.png').convert_alpha()
        add_bullet_speed = pygame.image.load('assets/shopIcons/addBulletSpeed.png').convert_alpha()
        add_player_health = pygame.image.load('assets/shopIcons/addHealth.png').convert_alpha()
        add_reload_speed = pygame.image.load('assets/shopIcons/addReloadSpeed.png').convert_alpha()
        add_player_speed = pygame.image.load('assets/shopIcons/addSpeed.png').convert_alpha()
        gear_image = pygame.image.load('assets/shopIcons/gear.png').convert_alpha()
        cash_icon = pygame.image.load('assets/shopIcons/dollar.png').convert_alpha()
        no_icon = pygame.image.load('assets/shopIcons/no.png').convert_alpha()
        yes_icon = pygame.image.load('assets/shopIcons/yes.png').convert_alpha()
        exit_icon = pygame.image.load('assets/shopIcons/door.png').convert_alpha()
        player_level_1 = pygame.image.load('assets/player/level_1/rocketStatic_1_Lvl_1.png').convert_alpha()
        player_level_2 = pygame.image.load('assets/player/level_2/rocketStatic_1_Lvl_2.png').convert_alpha()
        player_level_3 = pygame.image.load('assets/player/level_3/rocketStatic_1_Lvl_3.png').convert_alpha()
        player_level_4 = pygame.image.load('assets/player/level_4/rocketStatic_1_Lvl_4.png').convert_alpha()

        # Game window setting
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SCALED | pygame.FULLSCREEN)
        pygame.display.set_caption('Space invaders')
        pygame.display.set_icon(icon)

        # Setting colors, fonts, upgrade prices and displayed texts
        black = (0, 0, 0)
        grey = (128, 128, 128)
        green = (100, 255, 100)
        bullet_speed_upgrade_cost = 70
        player_speed_upgrade_cost = 50
        player_reload_upgrade_cost = 80
        player_health_upgrade_cost = 120
        font = pygame.font.Font(None, 75)
        font_shop = pygame.font.Font(None, 125)
        shop_text = font_shop.render('Shop', True, black)
        bullet_speed_cost = font.render(f'{bullet_speed_upgrade_cost}$', True, black)
        player_speed_cost = font.render(f'{player_speed_upgrade_cost}$', True, black)
        player_reload_cost = font.render(f'{player_reload_upgrade_cost}$', True, black)
        player_health_cost = font.render(f'{player_health_upgrade_cost}$', True, black)

        # Setting the position of elements that will be displayed on the screen
        yes_no_list = [
            [yes_icon, no_icon, (470, 335), bullet_speed_upgrade_cost, True],
            [yes_icon, no_icon, (470, 435), player_speed_upgrade_cost, True],
            [yes_icon, no_icon, (470, 535), player_reload_upgrade_cost, True],
            [yes_icon, no_icon, (470, 635), player_health_upgrade_cost, True],
        ]

        elements_list = [
            (shop_text, (215, 85)),
            (bullet_speed_cost, (100, 330)),
            (player_speed_cost, (100, 430)),
            (player_reload_cost, (100, 530)),
            (player_health_cost, (85, 630)),
            (add_bullet_speed, (230, 330)),
            (add_player_speed, (230, 430)),
            (add_reload_speed, (230, 530)),
            (add_player_health, (230, 630)),
            (gear_image, (360, 330)),
            (gear_image, (360, 430)),
            (gear_image, (360, 530)),
            (gear_image, (360, 630)),
            (cash_icon, (240, 750)),
            (exit_icon, (550, 930)),
        ]

        # Setting collisions for buttons that can be controlled in the store
        add_bullet_speed_hit_box = pygame.Rect(360, 330, 64, 64)
        add_player_speed_hit_box = pygame.Rect(360, 430, 64, 64)
        add_reload_speed_hit_box = pygame.Rect(360, 530, 64, 64)
        add_player_health_hit_box = pygame.Rect(360, 630, 64, 64)
        exit_icon_hit_box = pygame.Rect(550, 930, 128, 128)

        # Loading screen
        Screens.loading()

        while True:
            mouse_xy = pygame.mouse.get_pos()
            mouse_state = pygame.mouse.get_pressed()[0]

            # Setting the values of variables that change with integration with the program
            player_cash_text = font.render(f': {Settings.player_cash}$', True, black)
            player_bullet_text = font.render(f'{Settings.player_bullet_speed_upgrade}/3', True, black)
            player_speed_text = font.render(f'{Settings.player_speed_upgrade}/3', True, black)
            player_reload_text = font.render(f'{Settings.player_reload_time_upgrade}/3', True, black)
            player_health_text = font.render(f'{Settings.player_health}/5', True, black)

            if Settings.player_bullet_speed_upgrade == 3:
                yes_no_list[0][4] = False
            if Settings.player_speed_upgrade == 3:
                yes_no_list[1][4] = False
            if Settings.player_reload_time_upgrade == 3:
                yes_no_list[2][4] = False
            if Settings.player_health == 5:
                yes_no_list[3][4] = False
            else:
                yes_no_list[3][4] = True

            text_elements_list = [
                (player_cash_text, (280, 745)),
                (player_bullet_text, (550, 340)),
                (player_speed_text, (550, 440)),
                (player_reload_text, (550, 540)),
                (player_health_text, (550, 640))
            ]

            # Drawing store elements on the screen
            window.blit(background, (0, 0))
            pygame.draw.rect(window, grey, (50, 50, 600, 150))
            pygame.draw.rect(window, grey, (50, 250, 600, 600))

            Settings.all_player_upgrades = (Settings.player_speed_upgrade +
                                            Settings.player_bullet_speed_upgrade +
                                            Settings.player_reload_time_upgrade)

            if 0 <= Settings.all_player_upgrades < 3:
                pygame.draw.rect(window, green, (50, 900, 110, 110))
            else:
                pygame.draw.rect(window, grey, (50, 900, 110, 110))

            if 3 <= Settings.all_player_upgrades < 6:
                pygame.draw.rect(window, green, (170, 900, 110, 110))
            else:
                pygame.draw.rect(window, grey, (170, 900, 110, 110))

            if 6 <= Settings.all_player_upgrades < 9:
                pygame.draw.rect(window, green, (290, 900, 110, 110))
            else:
                pygame.draw.rect(window, grey, (290, 900, 110, 110))

            if Settings.all_player_upgrades == 9:
                pygame.draw.rect(window, green, (410, 900, 110, 110))
            else:
                pygame.draw.rect(window, grey, (410, 900, 110, 110))

            window.blit(player_level_1, (72, 922))
            window.blit(player_level_2, (192, 922))
            window.blit(player_level_3, (312, 922))
            window.blit(player_level_4, (432, 922))

            for element, position in text_elements_list:
                window.blit(element, position)

            for element, position in elements_list:
                window.blit(element, position)

            for yes_ic, no_ic, position, cost, state in yes_no_list:
                if Settings.player_cash >= cost and state:
                    window.blit(yes_ic, position)
                else:
                    window.blit(no_ic, position)

            pygame.display.update()

            # Event checking
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()

                # This piece of code is responsible for purchasing upgrades when certain conditions are met
                # protection against clicking several times in the same place has been introduced
                if event.type == pygame.MOUSEBUTTONDOWN and not mouse_state:
                    mouse_state = True
                    if add_bullet_speed_hit_box.collidepoint(mouse_xy) and Settings.player_bullet_speed_upgrade < 3 \
                            and Settings.player_cash >= bullet_speed_upgrade_cost:
                        Settings.player_bullet_speed_upgrade += 1
                        Settings.player_bullet_speed += 2
                        Settings.player_cash -= bullet_speed_upgrade_cost
                    if add_player_speed_hit_box.collidepoint(mouse_xy) and Settings.player_speed_upgrade < 3 \
                            and Settings.player_cash >= player_speed_upgrade_cost:
                        Settings.player_speed_upgrade += 1
                        Settings.player_speed += 1
                        Settings.player_cash -= player_speed_upgrade_cost
                    if add_reload_speed_hit_box.collidepoint(mouse_xy) and Settings.player_reload_time_upgrade < 3 \
                            and Settings.player_cash >= player_reload_upgrade_cost:
                        Settings.player_reload_time_upgrade += 1
                        Settings.player_reload_time -= 1
                        Settings.player_cash -= player_reload_upgrade_cost
                    if add_player_health_hit_box.collidepoint(mouse_xy) and Settings.player_health < 5 \
                            and Settings.player_cash >= player_health_upgrade_cost:
                        Settings.player_health += 1
                        Settings.player_cash -= player_health_upgrade_cost
                    # Exit from the store
                    if exit_icon_hit_box.collidepoint(mouse_xy):
                        Screens.loading()
                        main()
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_state = False
