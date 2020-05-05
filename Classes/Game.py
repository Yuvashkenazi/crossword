import pygame
from Classes.Crossword import Crossword


class Game:
    def __init__(self):
        pygame.init()
        self.running = False
        self.screen = pygame.display.set_mode([800, 800])
        self.size = 16
        pygame.display.set_caption('Mazal Tov!')

    def start_game(self):
        self.screen.fill((255, 255, 255))
        crossword = Crossword(self.screen, self.size)
        crossword.init_grid()
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    selected = crossword.get_selected_cell()
                    if event.key == 273:
                        new_cell = crossword.find_cell(max(0, selected.row-1),
                                                       selected.col)
                        crossword.set_selected_cell(new_cell)
                    elif event.key == 274:
                        new_cell = crossword.find_cell(min(self.size-1, selected.row+1),
                                                       selected.col)
                        crossword.set_selected_cell(new_cell)
                    elif event.key == 275:
                        new_cell = crossword.find_cell(selected.row,
                                                       min(self.size - 1, selected.col + 1))
                        crossword.set_selected_cell(new_cell)
                    elif event.key == 276:
                        new_cell = crossword.find_cell(selected.row,
                                                       max(0, selected.col - 1))
                        crossword.set_selected_cell(new_cell)

            crossword.draw_graph()

            pygame.display.flip()

        pygame.quit()
