import PySimpleGUI as sg
import game_functions
import game_data

#############################################################################################
#                                                                                           #
#   Local test code                                                                         #
#                                                                                           #
#############################################################################################

if __name__ == '__main__':
    main_layout = [[sg.Text('Robot Battle', size=(40, 1), key='-graph_title-', font=('Helvetica', 14))],
                   [sg.Graph(canvas_size=((game_data.f_length * 2) + 10, (game_data.f_height * 2) + 10), graph_bottom_left=(-5, -5),
                             graph_top_right=(game_data.f_length + 5, game_data.f_height + 5),
                             background_color='white', key='-field-')],
                   [sg.Button('Exit', size=(12, 1)), sg.Button('Jackson Start', size=(12,1), button_color=('white', 'blue')),
                    sg.Button('Dad Start', size=(12,1), button_color=('white', 'red')), sg.Button('Setup Robots', size=(12,1))]
                   ]

    playing_field = sg.Window('Robot Battle', main_layout, finalize=True)
    board_graph = playing_field['-field-']
#
#   Draw the board
#
    board_graph.DrawLine((0, 0), (game_data.f_length, 0))                                           # bottom line
    board_graph.DrawLine((game_data.f_length, 0), (game_data.f_length, game_data.f_height))         # right line
    board_graph.DrawLine((game_data.f_length, game_data.f_height), (0, game_data.f_height))         # top line
    board_graph.DrawLine((0, game_data.f_height), (0,0))                                            # left line
    game_data.main_gui = playing_field

    while True:  # Event Loop
        event, values = playing_field.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Setup Robots':
            game_functions.setup_game(board_graph)
        elif event == 'Jackson Start':
            game_functions.start_game(board_graph, 'Jackson')
        elif event == 'Dad Start':
            game_functions.start_game(board_graph, 'Dad')

    playing_field.close()
