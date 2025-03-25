from src.enums.colors import Colors


def shop_screen(game):
    text_to_display = game.font.render("STORE SCREEN", True, Colors.CACTUS.value)
    x, y = (100, 100)

    game.screen.blit(text_to_display, (x, y))
