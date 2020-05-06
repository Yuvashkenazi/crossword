LEFT_OFFSET = 150
TOP_OFFSET = 75


def get_coordinates_from_grid(row, col):
    return LEFT_OFFSET + col * 25, TOP_OFFSET + row * 25


def cells_distance(cell1, cell2):
    x = cell1.col - cell2.col
    y = cell1.row - cell2.row
    distance = (x ** 2 + y ** 2) ** 0.5
    return distance