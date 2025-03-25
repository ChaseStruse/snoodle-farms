from src.enums.colors import Colors


def check_collision(grid: dict, mouse_pos: tuple) -> None:
    for box in grid.values():
        if box.get_rect_obj().collidepoint((mouse_pos[0], mouse_pos[1])) and not box.active:
            box.color = Colors.RED.value
        else:
            if box.plant is not None:
                box.color = box.plant.color
            elif not box.active and not box.plantable:
                box.color = Colors.WHITE.value
            elif box.plantable and not box.active:
                box.color = Colors.GREY.value
