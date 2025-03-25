import pygame


class GridSquare:
    def __init__(self, coords, color, width, size_x, size_y, active=False, plantable=False, plant=None):
        self.coords = coords
        self.color = color
        self.width = width
        self.size_x = size_x
        self.size_y = size_y
        self.active = active
        self.plantable = plantable
        self.plant = plant

    def get_rect_obj(self):
        return pygame.Rect(self.coords[0], self.coords[1], self.size_x, self.size_y)
