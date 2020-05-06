import pygame
from Classes.Cell import Cell
from constants import Colors
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
            Word(5, 5, 5, 'h'),
            Word(grid_size-8, grid_size-1, 8, 'v')
        ]

    def init_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                cell = Cell(i, j, True)
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

    def init_selected_cell(self):
        center_cell = self.find_cell(self.grid_size//2, self.grid_size//2)
        if not center_cell.get_filled():
            self.set_selected_cell(center_cell)
            return True
        all_unfilled_cells = self.get_all_unfilled_cells()
        min_dist = 10000
        selected = None
        for cell in all_unfilled_cells:
            dist = cells_distance(cell, center_cell)
            if dist < min_dist:
                selected = cell
                min_dist = dist
        if not selected:
            return False
        self.set_selected_cell(selected)
        return True

    def get_all_unfilled_cells(self):
        all_unfilled_cells = []
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                cell = self.find_cell(i, j)
                if not cell.get_filled():
                    all_unfilled_cells.append(cell)
        return all_unfilled_cells

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
            if cell != self.selected:
                self._draw_cell(cell)
        # selected cell needs to be drawn last
        self._draw_cell(self.selected)

    def _draw_cell(self, cell):
        if cell.get_letter():
            self._draw_text(cell.get_letter(), cell.get_row(), cell.get_col())

        pygame.draw.rect(self.screen, cell.get_color(),
                         cell.get_rect(), cell.get_stroke_width())

    def _draw_text(self, text, row, col):
        cell = self.find_cell(row, col)
        pygame.draw.rect(self.screen, Colors.white, cell.get_rect(), 0)
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
