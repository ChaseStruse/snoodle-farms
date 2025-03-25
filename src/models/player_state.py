import pygame
from src.enums.game_states import GameStates
from src.game_screens.screen_main_game import main_game_screen
from src.game_screens.screen_shop import shop_screen
from src.game_screens.screen_main_menu import draw_main_menu

class PlayerState:
    def __init__(self, starting_inventory, starting_state):
        self.inventory = starting_inventory
        self.state = starting_state

    def manage_state(self, key_pressed):
        if key_pressed[pygame.K_1]:
            self.state = GameStates.MAIN_STATE.value
        elif key_pressed[pygame.K_9]:
            self.state = GameStates.SHOP_STATE.value

    def get_current_state_to_display(self, game):
        if self.state == GameStates.MAIN_STATE.value:
            return main_game_screen(player_state=self, game=game)
        if self.state == GameStates.SHOP_STATE.value:
            return shop_screen(game=game)
        if self.state == GameStates.MAIN_MENU_STATE.value:
            return draw_main_menu(game=game)


