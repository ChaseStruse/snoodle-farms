import pygame

from src.enums.colors import Colors
from src.enums.game_states import GameStates


def draw_main_menu(game):
    start = pygame.Rect(280, 320, 240, 80)
    pygame.draw.rect(game.screen, Colors.WHITE.value, start, start.width)
    text_to_display = game.font.render("START GAME", True, Colors.BLUE.value)
    game.screen.blit(text_to_display, (start.x + 60, start.y + 30))

    quit_rect = pygame.Rect(280, 440, 240, 80)
    pygame.draw.rect(game.screen, Colors.WHITE.value, quit_rect, quit_rect.width)
    text_to_display = game.font.render("QUIT GAME", True, Colors.BLUE.value)
    game.screen.blit(text_to_display, (quit_rect.x + 60, quit_rect.y + 30))
