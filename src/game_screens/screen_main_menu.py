import pygame
import sys
from src.enums.colors import Colors
from src.enums.game_states import GameStates

class MenuButton:
    def __init__(self, coords, color, size_x, size_y, state_represented):
        self.coords = coords
        self.color = color
        self.size_x = size_x
        self.size_y = size_y
        self.state_represented = state_represented

    def get_rect_obj(self):
        return pygame.Rect(self.coords[0], self.coords[1], self.size_x, self.size_y)

def draw_main_menu(game):
    start = MenuButton(coords=(280, 320), color=Colors.WHITE.value, size_x=240, size_y=80,
                       state_represented=GameStates.MAIN_STATE.value)
    pygame.draw.rect(game.screen, start.color, start.get_rect_obj(), start.get_rect_obj().width)
    text_to_display = game.font.render("START GAME", True, Colors.BLUE.value)
    game.screen.blit(text_to_display, (start.coords[0] + 60, start.coords[0] + 30))

    quit_rect = MenuButton(coords=(280, 440), color=Colors.WHITE.value, size_x=240, size_y=80,
                           state_represented=GameStates.QUIT_STATE.value)
    pygame.draw.rect(game.screen, quit_rect.color, quit_rect.get_rect_obj(), quit_rect.get_rect_obj().width)
    text_to_display = game.font.render("QUIT GAME", True, Colors.BLUE.value)
    game.screen.blit(text_to_display, (quit_rect.coords[0] + 60, quit_rect.coords[1] + 30))

    return [start, quit_rect]


def main_menu_screen(game):
    mouse_pos = pygame.mouse.get_pos()
    buttons = draw_main_menu(game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = [s for s in buttons if s.get_rect_obj().collidepoint(mouse_pos)]
            if clicked:
                game.player_state.state = clicked[0].state_represented
