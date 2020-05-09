import pygame
from Classes.Cell import Cell
from Classes.ClueBox import ClueBox
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
        self.small_font = pygame.font.Font(get_font_location(), 1)
        self.words = self.load_words(words)
        self.clue_box = ClueBox(self.screen)
        # right to left
        self.rtl = rtl

    def init_crossword(self):
        self.init_font()
        self.init_grid()
        self.add_words()
        self.init_selected_cell()
        self.clue_box.display_clues()

    def init_font(self):
        font_location = get_font_location()
        while self.font.get_height() < calculate_scale():
            bigger_font = pygame.font.Font(font_location, self.font.get_height())
            self.font = bigger_font
        self.small_font = pygame.font.Font(font_location, self.font.get_height() // 5)

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
        self.clue_box.set_selected_numbers(cell.get_belongs_to())
        self.clue_box.display_clues()

    def add_words(self):
        # word = start_row, start_col, length, dir
        for word in self.words:
            self._add_word(word)
        self.add_word_numbers()
        self.clue_box.set_words(self.words)

    def add_word_numbers(self):
        # update Cells
        if self.rtl:
            cells = sorted(self.get_all_unfilled_cells(),
                           key=lambda x: (x.row, -x.col))
        else:
            cells = sorted(self.get_all_unfilled_cells(),
                           key=lambda x: (x.row, x.col))
        i = 0
        for cell in cells:
            horizontal_neighbors = 0
            for nbr in [self.find_cell(cell.row, cell.col - 1),
                        self.find_cell(cell.row, cell.col + 1)]:
                if nbr and not nbr.get_filled():
                    horizontal_neighbors += 1
            vertical_neighbors = 0
            for nbr in [self.find_cell(cell.row - 1, cell.col),
                        self.find_cell(cell.row + 1, cell.col)]:
                if nbr and not nbr.get_filled():
                    vertical_neighbors += 1
            directions = [horizontal_neighbors, vertical_neighbors]

            # if there are horizontal neighbors
            if directions[0]:
                # if cell is first in horizontal word - increase and give i
                if Direction.horizontal in cell.get_first():
                    i += 1
                    cell.set_belongs_to(Direction.horizontal, i)
                # else give it the number of the previous cell
                else:
                    if self.rtl:
                        prev_h_cell = self.find_cell(cell.row, cell.col + 1)
                    else:
                        prev_h_cell = self.find_cell(cell.row, cell.col - 1)
                    prev_h_i = prev_h_cell.get_belongs_to()[0]
                    cell.set_belongs_to(Direction.horizontal, prev_h_i)

            # if there are vertical neighbors
            if directions[1]:
                # if cell is first in vertical word - increase and give i
                # (but increase only if it wasn't already increased for
                # horizontal clue)
                if Direction.vertical in cell.get_first():
                    if Direction.horizontal not in cell.get_first():
                        i += 1
                    cell.set_belongs_to(Direction.vertical, i)
                else:
                    prev_v_cell = self.find_cell(cell.row - 1, cell.col)
                    prev_v_i = prev_v_cell.get_belongs_to()[1]
                    cell.set_belongs_to(Direction.vertical, prev_v_i)

        # update Words
        for word in self.words:
            word_first_cell = self.find_cell(word.row, word.col)
            index = 0 if word.direction == Direction.horizontal else 1
            word.number = word_first_cell.get_belongs_to()[index]

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
                    cell.set_first(Direction.horizontal)
            elif word.direction == Direction.vertical:
                cell = self.find_cell(word.row + i, word.col)
                if i == 0:
                    cell.set_first(Direction.vertical)
            cell.set_filled(False)

    def draw_graph(self):
        for cell in self.cells:
            if cell != self.selected:
                self._draw_cell(cell)
        # selected cell needs to be drawn last
        self._draw_cell(self.selected)

    def _draw_cell(self, cell):
        if cell.get_letter():
            self._draw_letter(cell)
        if cell.get_first():
            self._draw_clue_number(cell)
        # self._draw_clue_number(cell)

        pygame.draw.rect(self.screen, cell.get_color(),
                         cell.get_rect(), cell.get_stroke_width())

    def _draw_clue_number(self, cell):
        coords = get_coordinates_from_grid(cell.get_row(), cell.get_col())

        index = 0 if cell.get_first() == Direction.horizontal else 1
        text = str(cell.get_belongs_to()[index])
        offset = self._get_cell_center_offset(text)
        dest = (coords[0] + offset[0] + 30,
                coords[1] + offset[1] + 7)  # TODO: fit to all screens
        surface = self.small_font.render(text, True, Color.black)
        self.screen.blit(surface, dest)

        # # comment previous and uncomment this to see all cell numbers
        # text = str(cell.get_belongs_to()[0])
        # offset = self._get_cell_center_offset(text)
        # dest = (coords[0] + offset[0] + 20,
        # coords[1] + offset[1] + 7)
        # surface = self.small_font.render(text, True, Color.black)
        # self.screen.blit(surface, dest)
        #
        # text = str(cell.get_belongs_to()[1])
        # offset = self._get_cell_center_offset(text)
        # dest = (coords[0] + offset[0] + 30,
        #         coords[1] + offset[1] + 7)
        # surface = self.small_font.render(text, True, Color.black)
        # self.screen.blit(surface, dest)

    def _draw_letter(self, cell):
        pygame.draw.rect(self.screen, Color.white, cell.get_rect(), 0)
        coords = get_coordinates_from_grid(cell.get_row(), cell.get_col())
        text = cell.get_letter()
        offset = self._get_cell_center_offset(text)

        dest = (coords[0] + offset[0], coords[1] + offset[1])
        draw_text(self.screen, self.font, dest[0], dest[1], text, Color.purple)

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

    def __repr__(self):
        end_row = self.row if self.direction == Direction.horizontal else self.col + self.length
        end_col = self.col if self.direction == Direction.vertical else self.row + self.length
        return f"#{self.number}{self.direction}, text: {self.text}, <{self.row}, {self.col}> to <{end_row}, {end_col}>"
