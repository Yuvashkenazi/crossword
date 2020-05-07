import pygame

from constants import Color
from util import *


class Cell:
    def __init__(self, row, col, filled):
        self.row = row
        self.col = col
        self.filled = filled
        self.selected = False
        self._set_color()
        self.scale = calculate_scale()
        self.stroke_width = 0 if filled else 3
        self.letter = ' '

    def get_color(self):
        return self.color

    def get_rect(self):
        coords = get_coordinates_from_grid(self.row, self.col)
        return pygame.Rect(coords[0], coords[1], self.scale, self.scale)

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def set_filled(self, is_filled):
        self.filled = is_filled
        self.stroke_width = 0 if is_filled else 3

    def get_filled(self):
        return self.filled

    def get_stroke_width(self):
        return self.stroke_width

    def set_stroke_width(self, value):
        self.stroke_width = value

    def set_selected(self, selected):
        self.selected = selected
        self._set_color()

    def _set_color(self):
        self.color = Color.black if not self.selected else Color.green

    def set_letter(self, letter):
        self.letter = letter

    def get_letter(self):
        return self.letter
