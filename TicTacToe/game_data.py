game_squares = []

def draw_x(board, row, column):
    y_coord = row * 150 - 75
    x_coord = column * 150 - 75
    element = board.DrawLine((x_coord - 50, y_coord - 50), (x_coord + 50, y_coord + 50), color='blue', width=5)
    game_squares.append(element)
    element = board.DrawLine((x_coord - 50, y_coord + 50), (x_coord + 50, y_coord - 50), color='blue', width=5)
    game_squares.append(element)

def draw_o(board, row, column):
    y_coord = row * 150 - 75
    x_coord = column * 150 - 75
    element = board.DrawCircle((x_coord, y_coord), 50, line_color='red', line_width=5)
    game_squares.append(element)

def erase_board(board):
    for element in game_squares:
        board.DeleteFigure(element)

    game_squares.clear()
