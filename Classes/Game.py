import pygame
from Classes.Crossword import Crossword
from constants import *
from util import *


class Game:
    def __init__(self):
        pygame.init()
        self.running = False
        self.screen = pygame.display.set_mode()
        self.crossword_size = CROSSWORD_SIZE
        pygame.display.set_caption('Mazal Tov!')
        self.crossword = Crossword(self.screen, self.crossword_size)
        self.language = Language.HE

    def start_game(self):
        self.screen.fill(Color.white)
        self.crossword.init_crossword()

        self.running = True

        LETTERS = None
        if self.language == Language.EN:
            LETTERS = LETTERS_EN
        if self.language == Language.HE:
            LETTERS = LETTERS_HE

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == ESCAPE:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key in ARROWS:
                    self.move_around(event)
                if event.type == pygame.KEYDOWN and event.key in LETTERS:
                    self.crossword.change_letter(LETTERS[event.key])
                if event.type == pygame.KEYDOWN and event.key in [DEL,
                                                                  BACKSPACE]:
                    self.crossword.change_letter(' ')

            self.crossword.draw_graph()

            pygame.display.flip()

        pygame.quit()

    def move_around(self, event):
        selected = self.crossword.get_selected_cell()
        if event.key == UP:
            # from previous to top
            possibilities = range(selected.row - 1, -1, -1)
            direction = Direction.vertical

        elif event.key == DOWN:
            # from next to bottom
            possibilities = range(selected.row + 1, self.crossword_size)
            direction = Direction.vertical

        elif event.key == RIGHT:
            # from next to rightmost
            possibilities = range(selected.col + 1, self.crossword_size)
            direction = Direction.horizontal

        elif event.key == LEFT:
            # from previous to leftmost
            possibilities = range(selected.col - 1, -1, -1)
            direction = Direction.horizontal
        self.move_to_nearest(possibilities, selected.row, selected.col,
                             direction)

    def move_to_nearest(self, rng, row, col, dir):
        for x in rng:
            if dir == Direction.horizontal:
                new_cell = self.crossword.find_cell(row, x)
            elif dir == Direction.vertical:
                new_cell = self.crossword.find_cell(x, col)
            if not new_cell.get_filled():
                self.crossword.set_selected_cell(new_cell)
                break
