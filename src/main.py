from models.plant import Plant
from models.inventory import Inventory
from models.game import Game
from models.player_state import PlayerState
from enums.colors import Colors
from enums.game_states import GameStates


def initialize_game_state():
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

    inv = Inventory(max_size=8, current_items=current, selected_item_key="0", selected_item=current["0"]["plant"])
    return PlayerState(starting_state=GameStates.MAIN_MENU_STATE.value, starting_inventory=inv)


if __name__ == '__main__':
    game_state = initialize_game_state()
    game = Game(window_dimensions=[800, 800], player_state=game_state)

    game.run()
