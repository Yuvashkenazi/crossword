import pygame
from Classes.Crossword import Crossword


class Game:
    def __init__(self):
        pygame.init()
        self.running = False
        self.screen = pygame.display.set_mode([800, 800])
        pygame.display.set_caption('Mazal Tov!')

    def start_game(self):
        self.running = True
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))

            crossword = Crossword(self.screen, 16)
            crossword.init_grid()

            pygame.display.flip()

        pygame.quit()
