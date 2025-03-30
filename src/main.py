"""

Main entry point for the game

Responsibilities
- Initialize the GameState
    - Create initial inventory for the player to use at the start of a new game
    - Sets the GameState to Main Menu

- Initializes Game object
- Runs the Game
"""

from models.plant import Plant
from models.inventory import Inventory
from models.game import Game
from game_states.game_state import GameState
from enums.colors import Colors
from enums.game_states import GameStates


def initialize_game_state():
    cactus = Plant(name="Cactus", color=Colors.CACTUS.value, price=10)
    rose = Plant(name="Rose", color=Colors.ROSE.value, price=11)

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

    inv = Inventory(max_size=8, current_items=current, selected_item_key="0", selected_item=current["0"]["plant"])
    return GameState(starting_state=GameStates.MAIN_MENU_STATE.value, starting_inventory=inv)


if __name__ == '__main__':
    game_state = initialize_game_state()
    game = Game(window_dimensions=[800, 800], game_state=game_state)

    game.run()
