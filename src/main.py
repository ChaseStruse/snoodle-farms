import pygame
import sys
from services.grid_service import create_grid, draw_grid, create_inventory_grid, draw_inventory
from models.plant import Plant
from models.inventory import Inventory
from models.game import Game
from enums.colors import Colors

cactus = Plant(name="Cactus", color=Colors.CACTUS.value, quantity=1)
rose = Plant(name="Rose", color=Colors.ROSE.value, quantity=2)

current = {
    "0": {
        "plant": cactus,
        "quantity": 2
    },
    "1": {
        "plant": rose,
        "quantity": 3
    },
}

inventory = Inventory(max_size=10, current_items=current, selected_item_key="0", selected_item=current["0"]["plant"])
game = Game(window_dimensions=[800, 800], inventory=inventory)

if __name__ == '__main__':
    game.run()
