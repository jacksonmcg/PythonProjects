import game_data
import random
import PySimpleGUI as sg
import time

def isSpaceFull(space, fill) :
    count = 0
    while count < len(fill):
        if fill[count] == space:
            return True
        count += 1
    return False

def user_turn(board, fill):
    grid_layout = [
        [sg.Text('Row and Column')],
        [sg.Text('Row', size=(5, 1)), sg.InputText(size=(3,1))],
        [sg.Text('Column', size=(5, 1)), sg.InputText(size=(3,1))],
        [sg.Button('Enter')]
    ]
    user_ask = sg.Window('User Input', grid_layout)

    while True:
        event, values = user_ask.read()
        break
    user_ask.close()

    row = int(values[0])
    column = int(values[1])
    space = (column - 1) * 3 + row

    if isSpaceFull(space, fill) == False :
        game_data.draw_x(board, row, column)
        return space
    else:
        t = user_turn(board, fill)
        return t

def goMiddle(fill):
    count = 0
    while count < len(fill):
        if fill[count] == 5:
            return True
        count += 1
    return False

def determineComSpace(x_spaces, y_spaces):
    count1 = 0
    x = [False, False, False, False, False, False, False, False, False, False]
    # print(len(y_spaces))
    while count1 < len(x_spaces):
        if x_spaces[count1] == 1:
            x[1] = True
        elif x_spaces[count1] == 2:
            x[2] = True
        elif x_spaces[count1] == 3:
            x[3] = True
        elif x_spaces[count1] == 4:
            x[4] = True
        elif x_spaces[count1] == 5:
            x[5] = True
        elif x_spaces[count1] == 6:
            x[6] = True
        elif x_spaces[count1] == 7:
            x[7] = True
        elif x_spaces[count1] == 8:
            x[8] = True
        elif x_spaces[count1] == 9:
            x[9] = True
        count1 += 1

    count2 = 0
    y = [False, False, False, False, False, False, False, False, False, False]
    # print(len(y_spaces))
    while count2 < len(y_spaces):
        if y_spaces[count2] == 1:
            x[1] = True
        elif y_spaces[count2] == 2:
            x[2] = True
        elif y_spaces[count2] == 3:
            y[3] = True
        elif y_spaces[count2] == 4:
            y[4] = True
        elif y_spaces[count2] == 5:
            y[5] = True
        elif y_spaces[count2] == 6:
            y[6] = True
        elif y_spaces[count2] == 7:
            y[7] = True
        elif y_spaces[count2] == 8:
            y[8] = True
        elif y_spaces[count2] == 9:
            y[9] = True
        count2 += 1

    if y[1] and y[2] and not(x[3]) and not(y[3]):
        return 3
    elif y[1] and y[3] and not(x[2]) and not(x[2]):
        return 2
    elif y[2] and y[3] and not(x[1]) and not(x[1]):
        return 1
    elif y[1] and y[4] and not(x[7]) and not(y[7]):
        return 7
    elif y[4] and y[7] and not(x[1]) and not(x[1]):
        return 1
    elif y[7] and y[1] and not(x[4]) and not(x[5]):
        return 4
    elif y[1] and y[5] and not(x[9]) and not(y[5]):
        return 9
    elif y[5] and y[9] and not(x[1]) and not(y[5]):
        return 1
    elif y[9] and y[1] and not(x[5]) and not(y[8]):
        return 5
    elif y[2] and y[5] and not(x[8]) and not(y[8]):
        return 8
    elif y[5] and y[8] and not(x[2]) and not(y[2]):
        return 2
    elif y[8] and y[2] and not(x[5]) and not(y[5]):
        return 5
    elif y[6] and y[9] and not(x[3]) and not(y[3]):
        return 3
    elif y[3] and y[9] and not(x[6]) and not(y[6]):
        return 6
    elif y[3] and y[6] and not(x[9]) and not(y[9]):
        return 9
    elif y[5] and y[7] and not(x[3]) and not(y[3]):
        return 3
    elif y[3] and y[7] and not(x[5]) and not(y[5]):
        return 5
    elif y[3] and y[5] and not(x[7]) and not(y[7]):
        return 7
    elif y[5] and y[6] and not(x[4]) and not(y[4]):
        return 4
    elif y[4] and y[6] and not(x[5]) and not(y[5]):
        return 5
    elif y[4] and y[5] and not(x[6]) and not(y[6]):
        return 6
    elif y[8] and y[9] and not(x[7]) and not(y[7]):
        return 7
    elif y[7] and y[8] and not(x[8]) and not(y[8]):
        return 8
    elif y[7] and y[8] and not(x[9]) and not(y[9]):
        return 9
    elif x[1] and x[2] and not(x[3]) and not(y[3]):
        return 3
    elif x[1] and x[3] and not(x[2]) and not(y[2]):
        return 2
    elif x[2] and x[3] and not(x[1]) and not(y[1]):
        return 1
    elif x[1] and x[4] and not(x[7]) and not(y[7]):
        return 7
    elif x[4] and x[7] and not(x[1]) and not(y[7]):
        return 1
    elif x[7] and x[1] and not(x[4]) and not(y[4]):
        return 4
    elif x[1] and x[5] and not(x[9]) and not(y[9]):
        return 9
    elif x[5] and x[9] and not(x[1]) and not(y[1]):
        return 1
    elif x[9] and x[1] and not(x[5]) and not(y[5]):
        return 5
    elif x[2] and x[5] and not(x[8]) and not(y[8]):
        return 8
    elif x[5] and x[8] and not(x[2]) and not(y[2]):
        return 2
    elif x[8] and x[2] and not(x[5]) and not(y[5]):
        return 5
    elif x[6] and x[9] and not(x[3]) and not(y[3]):
        return 3
    elif x[3] and x[9] and not(x[6]) and not(y[6]):
        return 6
    elif x[3] and x[6] and not(x[9]) and not(y[9]):
        return 9
    elif x[5] and x[7] and not(x[3]) and not(y[3]):
        return 3
    elif x[3] and x[7] and not(x[5]) and not(y[5]):
        return 5
    elif x[3] and x[5] and not(x[7]) and not(y[7]):
        return 7
    elif x[5] and x[6] and not(x[4]) and not(y[4]):
        return 4
    elif x[4] and x[6] and not(x[5]) and not(y[5]):
        return 5
    elif x[4] and x[5] and not(x[6]) and not(y[6]):
        return 6
    elif x[8] and x[9] and not(x[7]) and not(y[7]):
        return 7
    elif x[7] and x[8] and not(x[8]) and not(y[8]):
        return 8
    elif x[7] and x[8] and not(x[9]) and not(y[9]):
        return 9
    else:
        return 0

