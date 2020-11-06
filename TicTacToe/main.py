import PySimpleGUI as sg
import game_functions
import game_data
#import map_lists
#import coloring_algorithm

#############################################################################################
#                                                                                           #
#   Local test code                                                                         #
#                                                                                           #
#############################################################################################

if __name__ == '__main__':

    main_layout = [[sg.Text('Tic-Tac-Toe', size=(40, 1), key='-graph_title-', font=('Helvetica', 14))],
                   [sg.Graph(canvas_size=(456, 456), graph_bottom_left=(-3, 453), graph_top_right=(453, -3),
                             background_color='white', key='-tic_tac-')],
                   [sg.Button('Exit', size=(10, 1)), sg.Button('User Start', size=(10,1)),
                    sg.Button('App Start', size=(10,1)), sg.Button('COM Game', size=(10,1)),  sg.Button('Clear Board', size=(10,1))]
                   ]

    board = sg.Window('Tic-Tac-Toe Program', main_layout, finalize=True)
    board_graph = board['-tic_tac-']
#
#   Draw the board
#
    board_graph.DrawLine((0,0), (450,0))        # top line
    board_graph.DrawLine((450,0), (450,450))    # right line
    board_graph.DrawLine((450,450), (0,450))    # bottom line
    board_graph.DrawLine((0,450), (0,0))        # left line

    board_graph.DrawLine((0,150), (450,150))
    board_graph.DrawLine((0,300), (450,300))

    board_graph.DrawLine((150,0), (150,450))
    board_graph.DrawLine((300,0), (300,450))

    while True:  # Event Loop
        event, values = board.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'User Start':
            game_functions.start_game(board_graph, 'user')
        elif event == 'App Start':
            game_functions.start_game(board_graph, 'com')
        elif event == 'COM Game':
            game_functions.start_game(board_graph, 'app')
        elif event == 'Clear Board':
            game_data.erase_board(board_graph)

    board.close()
