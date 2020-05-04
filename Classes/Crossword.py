import pygame
from Classes.Cell import Cell


class Crossword:
    def __init__(self, screen, grid_size):
        self.screen = screen
        self.grid_size = grid_size

    def init_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                cell = Cell(i * 25, j * 25, False)
                self._draw_cell(cell)

    def _draw_cell(self, cell):
        pygame.draw.rect(self.screen, cell.get_color(),
                         cell.get_rect(), cell.get_stroke_width())
