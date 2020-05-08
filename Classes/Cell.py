import pygame

from constants import Color, Direction
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
        self.belongs_to_words = [0, 0]  # [horizontal, vertical]
        self.is_first_letter = ''  # '', h, v, hv

    def __repr__(self):
        return f"<{self.row}, {self.col}> color: {'black' if self.filled else 'white'}"

    def get_color(self):
        return self.color

    def get_rect(self):
        coords = get_coordinates_from_grid(self.row, self.col)
        return pygame.Rect(coords[0], coords[1], self.scale, self.scale)

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def set_belongs_to(self, direction, number):
        if direction == Direction.horizontal:
            self.belongs_to_words[0] = number
        elif direction == Direction.vertical:
            self.belongs_to_words[1] = number

    def get_belongs_to(self):
        return self.belongs_to_words

    def set_first(self, is_first):
        if is_first == Direction.horizontal:
            self.is_first_letter = is_first + self.is_first_letter
        elif is_first == Direction.vertical:
            self.is_first_letter = self.is_first_letter + is_first

    def get_first(self):
        return self.is_first_letter

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
