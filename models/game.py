import pygame
import sys
from services.grid_service import create_grid, draw_grid, create_inventory_grid, draw_inventory
from enums.colors import Colors
from services.collision_service import check_collision


class Game:
    def __init__(self, window_dimensions: list, inventory):
        pygame.init()
        self.window_dimensions = window_dimensions
        self.inventory = inventory
        self.grid = create_grid(window_dimensions=self.window_dimensions)
        self.font = pygame.font.Font(None, 30)
        self.inventory_grid = create_inventory_grid(inventory=self.inventory)
        self.screen = pygame.display.set_mode((window_dimensions[0], window_dimensions[1]))
        self.clock = pygame.time.Clock()
        self.screen.fill(Colors.BLACK.value)
        self.current_state = 9

    def perform_mouse_down_functionality(self, mouse_pos):
        clicked = [s for s in self.grid.values() if s.get_rect_obj().collidepoint(mouse_pos)]
        if clicked:
            if clicked[0].plantable and not clicked[0].active:
                if self.inventory.handle_quantity():
                    self.inventory_grid[self.inventory.selected_item.name].quantity -= 1
                    clicked[0].color = self.inventory.selected_item.color
                    clicked[0].width = 20
                    clicked[0].active = True
                    clicked[0].plant = self.inventory.selected_item

    def main_game_screen(self):
        draw_grid(self.screen, self.grid)
        draw_inventory(screen=self.screen, grid=self.inventory_grid, font=self.font,
                       text_color=Colors.WHITE.value)
        mouse_pos = pygame.mouse.get_pos()
        check_collision(self.grid, mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_1]:
                    self.inventory.selected_item = self.inventory.current_items["0"]["plant"]
                    self.inventory.selected_item_key = "0"
                if pressed[pygame.K_2]:
                    self.inventory.selected_item = self.inventory.current_items["1"]["plant"]
                    self.inventory.selected_item_key = "1"
                elif pressed[pygame.K_9]:
                    self.current_state = 9
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.perform_mouse_down_functionality(mouse_pos=mouse_pos)

    def shop_screen(self):
        text_to_display = self.font.render("STORE SCREEN", True, Colors.CACTUS.value)
        x, y = (100, 100)

        self.screen.blit(text_to_display, (x, y))

    def game_state(self, state_selected):
        if state_selected == 1:
            self.main_game_screen()
        if state_selected == 9:
            self.shop_screen()

    def run(self):
        while True:
            self.screen.fill(Colors.BLACK.value)
            self.game_state(self.current_state)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_1]:
                        self.current_state = 1
                    elif pressed[pygame.K_9]:
                        self.current_state = 9

            pygame.display.update()
            pygame.display.flip()
