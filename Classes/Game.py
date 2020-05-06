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
        self.language = Languages.EN

    def start_game(self):
        self.screen.fill((255, 255, 255))
        self.crossword.init_grid()
        self.crossword.add_words()
        self.running = True

        LETTERS = None
        if self.language == Languages.EN:
            LETTERS = LETTERS_EN
        if self.language == Languages.HE:
            LETTERS = LETTERS_HE

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
            new_cell = self.crossword.find_cell(max(0, selected.row - 1),
                                                selected.col)
            self.crossword.set_selected_cell(new_cell)
        elif event.key == DOWN:
            new_cell = self.crossword.find_cell(min(self.size - 1, selected.row + 1),
                                                selected.col)
            self.crossword.set_selected_cell(new_cell)
        elif event.key == RIGHT:
            new_cell = self.crossword.find_cell(selected.row,
                                                min(self.size - 1, selected.col + 1))
            self.crossword.set_selected_cell(new_cell)
        elif event.key == LEFT:
            new_cell = self.crossword.find_cell(selected.row,
                                                max(0, selected.col - 1))
            self.crossword.set_selected_cell(new_cell)
