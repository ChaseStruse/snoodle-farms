import pygame


class ShopSquare:
    def __init__(self, coords, width, size_x, size_y, plant, quantity):
        self.coords = coords
        self.width = width
        self.size_x = size_x
        self.size_y = size_y
        self.plant = plant
        self.quantity = quantity

    def get_rect_obj(self):
        return pygame.Rect(self.coords[0], self.coords[1], self.size_x, self.size_y)
