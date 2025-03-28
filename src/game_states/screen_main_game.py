import pygame
import sys
from src.enums.colors import Colors
from src.enums.game_states import GameStates
from src.services.collision_service import check_collision
from src.services.grid_service import draw_grid, draw_inventory


def perform_mouse_down_functionality(game, mouse_pos):
    clicked = [s for s in game.grid.values() if s.get_rect_obj().collidepoint(mouse_pos)]
    if clicked:
        if clicked[0].plantable and not clicked[0].active:
            if game.game_state.inventory.handle_quantity():
                game.inventory_grid[game.game_state.inventory.selected_item.name].quantity -= 1
                clicked[0].color = game.game_state.inventory.selected_item.color
                clicked[0].width = 20
                clicked[0].active = True
                clicked[0].plant = game.game_state.inventory.selected_item


def main_game_screen(game, game_state):
    draw_grid(game.screen, game.grid)
    draw_inventory(screen=game.screen, grid=game.inventory_grid, font=game.font,
                   text_color=Colors.WHITE.value)
    mouse_pos = pygame.mouse.get_pos()
    check_collision(game.grid, mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_1]:
                game.game_state.inventory.selected_item = game.game_state.inventory.current_items["0"]["plant"]
                game.game_state.inventory.selected_item_key = "0"
            if pressed[pygame.K_2]:
                game.game_state.inventory.selected_item = game.game_state.inventory.current_items["1"]["plant"]
                game.game_state.inventory.selected_item_key = "1"
            elif pressed[pygame.K_9]:
                game_state.state = GameStates.SHOP_STATE.value
        if event.type == pygame.MOUSEBUTTONDOWN:
            perform_mouse_down_functionality(game=game, mouse_pos=mouse_pos)
