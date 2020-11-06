import PySimpleGUI as sg
import map_functions
import map_lists
import coloring_algorithm

#############################################################################################
#                                                                                           #
#   Local test code                                                                         #
#                                                                                           #
#############################################################################################

if __name__ == '__main__':

    main_layout = [[sg.Text('USA Map', size=(50, 1), key='-graph_title-', font=('Helvetica', 14))],
                   [sg.Graph(canvas_size=(1100, 650), graph_bottom_left=(0, 0), graph_top_right=(1100, 650),
                             background_color='white', key='-usa_map-')],
                   [sg.Button('Exit', size=(10, 1)), sg.Button('Start Coloring', size=(15,1)),
                    sg.Button('Clear Map', size=(15,1))]
                   ]

    map_win = sg.Window('USA Map Color Program', main_layout, finalize=True)
    map_lists.main_gui = map_win
    map_graph = map_win['-usa_map-']
#
#   Draw US Map
#
    for us_state in range(0,48):
        polyobj = map_graph.DrawPolygon(map_lists.state_pts[us_state], line_color='black', line_width=1, fill_color='white')
        polyname = map_graph.DrawText(map_lists.state_name[us_state][0], map_lists.state_name[us_state][1],
                           color='black', font=('Helvetica', 12, 'bold'))
        map_lists.state_objects.append((polyobj, polyname))
#
#   Set all states to have no color at the start and save state names
#
    for index1 in range(0,48):
        map_lists.color_grid.append('white')

    time_out = 0
    state_ctr = 0
    while True:  # Event Loop
        event, values = map_win.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Start Coloring':
            coloring_algorithm.color_map(map_graph)
        elif event == 'Clear Map':
            map_functions.clear_map(map_graph)

    map_win.close()
