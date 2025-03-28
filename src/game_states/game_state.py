import pygame
from src.enums.game_states import GameStates
from src.game_states.screen_main_game import main_game_screen
from src.game_states.screen_shop import shop_screen
from src.game_states.screen_main_menu import main_menu_screen


class GameState:
    def __init__(self, starting_inventory, starting_state):
        self.inventory = starting_inventory
        self.state = starting_state

    def manage_state_in_game(self, key_pressed):
        if key_pressed[pygame.K_1]:
            self.state = GameStates.MAIN_STATE.value
        elif key_pressed[pygame.K_9]:
            self.state = GameStates.SHOP_STATE.value

    def get_current_state_to_display(self, game):
        if self.state == GameStates.MAIN_STATE.value:
            return main_game_screen(game_state=self, game=game)
        if self.state == GameStates.SHOP_STATE.value:
            return shop_screen(game=game)
        if self.state == GameStates.MAIN_MENU_STATE.value:
            return main_menu_screen(game=game)


