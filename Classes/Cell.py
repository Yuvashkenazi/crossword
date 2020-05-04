import pygame


class Cell:
    def __init__(self, x, y, filled):
        self.x = x
        self.y = y
        self.filled = filled
        self.color = (0, 0, 0)
        self.width = 25
        self.height = 25
        self.stroke_width = 0 if filled else 3

    def get_color(self):
        return self.color

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def get_stroke_width(self):
        return self.stroke_width
