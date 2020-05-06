from enum import Enum
import pygame


class Languages(Enum):
    EN = 1
    HE = 2


class Colors:
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (92, 184, 92)
    purple = (89, 0, 178)


UP = 273
DOWN = 274
RIGHT = 275
LEFT = 276
ARROWS = [UP, DOWN, RIGHT, LEFT]

SPACE = 32
ENTER = 13
ESC = 27
DEL = 127
BK_SPACE = 8

LANGUAGES = {
    'EN': 0,
    'HE': 1
}

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

LETTERS_EN2 = {
    47: 'Q',
    39: 'W',
    247: 'E',
    248: 'R',
    224: 'T',
    232: 'Y',
    229: 'U',
    239: 'I',
    237: 'O',
    244: 'P',
    249: 'A',
    227: 'S',
    226: 'D',
    235: 'F',
    242: 'G',
    233: 'H',
    231: 'J',
    236: 'K',
    234: 'L',
    230: 'Z',
    241: 'X',
    225: 'C',
    228: 'V',
    240: 'B',
    238: 'N',
    246: 'M',
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

LETTERS_HE2 = {
    247: 'ק',
    248: 'ר',
    224: 'א',
    232: 'ט',
    229: 'ו',
    # 239: 'ן',
    # 237: 'ם',
    244: 'פ',
    249: 'ש',
    227: 'ד',
    226: 'ג',
    235: 'כ',
    242: 'ע',
    233: 'י',
    231: 'ח',
    236: 'ל',
    # 234: 'ך',
    # 243: 'ף',
    230: 'ז',
    241: 'ס',
    225: 'ב',
    228: 'ה',
    240: 'נ',
    238: 'מ',
    246: 'צ',
    250: 'ת',
    # 245: 'ץ',
}
