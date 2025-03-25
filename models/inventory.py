import pygame


class InventoryUIBlock:
    def __init__(self, coords, color, width, size_x, size_y, plant, quantity):
        self.coords = coords
        self.color = color
        self.width = width
        self.size_x = size_x
        self.size_y = size_y
        self.plant = plant
        self.quantity = quantity

    def get_rect_obj(self):
        return pygame.Rect(self.coords[0], self.coords[1], self.size_x, self.size_y)


class Inventory:
    def __init__(self, max_size: int, current_items: dict, selected_item_key: str, selected_item):
        self.max_size = max_size
        self.current_items = current_items
        self.selected_item = selected_item
        self.selected_item_key = selected_item_key

    def handle_quantity(self):
        if self.current_items[self.selected_item_key]["quantity"] > 0:
            self.current_items[self.selected_item_key]["quantity"] = (
                    self.current_items[self.selected_item_key]["quantity"] - 1
            )
            return True
        else:
            return False





