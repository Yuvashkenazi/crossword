import pygame
from Classes.Crossword import Crossword
from constants import *


class Game:
    def __init__(self):
        pygame.init()
        self.running = False
        self.screen = pygame.display.set_mode([800, 800])
        self.size = 16
        pygame.display.set_caption('Mazal Tov!')
        self.crossword = Crossword(self.screen, self.size)
        self.language = Languages.HE

    def start_game(self):
        self.screen.fill(Colors.white)
        self.crossword.init_grid()
        self.crossword.add_words()
        self.crossword.init_selected_cell()
        self.running = True

        LETTERS = None
        if self.language == Languages.EN:
            LETTERS = LETTERS_EN2
        if self.language == Languages.HE:
            LETTERS = LETTERS_HE2

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key in ARROWS:
                    self.move_around(event)
                if event.type == pygame.KEYDOWN and event.key in LETTERS:
                    self.crossword.change_letter(LETTERS[event.key])

            self.crossword.draw_graph()

            pygame.display.flip()

        pygame.quit()

    def move_around(self, event):
        selected = self.crossword.get_selected_cell()
        if event.key == UP:
            # from previous to top
            possibilities = range(selected.row - 1, -1, -1)
            direction = 'v'

        elif event.key == DOWN:
            # from next to bottom
            possibilities = range(selected.row + 1, self.size)
            direction = 'v'

        elif event.key == RIGHT:
            # from next to rightmost
            possibilities = range(selected.col + 1, self.size)
            direction = 'h'

        elif event.key == LEFT:
            # from previous to leftmost
            possibilities = range(selected.col - 1, -1, -1)
            direction = 'h'
        self.move_to_nearest(possibilities, selected.row, selected.col,
                             direction)

    def move_to_nearest(self, rng, row, col, dir):
        for x in rng:
            if dir == 'h':
                new_cell = self.crossword.find_cell(row, x)
            elif dir == 'v':
                new_cell = self.crossword.find_cell(x, col)
            if not new_cell.get_filled():
                self.crossword.set_selected_cell(new_cell)
                break
