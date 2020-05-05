import pygame


class Cell:
    def __init__(self, row, col, filled):
        self.row = row
        self.col = col
        self.filled = filled
        self.selected = False
        self._set_color()
        self.width = 25
        self.height = 25
        self.stroke_width = 0 if filled else 3

    def get_color(self):
        return self.color

    def get_rect(self):
        return pygame.Rect(150 + self.col * 25, 75 + self.row * 25, self.width, self.height)

    def get_stroke_width(self):
        return self.stroke_width

    def set_stroke_width(self, value):
        self.stroke_width = value

    def set_selected(self, selected):
        self.selected = selected
        self._set_color()

    def _set_color(self):
        self.color = (0, 0, 0) if not self.selected else (92, 184, 92)