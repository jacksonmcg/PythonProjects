import map_lists
import map_functions
import time

##############################################################################
#                                                                            #
#   Available functions                                                      #
#       get_borders(map_list.KENTUCKY[0])                                    #
#           call function with state index                                   #
#           returns a list of states that border the passed state            #
#                                                                            #
#       get_state_color(map_lists.SOUTHCAROLNA[0])                           #
#           returns the current color of a state.  'white' means not colored #
#                                                                            #
#       color_state(us_map, map_lists.CALIFORNIA[0], 'blue')                 #
#           must pass the map of the US and the state index                  #
#           this function will color the actual map                          #
#           to 'clear' a state, color it white                               #
#                                                                            #
#       get_state_name(state_index)                                          #
#           call function with state index                                   #
#           returns the name of a state                                      #
#                                                                            #
##############################################################################

def colorBorder(us_map, state, counter, borders, parsedStates, colorCounter):

    rd = False
    bl = False
    yl = False
    gr = False
    stop = False

    for states in range(0,48):
        color = map_functions.get_state_color(states)
        if color == 'white' :
            break
        elif states == 47:
            return
    if stop == True:
        return
    else:
        if map_functions.get_state_color(state) == 'white':
            recentBorder = state
            list_border = map_functions.get_borders(recentBorder)
            count = 0
            while count < len(list_border):
                if(map_functions.get_state_color(list_border[count][0]) == 'red') :
                    rd = True
                if(map_functions.get_state_color(list_border[count][0]) == 'blue') :
                    bl = True
                if (map_functions.get_state_color(list_border[count][0]) == 'yellow'):
                    yl = True
                if (map_functions.get_state_color(list_border[count][0]) == 'green'):
                    gr = True
                count += 1

            if colorCounter == 4:
                map_functions.get_state_color(state) == 'white'
            elif colorCounter == 3:
                if gr == False:
                    map_functions.color_state(us_map, state, 'green')
                else:
                    map_functions.get_state_color(state) == 'white'
            elif colorCounter == 2:
                if yl == False:
                    map_functions.color_state(us_map, state, 'yellow')
                elif gr == False:
                    map_functions.color_state(us_map, state, 'green')
                else:
                    map_functions.get_state_color(state) == 'white'
            elif colorCounter == 1:
                if bl == False:
                    map_functions.color_state(us_map, state, 'blue')
                elif yl == False:
                    map_functions.color_state(us_map, state, 'yellow')
                elif gr == False:
                    map_functions.color_state(us_map, state, 'green')
                else:
                    map_functions.get_state_color(state) == 'white'
            else:
                if rd == False:
                    map_functions.color_state(us_map, state, 'red')
                elif bl == False :
                    map_functions.color_state(us_map, state, 'blue')
                elif yl == False:
                    map_functions.color_state(us_map, state, 'yellow')
                elif gr == False:
                    map_functions.color_state(us_map, state, 'green')

            parsedStates.append(state)
            if map_functions.get_state_color(state) == 'white' :
                parsedStates.pop()
                if map_functions.get_state_color(parsedStates[-1]) == 'green':
                    colorCounter = 4
                elif map_functions.get_state_color(parsedStates[-1]) == 'yellow':
                    colorCounter = 3
                elif map_functions.get_state_color(parsedStates[-1]) == 'blue':
                    colorCounter = 2
                elif map_functions.get_state_color(parsedStates[-1]) == 'red':
                    colorCounter = 1
                sys = parsedStates.pop()
                list_border = map_functions.get_borders(sys)
                map_functions.color_state(us_map, sys, 'white')
                colorBorder(us_map, sys, 0, list_border, parsedStates, colorCounter)
            else:
                colorCounter = 0
                colorBorder(us_map, list_border[0][0], 0, list_border, parsedStates, colorCounter)
        else:
            re = 0
            try:
                counter = counter + 1
                colorCounter = 0
                colorBorder(us_map, borders[counter][0], counter, borders, parsedStates, colorCounter)
            except IndexError:
                recent = parsedStates.pop()
                colorCounter = 0
                list_border = map_functions.get_borders(recent)
                colorBorder(us_map, recent, 0, list_border, parsedStates, colorCounter)

def color_map(us_map):
    print('Write code to color the Map here')
    map_functions.color_state(us_map, map_lists.WASHINGTON[0], 'red')
    list_border = map_functions.get_borders(map_lists.WASHINGTON[0])
    colorBorder(us_map, list_border[0][0], 0, list_border, [], 0)