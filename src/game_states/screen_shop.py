from src.enums.colors import Colors
from src.services.grid_service import draw_shop_grid, create_shop_grid
from src.models.plant import Plant


def shop_screen(game):
    cactus = Plant(name="Cactus", color=Colors.CACTUS.value, price=10)
    rose = Plant(name="Rose", color=Colors.ROSE.value, price=5)
    lapis = Plant(name="Lapis", color=Colors.BLUE.value, price=20)
    potato = Plant(name="Potato", color=Colors.POTATO.value, price=19)
    corn = Plant(name="Corn", color=Colors.CORN.value, price=13)
    tomato = Plant(name="Tomato", color=Colors.TOMATO.value, price=12)
    orange = Plant(name="Orange", color=Colors.ORANGE.value, price=18)

    shop_plants = [cactus, rose, lapis, potato, corn, tomato, orange]

    draw_shop_grid(game.screen, create_shop_grid(game.screen, shop_plants, game.font))
    text_to_display = game.font.render("STORE SCREEN", True, Colors.CACTUS.value)
    x, y = (400 - text_to_display.width / 2, 80)
    game.screen.blit(text_to_display, (x, y))