def computer_turn(board, row, column, fill, x_spaces, y_spaces):
    if(goMiddle(fill) == False):
        row = 2
        column = 2
        space = 5
    else:
        space = (column - 1) * 3 + row

    space2 = determineComSpace(x_spaces, y_spaces)

    if(space2 != 0):
        row = space2 % 3
        if(row == 0):
            row = 3
        if space2 < 4 :
            column = 1
        elif space2 < 7 :
            column = 2
        else :
            column = 3
        space = space2
    else:
        space = (column - 1) * 3 + row

    if isSpaceFull(space, fill) == False :
        game_data.draw_o(board, row, column)
        return space
    else:
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        t = computer_turn(board, x, y, fill, x_spaces, y_spaces)
        return t

def computer_turn_x(board, row, column, fill, x_spaces, y_spaces):
    if(goMiddle(fill) == False):
        row = 2
        column = 2
        space = 5
    else:
        space = (column - 1) * 3 + row

    space2 = determineComSpace(x_spaces, y_spaces)

    if(space2 != 0):
        row = space2 % 3
        if(row == 0):
            row = 3
        if space2 < 4 :
            column = 1
        elif space2 < 7 :
            column = 2
        else :
            column = 3
        space = space2
    else:
        space = (column - 1) * 3 + row

    if isSpaceFull(space, fill) == False :
        game_data.draw_x(board, row, column)
        return space
    else:
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        t = computer_turn_x(board, x, y, fill, x_spaces, y_spaces)
        return t

