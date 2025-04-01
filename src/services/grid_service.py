import pygame
from src.enums.colors import Colors
from src.models.grid_square import GridSquare
from src.models.inventory import InventoryUIBlock
from src.models.shop_square import ShopSquare
from src.models.plant import Plant


def create_grid(window_dimensions):
    block_size = 80
    grid = {}
    window_width = window_dimensions[0]
    window_height = window_dimensions[1]

    for x in range(0, window_width, block_size):
        for y in range(0, window_height, block_size):
            if x in (80, 160, 240, 480, 560, 640) and y not in (0, 720):
                grid[f"({x}, {y})"] = GridSquare(coords=(x, y), color=Colors.GREY.value, width=40, size_x=block_size,
                                                 size_y=block_size, plantable=True)
    return grid


def create_inventory_grid(inventory):
    block_size = 80
    current_x = 0
    grid = {}

    for item in inventory.current_items.values():
        grid[item["plant"].name] = InventoryUIBlock(coords=(current_x, 720), color=item["plant"].color, width=10,
                                                    size_x=block_size, size_y=block_size, plant=item["plant"],
                                                    quantity=item["quantity"])
        current_x += 80
    return grid


def create_shop_grid(screen, shop_items, font):
    block_size = 90
    grid = {}

    starting_coords = (100, 200)
    for plant in shop_items:
        grid[plant.name] = ShopSquare(coords=starting_coords, width=10, size_x=block_size, size_y=block_size,
                                      plant=plant, quantity=100)
        text_to_display = font.render(f"${str(plant.price)}", True, Colors.WHITE.value)
        x, y = grid[plant.name].get_rect_obj().center
        screen.blit(text_to_display, (x - text_to_display.width / 2, y - text_to_display.height / 2))

        if starting_coords[0] >= 600:
            starting_coords = (100, starting_coords[1] + 100)
        else:
            starting_coords = (starting_coords[0] + 100, starting_coords[1])
    return grid


def draw_grid(screen, grid):
    for square in grid.values():
        pygame.draw.rect(screen, square.color, square.get_rect_obj(), square.width)


def draw_inventory(screen, grid, font, text_color):
    for square in grid.values():
        pygame.draw.rect(screen, square.color, square.get_rect_obj(), square.width)
        text_to_display = font.render(str(square.quantity), True, text_color)
        x, y = square.get_rect_obj().center

        screen.blit(text_to_display, (x, y))


def draw_shop_grid(screen, grid):
    for square in grid.values():
        pygame.draw.rect(screen, square.plant.color, square.get_rect_obj(), square.width)
