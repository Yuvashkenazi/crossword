import pygame

from constants import CROSSWORD_SIZE


def get_offset():
    cw_dim = calculate_scale() * CROSSWORD_SIZE
    win_dim = get_window_size()
    left_offset = (win_dim[0] - cw_dim) // 1.25
    top_offset = (win_dim[1] - cw_dim) // 2
    return left_offset, top_offset


def get_window_size():
    return pygame.display.get_window_size()


def calculate_scale():
    win_size = get_window_size()
    min_dim = min(win_size)
    allocated_size = min_dim // 1.25
    return allocated_size // CROSSWORD_SIZE


def get_coordinates_from_grid(row, col):
    scale = calculate_scale()
    offset = get_offset()
    return offset[0] + col * scale, offset[1] + row * scale


def cells_distance(cell1, cell2):
    x = cell1.col - cell2.col
    y = cell1.row - cell2.row
    distance = (x ** 2 + y ** 2) ** 0.5
    return distance


def get_font_location():
    return 'fonts/Arimo/Arimo-Regular.ttf'