def win_con(x_spaces, y_spaces):
    count1 = 0
    x = [False, False, False, False, False, False, False, False, False, False]
    #print(len(y_spaces))
    while count1 < len(x_spaces):
        if x_spaces[count1] == 1:
            x[1] = True
        elif x_spaces[count1] == 2:
            x[2] = True
        elif x_spaces[count1] == 3:
            x[3] = True
        elif x_spaces[count1] == 4:
            x[4] = True
        elif x_spaces[count1] == 5:
            x[5] = True
        elif x_spaces[count1] == 6:
            x[6] = True
        elif x_spaces[count1] == 7:
            x[7] = True
        elif x_spaces[count1] == 8:
            x[8] = True
        elif x_spaces[count1] == 9:
            x[9] = True
        count1 += 1

    # print(x)

    if x[1] and x[2] and x[3]:
        print("X wins!")
        return True
    if x[1] and x[4] and x[7]:
        print("X wins!")
        return True
    if x[1] and x[5] and x[9]:
        print("X wins!")
        return True
    if x[2] and x[5] and x[8]:
        print("X wins!")
        return True
    if x[3] and x[6] and x[9]:
        print("X wins!")
        return True
    if x[3] and x[5] and x[7]:
        print("X wins!")
        return True
    if x[4] and x[5] and x[6]:
        print("X wins!")
        return True
    if x[7] and x[8] and x[9]:
        print("X wins!")
        return True

    ##############################################

    count2 = 0

    y = [False, False, False, False, False, False, False, False, False, False]
    #print(len(y_spaces))
    while count2 < len(y_spaces):
        if y_spaces[count2] == 1:
            y[1] = True
        elif y_spaces[count2] == 2:
            y[2] = True
        elif y_spaces[count2] == 3:
            y[3] = True
        elif y_spaces[count2] == 4:
            y[4] = True
        elif y_spaces[count2] == 5:
            y[5] = True
        elif y_spaces[count2] == 6:
            y[6] = True
        elif y_spaces[count2] == 7:
            y[7] = True
        elif y_spaces[count2] == 8:
            y[8] = True
        elif y_spaces[count2] == 9:
            y[9] = True
        count2 += 1

    #print(y)

    if y[1] and y[2] and y[3] :
        print("O wins!")
        return True
    if y[1] and y[4] and y[7]:
        print("O wins!")
        return True
    if y[1] and y[5] and y[9]:
        print("O wins!")
        return True
    if y[2] and y[5] and y[8] :
        print("O wins!")
        return True
    if y[3] and y[6] and y[9] :
        print("O wins!")
        return True
    if y[3] and y[5] and y[7] :
        print("O wins!")
        return True
    if y[4] and y[5] and y[6]:
        print("O wins!")
        return True
    if y[7] and y[8] and y[9]:
        print("O wins!")
        return True

    # print('----------------------')
    return False


#############################################################################
#                                                                           #
#   Code to play the game goes below here                                   #
#                                                                           #
#############################################################################

#############################################################################

def start_game(board, first_turn):

    count = 0
    filledSpaces = []
    x_spaces = []
    y_spaces = []

    while count < 9 :
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        if first_turn == 'user':
            # print('the user goes first')
            if(count%2 == 0):
                space = user_turn(board, filledSpaces)
                # print(space)
                filledSpaces.append(space)
                x_spaces.append(space)
                #print(x_spaces)
            else:
                space = computer_turn(board, x, y, filledSpaces, x_spaces, y_spaces)
                filledSpaces.append(space)
                y_spaces.append(space)
                #print(y_spaces)

            if win_con(x_spaces, y_spaces):
                break
        if first_turn == 'com':
            # print('the user goes first')
            if(count%2 == 0):
                space = computer_turn(board, x, y, filledSpaces, x_spaces, y_spaces)
                filledSpaces.append(space)
                y_spaces.append(space)
                #print(y_spaces)
            else:
                space = user_turn(board, filledSpaces)
                # print(space)
                filledSpaces.append(space)
                x_spaces.append(space)
                #print(x_spaces)


            if win_con(x_spaces, y_spaces):
                break
        else :
            # print('the user goes first')
            if (count % 2 == 0):
                space = computer_turn(board, x, y, filledSpaces, x_spaces, y_spaces)
                filledSpaces.append(space)
                y_spaces.append(space)
                # print(y_spaces)
            else:
                space = computer_turn_x(board, x, y, filledSpaces, x_spaces, y_spaces)
                filledSpaces.append(space)
                x_spaces.append(space)
                # print(x_spaces)

            if win_con(x_spaces, y_spaces):
                break


        # print('x - ' + str(x_spaces))
        # print('o - ' + str(y_spaces))
        # print('--------------')

        count += 1
