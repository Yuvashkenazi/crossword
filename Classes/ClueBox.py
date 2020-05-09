from util import *
from constants import *
from gameOptions import *


class ClueBox:
    def __init__(self, screen):
        self.screen = screen
        self.offset = get_clues_offset()
        self.words = []
        self.font = pygame.font.Font(get_font_location(), 22)
        self.selected_numbers = [0, 0]

    def set_words(self, words):
        self.words = words

    def set_selected_numbers(self, selected):
        self.selected_numbers = selected

    def display_clues(self):
        hz_words = self._get_words_by_direction(Direction.horizontal)
        v_words = self._get_words_by_direction(Direction.vertical)

        hz_title = reverse_word('מאוזן:') if LANGUAGE == Language.HE else 'Horizontal'
        v_title = reverse_word('מאונך:') if LANGUAGE == Language.HE else 'Vertical'

        offset = get_clues_offset()
        row_left_offset = offset[0]
        row_top_offset = offset[1]

        dest = (row_left_offset, row_top_offset)
        size = self.font.size(hz_title)
        pygame.draw.rect(self.screen, Color.white, pygame.Rect(dest[0], dest[1], size[0], size[1]), 0)
        self.font.set_bold(True)
        self.font.set_underline(True)
        draw_text(self.screen, self.font, dest[0], dest[1], hz_title, Color.black)
        self.font.set_bold(False)
        self.font.set_underline(False)

        for word in hz_words:
            row_top_offset += 60
            dest = (row_left_offset, row_top_offset)
            text = reverse_word(reverse_word(str(word.number)) + '. ' + word.q)
            color = Color.green if self.selected_numbers[0] == word.number else Color.black
            size = self.font.size(text)
            pygame.draw.rect(self.screen, Color.white, pygame.Rect(dest[0], dest[1], size[0], size[1]), 0)
            draw_text(self.screen, self.font, dest[0], dest[1], text, color)

        row_top_offset += 100

        dest = (row_left_offset, row_top_offset)
        size = self.font.size(v_title)
        pygame.draw.rect(self.screen, Color.white, pygame.Rect(dest[0], dest[1], size[0], size[1]), 0)
        self.font.set_bold(True)
        self.font.set_underline(True)
        draw_text(self.screen, self.font, dest[0], dest[1], v_title, Color.black)
        self.font.set_bold(False)
        self.font.set_underline(False)

        for word in v_words:
            row_top_offset += 60
            dest = (row_left_offset, row_top_offset)
            text = reverse_word(str(word.number) + '. ' + word.q)
            color = Color.green if self.selected_numbers[1] == word.number else Color.black
            size = self.font.size(text)
            pygame.draw.rect(self.screen, Color.white, pygame.Rect(dest[0], dest[1], size[0], size[1]), 0)
            draw_text(self.screen, self.font, dest[0], dest[1], text, color)

    def _get_words_by_direction(self, direction):
        dir_words = []
        for word in self.words:
            if word.direction == direction:
                dir_words.append(word)
        return dir_words
