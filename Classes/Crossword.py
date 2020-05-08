import pygame
from Classes.Cell import Cell
from constants import Color
from constants import Direction
from util import *
from words import words


class Crossword:
    def __init__(self, screen, grid_size, rtl=True):
        self.screen = screen
        self.grid_size = grid_size
        self.cells = []
        self.selected = None
        self.font = pygame.font.Font(get_font_location(), 1)
        self.words = self.load_words(words)
        # right to left
        self.rtl = rtl

    def init_crossword(self):
        self.init_font()
        self.init_grid()
        self.add_words()
        self.init_selected_cell()

    def init_font(self):
        font_location = get_font_location()
        while self.font.get_height() < calculate_scale():
            bigger_font = pygame.font.Font(font_location, self.font.get_height())
            self.font = bigger_font

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
        self.add_word_numbers()

    def add_word_numbers(self):
        for cell in self.get_all_unfilled_cells():
            pass #TODO: CONTINUE THIS

    def init_selected_cell(self):
        center_cell = self.find_cell(self.grid_size // 2, self.grid_size // 2)
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
            if word.direction == Direction.horizontal:
                cell = self.find_cell(word.row, word.col + i)
                if (i == 0 and not self.rtl) or (i == word.length - 1 and self.rtl):
                    cell.set_first(True)
            elif word.direction == Direction.vertical:
                cell = self.find_cell(word.row + i, word.col)
                if i == 0:
                    cell.set_first(True)
            cell.set_filled(False)

    def draw_graph(self):
        for cell in self.cells:
            if cell != self.selected:
                self._draw_cell(cell)
        # selected cell needs to be drawn last
        self._draw_cell(self.selected)

    def draw_clues(self):
        hz_words = self._get_horizontal_words()
        v_words = self._get_vertical_words()

        hz_title = reverse_word('מאוזן:') if self.rtl else 'Horizontal'
        v_title = reverse_word('מאונך:') if self.rtl else 'Vertical'

        offset = get_clues_offset()
        row_left_offset = offset[0]
        row_top_offset = offset[1]

        dest = (row_left_offset, row_top_offset)
        surface = self.font.render(hz_title, True, Color.black)
        self.screen.blit(surface, dest)

        for word in hz_words:
            row_top_offset += 60
            dest = (row_left_offset, row_top_offset)
            surface = self.font.render(reverse_word(word.q), True, Color.black)
            self.screen.blit(surface, dest)

        row_top_offset += 100

        dest = (row_left_offset, row_top_offset)
        surface = self.font.render(v_title, True, Color.black)
        self.screen.blit(surface, dest)

        for word in v_words:
            row_top_offset += 60
            dest = (row_left_offset, row_top_offset)
            surface = self.font.render(reverse_word(word.q), True, Color.black)
            self.screen.blit(surface, dest)

    def _get_horizontal_words(self):
        hz_words = []
        for word in self.words:
            if word.direction == Direction.horizontal:
                hz_words.append(word)
        return hz_words

    def _get_vertical_words(self):
        v_words = []
        for word in self.words:
            if word.direction == Direction.vertical:
                v_words.append(word)
        return v_words

    def _draw_cell(self, cell):
        if cell.get_letter():
            self._draw_text(cell.get_letter(), cell.get_row(), cell.get_col())

        pygame.draw.rect(self.screen, cell.get_color(),
                         cell.get_rect(), cell.get_stroke_width())

    def _draw_text(self, text, row, col):
        cell = self.find_cell(row, col)
        pygame.draw.rect(self.screen, Color.white, cell.get_rect(), 0)
        coords = get_coordinates_from_grid(row, col)
        offset = self._get_cell_center_offset(text)

        dest = (coords[0] + offset[0], coords[1] + offset[1])
        surface = self.font.render(text, True, Color.purple)
        self.screen.blit(surface, dest)

    def _get_cell_center_offset(self, letter):
        scale = calculate_scale()
        letter_size = self.font.size(letter)
        letter_width = letter_size[0]
        letter_height = letter_size[1]
        left_offset = (scale - letter_width) // 2
        top_offset = (scale - letter_height) // 2
        return left_offset, top_offset

    def find_cell(self, row, col):
        for cell in self.cells:
            if cell.row == row and cell.col == col:
                return cell
        return None

    def get_selected_cell(self):
        return self.selected

    def load_words(self, words):
        return [Word(**word) for word in words]


class Word:
    def __init__(self, q, ans, start_row, start_col, direction):
        self.q = q
        self.text = ans
        self.row = start_row
        self.col = start_col
        self.direction = direction
        self.length = len(ans)
        self.number = None
