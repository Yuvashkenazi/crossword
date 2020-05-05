import pygame
from Classes.Cell import Cell


class Crossword:
    def __init__(self, screen, grid_size):
        self.screen = screen
        self.grid_size = grid_size
        self.cells = []
        self.selected = None

    def init_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                cell = Cell(i, j, False)

                if i == 8 and j == 8:
                    cell.set_selected(True)
                    self.selected = cell

                self.cells.append(cell)

    def draw_graph(self):
        for cell in self.cells:
            self._draw_cell(cell)

        # selected cell needs to be drawn last
        self._draw_cell(self.selected)

    def _draw_cell(self, cell):
        pygame.draw.rect(self.screen, cell.get_color(),
                         cell.get_rect(), cell.get_stroke_width())

    def find_cell(self, row, col):
        for cell in self.cells:
            if cell.row == row and cell.col == col:
                return cell
        return None
