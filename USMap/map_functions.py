import map_lists

def get_borders(state_index):
    return map_lists.usa_borders[state_index]

def get_state_color(state_index):
    current_color = map_lists.color_grid[state_index]
    return current_color

def color_state(us_plot, state_index, color):
    us_plot.DeleteFigure(map_lists.state_objects[state_index][0])
    us_plot.DeleteFigure(map_lists.state_objects[state_index][1])

    new_poly = us_plot.DrawPolygon(map_lists.state_pts[state_index], line_color='black', line_width=1, fill_color=color)
    new_name = us_plot.DrawText(map_lists.state_name[state_index][0], map_lists.state_name[state_index][1],
                       color='black', font=('Helvetica', 12, 'bold'))
    map_lists.state_objects[state_index] = (new_poly, new_name)

    map_lists.color_grid[state_index] = color
    map_lists.main_gui.Refresh()

def clear_map(us_map):
    for index1 in range(0,48):
        map_lists.color_grid[index1] = 'uncolored'
        color_state(us_map, index1, 'white')

def get_state_name(state_index):
    sname = map_lists.states_50[state_index][1]
    return sname

#############################################################################################
#                                                                                           #
#   Local test code                                                                         #
#                                                                                           #
#############################################################################################

if __name__ == '__main__':

    get_state_color(12)
