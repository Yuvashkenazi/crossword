import pygame
from Classes.Cell import Cell
from util import *


class Crossword:
    def __init__(self, screen, grid_size):
        self.screen = screen
        self.grid_size = grid_size
        self.cells = []
        self.selected = None
        self.words = [
            Word(0, 0, 10, 'h'),
            Word(0, 0, 10, 'v'),
            Word(0, 5, 10, 'v'),
            Word(5, 5, 5, 'h')
        ]

    def init_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                cell = Cell(i, j, True)

                if i == 8 and j == 8:
                    self.set_selected_cell(cell)

                self.cells.append(cell)

    def set_selected_cell(self, cell):
        for other_cell in self.cells:
            other_cell.set_selected(False)
        cell.set_selected(True)
        self.selected = cell

    def add_words(self):
        # word = start_row, start_col, length, dir
        for word in self.words:
            self._add_word(word)

    def change_letter(self, letter):
        if not self.selected.get_filled():
            self.selected.set_letter(letter)

    def _add_word(self, word):
        for i in range(word.length):
            if word.direction == 'h':
                cell = self.find_cell(word.row, word.col + i)
            elif word.direction == 'v':
                cell = self.find_cell(word.row + i, word.col)
            cell.set_filled(False)

    def draw_graph(self):
        for cell in self.cells:
            self._draw_cell(cell)

        # selected cell needs to be drawn last
        self._draw_cell(self.selected)

    def _draw_cell(self, cell):
        pygame.draw.rect(self.screen, cell.get_color(),
                         cell.get_rect(), cell.get_stroke_width())
        self._draw_text(cell.get_letter(), cell.get_row(), cell.get_col())

    def _draw_text(self, text, row, col):
        coords = get_coordinates_from_grid(row, col)
        surface = pygame.font.SysFont('arial', 25).render(text, True, (100, 0, 200))
        self.screen.blit(surface, (coords[0] + 5, coords[1] - 2))

    def find_cell(self, row, col):
        for cell in self.cells:
            if cell.row == row and cell.col == col:
                return cell
        return None

    def get_selected_cell(self):
        return self.selected


class Word:
    def __init__(self, start_row, start_col, length, direction, text=None):
        self.row = start_row
        self.col = start_col
        self.length = length
        self.direction = direction
        self.text = text
