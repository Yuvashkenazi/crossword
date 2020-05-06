LEFT_OFFSET = 150
TOP_OFFSET = 75


def get_coordinates_from_grid(row, col):
    return LEFT_OFFSET + col * 25, TOP_OFFSET + row * 25
