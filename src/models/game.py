import pygame
import sys
from src.services.grid_service import create_grid, draw_grid, create_inventory_grid, draw_inventory
from src.enums.colors import Colors
from src.enums.game_states import GameStates
from src.services.collision_service import check_collision
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

    def perform_mouse_down_functionality(self, mouse_pos):
        clicked = [s for s in self.grid.values() if s.get_rect_obj().collidepoint(mouse_pos)]
        if clicked:
            if clicked[0].plantable and not clicked[0].active:
                if self.game_state.inventory.handle_quantity():
                    self.inventory_grid[self.game_state.inventory.selected_item.name].quantity -= 1
                    clicked[0].color = self.game_state.inventory.selected_item.color
                    clicked[0].width = 20
                    clicked[0].active = True
                    clicked[0].plant = self.game_state.inventory.selected_item

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
