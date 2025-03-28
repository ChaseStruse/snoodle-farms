"""
Main Object for the game and its objects within it

Responsibilities
- Keeps track of the grids
- Contains the main game loop
"""

import pygame
import sys
from src.services.grid_service import create_grid, create_inventory_grid
from src.enums.colors import Colors
from src.enums.game_states import GameStates
from src.game_states.game_state import GameState


class Game:
    def __init__(self, window_dimensions: list, game_state: GameState):
        pygame.init()
        self.window_dimensions = window_dimensions
        self.game_state = game_state
        self.grid = create_grid(window_dimensions=self.window_dimensions)
        self.font = pygame.font.Font(None, 30)
        self.inventory_grid = create_inventory_grid(inventory=self.game_state.inventory)
        self.screen = pygame.display.set_mode((window_dimensions[0], window_dimensions[1]))
        self.clock = pygame.time.Clock()
        self.screen.fill(Colors.BLACK.value)

    def run(self):
        while True:
            self.screen.fill(Colors.BLACK.value)
            self.game_state.get_current_state_to_display(game=self)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.game_state.state != GameStates.MAIN_MENU_STATE:
                    if event.type == pygame.KEYDOWN:
                        pressed = pygame.key.get_pressed()
                        self.game_state.manage_state_in_game(key_pressed=pressed)

            pygame.display.update()
            pygame.display.flip()
