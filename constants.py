import pygame

CROSSWORD_SIZE = 16


class Language:
    EN = 1
    HE = 2


class Color:
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (92, 184, 92)
    purple = (89, 0, 178)


class Direction:
    vertical = 'v'
    horizontal = 'h'


UP = pygame.K_UP
DOWN = pygame.K_DOWN
RIGHT = pygame.K_RIGHT
LEFT = pygame.K_LEFT
ARROWS = [UP, DOWN, RIGHT, LEFT]

SPACE = pygame.K_SPACE
ENTER = pygame.K_RETURN
ESC = pygame.K_ESCAPE
DEL = pygame.K_DELETE
BACKSPACE = pygame.K_BACKSPACE
ESCAPE= pygame.K_ESCAPE

LETTERS_EN = {
    pygame.K_q: 'Q',
    pygame.K_w: 'W',
    pygame.K_e: 'E',
    pygame.K_r: 'R',
    pygame.K_t: 'T',
    pygame.K_y: 'Y',
    pygame.K_u: 'U',
    pygame.K_i: 'I',
    pygame.K_o: 'O',
    pygame.K_p: 'P',
    pygame.K_a: 'A',
    pygame.K_s: 'S',
    pygame.K_d: 'D',
    pygame.K_f: 'F',
    pygame.K_g: 'G',
    pygame.K_h: 'H',
    pygame.K_j: 'J',
    pygame.K_k: 'K',
    pygame.K_l: 'L',
    pygame.K_z: 'Z',
    pygame.K_x: 'X',
    pygame.K_c: 'C',
    pygame.K_v: 'V',
    pygame.K_b: 'B',
    pygame.K_n: 'N',
    pygame.K_m: 'M',
}


LETTERS_HE = {
    pygame.K_e: 'ק',
    pygame.K_r: 'ר',
    pygame.K_t: 'א',
    pygame.K_y: 'ט',
    pygame.K_u: 'ו',
    pygame.K_i: 'נ',
    pygame.K_o: 'מ',
    pygame.K_p: 'פ',
    pygame.K_a: 'ש',
    pygame.K_s: 'ד',
    pygame.K_d: 'ג',
    pygame.K_f: 'כ',
    pygame.K_g: 'ע',
    pygame.K_h: 'י',
    pygame.K_j: 'ח',
    pygame.K_k: 'ל',
    pygame.K_l: 'כ',
    pygame.K_SEMICOLON: 'פ',
    pygame.K_z: 'ז',
    pygame.K_x: 'ס',
    pygame.K_c: 'ב',
    pygame.K_v: 'ה',
    pygame.K_b: 'נ',
    pygame.K_n: 'מ',
    pygame.K_m: 'צ',
    pygame.K_COMMA: 'ת',
    pygame.K_PERIOD: 'צ'
}
