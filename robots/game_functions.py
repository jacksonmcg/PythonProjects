import random
import game_data
import dad_robots
import jackson_robots
import time

def execute_cmd(robot, cmd_data, user, field):
    response = None
    if user == game_data.DAD and cmd_data[0] != 0:
        if game_data.red_element[robot] != 0:
            field.DeleteFigure(game_data.red_element[robot])
            game_data.main_gui.Refresh()
            game_data.red_element[robot] = 0

        next_command = cmd_data[0]
        if next_command == game_data.MOVE:
            dad_move(field,robot, cmd_data[1])
            game_data.red_element[robot] = 0
        elif next_command == game_data.LOOK:
            response = robot_look(robot, cmd_data[1], user)
            game_data.red_element[robot] = 0
        elif next_command == game_data.SHOOT:
            element = robot_shoot(field, robot, cmd_data[1], user)
            game_data.red_element[robot] = element
        time.sleep(game_data.time_delay)

    elif user == game_data.JACKSON and cmd_data[0] != 0:
        if game_data.blue_element[robot] != 0:
            field.DeleteFigure(game_data.blue_element[robot])
            game_data.main_gui.Refresh()
            game_data.blue_element[robot] = 0

        next_command = cmd_data[0]
        if next_command == game_data.MOVE:
            response = jackson_move(field,robot, cmd_data[1])
        elif next_command == game_data.LOOK:
            response = robot_look(robot, cmd_data[1], user)
        elif next_command == game_data.SHOOT:
            response = robot_shoot(field, robot, cmd_data[1], user)
            game_data.blue_element[robot] = response
        time.sleep(game_data.time_delay)

    return response

def setup_game(field_of_play):
    if len(game_data.blue_positions) > 0:
        for robot in game_data.blue_positions:
            field_of_play.DeleteFigure(robot[1])

    if len(game_data.red_positions) > 0:
        for robot in game_data.red_positions:
            field_of_play.DeleteFigure(robot[1])

    for robot in range(0,5):
        rand_x = random.randrange(0, game_data.f_length + 1)
        rand_y = random.randrange(0, game_data.f_height + 1)
        draw_blue(field_of_play, robot, rand_x, rand_y)

    for robot in range(0, 5):
        rand_x = random.randrange(0, game_data.f_length + 1)
        rand_y = random.randrange(0, game_data.f_height + 1)
        draw_red(field_of_play, robot, rand_x, rand_y)

def draw_blue(field, robot, x_coord, y_coord):
    element = field.DrawCircle((x_coord, y_coord), 3, line_color='black', fill_color='blue')
    game_data.blue_positions[robot] = (robot, element, x_coord, y_coord, True)
    game_data.main_gui.Refresh()

def draw_red(field, robot, x_coord, y_coord):
    element = field.DrawCircle((x_coord, y_coord), 3, line_color='black', fill_color='red')
    game_data.red_positions[robot] = (robot, element, x_coord, y_coord, True)
    game_data.main_gui.Refresh()

def jackson_move(field, robot, direction):
    moving_robot = game_data.blue_positions[robot]
    if direction == game_data.NORTH_DIR:
        if moving_robot[3] < game_data.f_height:
            field.DeleteFigure(moving_robot[1])
            draw_blue(field, robot, moving_robot[2], moving_robot[3] + 1)
            check_robot(game_data.JACKSON, moving_robot[0], moving_robot[2], moving_robot[3] + 1, field)
            game_data.main_gui.Refresh()
    if direction == game_data.NE_DIR:
        if moving_robot[2] < game_data.f_length and moving_robot[3] < game_data.f_height:
            field.DeleteFigure(moving_robot[1])
            draw_blue(field, robot, moving_robot[2] + 1, moving_robot[3] + 1)
            check_robot(game_data.JACKSON, moving_robot[0], moving_robot[2] + 1, moving_robot[3] + 1, field)
            game_data.main_gui.Refresh()
    if direction == game_data.EAST_DIR:
        if moving_robot[2] < game_data.f_length:
            field.DeleteFigure(moving_robot[1])
            draw_blue(field, robot, moving_robot[2] + 1, moving_robot[3])
            check_robot(game_data.JACKSON, moving_robot[0], moving_robot[2] + 1, moving_robot[3], field)
    if direction == game_data.SE_DIR:
        if moving_robot[2] < game_data.f_length and moving_robot[3] > 0:
            field.DeleteFigure(moving_robot[1])
            draw_blue(field, robot, moving_robot[2] + 1, moving_robot[3] - 1)
            check_robot(game_data.JACKSON, moving_robot[0], moving_robot[2] + 1, moving_robot[3] - 1, field)
    if direction == game_data.SOUTH_DIR:
        if moving_robot[3] > 0:
            field.DeleteFigure(moving_robot[1])
            draw_blue(field, robot, moving_robot[2], moving_robot[3] - 1)
            check_robot(game_data.JACKSON, moving_robot[0], moving_robot[2], moving_robot[3] - 1, field)
    if direction == game_data.SW_DIR:
        if moving_robot[2] > 0 and moving_robot[3] > 0:
            field.DeleteFigure(moving_robot[1])
            draw_blue(field, robot, moving_robot[2] - 1, moving_robot[3] - 1)
            check_robot(game_data.JACKSON, moving_robot[0], moving_robot[2] - 1, moving_robot[3] - 1, field)
    if direction == game_data.WEST_DIR:
        if moving_robot[2] > 0:
            field.DeleteFigure(moving_robot[1])
            draw_blue(field, robot, moving_robot[2] - 1, moving_robot[3])
            check_robot(game_data.JACKSON, moving_robot[0], moving_robot[2] - 1, moving_robot[3], field)
            game_data.main_gui.Refresh()
    if direction == game_data.NW_DIR:
        if moving_robot[2] > 0 and moving_robot[3] < game_data.f_height:
            field.DeleteFigure(moving_robot[1])
            draw_blue(field, robot, moving_robot[2] - 1, moving_robot[3] + 1)
            check_robot(game_data.JACKSON, moving_robot[0], moving_robot[2] - 1, moving_robot[3] + 1, field)
            game_data.main_gui.Refresh()

def dad_move(field, robot, direction):
    moving_robot = game_data.red_positions[robot]
    if direction == game_data.NORTH_DIR:
        if moving_robot[3] < game_data.f_height:
            field.DeleteFigure(moving_robot[1])
            draw_red(field, robot, moving_robot[2], moving_robot[3] + 1)
            check_robot(game_data.DAD, moving_robot[0], moving_robot[2], moving_robot[3] + 1, field)
            game_data.main_gui.Refresh()
    if direction == game_data.NE_DIR:
        if moving_robot[2] < game_data.f_length and moving_robot[3] < game_data.f_height:
            field.DeleteFigure(moving_robot[1])
            draw_red(field, robot, moving_robot[2] + 1, moving_robot[3] + 1)
            check_robot(game_data.DAD, moving_robot[0], moving_robot[2] + 1, moving_robot[3] + 1, field)
            game_data.main_gui.Refresh()
    if direction == game_data.EAST_DIR:
        if moving_robot[2] < game_data.f_length:
            field.DeleteFigure(moving_robot[1])
            draw_red(field, robot, moving_robot[2] + 1, moving_robot[3])
            check_robot(game_data.DAD, moving_robot[0], moving_robot[2] + 1, moving_robot[3], field)
            game_data.main_gui.Refresh()
    if direction == game_data.SE_DIR:
        if moving_robot[2] < game_data.f_length and moving_robot[3] > 0:
            field.DeleteFigure(moving_robot[1])
            draw_red(field, robot, moving_robot[2] + 1, moving_robot[3] - 1)
            check_robot(game_data.DAD, moving_robot[0], moving_robot[2] + 1, moving_robot[3] - 1, field)
            game_data.main_gui.Refresh()
    if direction == game_data.SOUTH_DIR:
        if moving_robot[3] > 0:
            field.DeleteFigure(moving_robot[1])
            draw_red(field, robot, moving_robot[2], moving_robot[3] - 1)
            check_robot(game_data.DAD, moving_robot[0], moving_robot[2], moving_robot[3] - 1, field)
            game_data.main_gui.Refresh()
    if direction == game_data.SW_DIR:
        if moving_robot[2] > 0 and moving_robot[3] > 0:
            field.DeleteFigure(moving_robot[1])
            draw_red(field, robot, moving_robot[2] - 1, moving_robot[3] - 1)
            check_robot(game_data.DAD, moving_robot[0], moving_robot[2] - 1, moving_robot[3] - 1, field)
            game_data.main_gui.Refresh()
    if direction == game_data.WEST_DIR:
        if moving_robot[2] > 0:
            field.DeleteFigure(moving_robot[1])
            draw_red(field, robot, moving_robot[2] - 1, moving_robot[3])
            check_robot(game_data.DAD, moving_robot[0], moving_robot[2] - 1, moving_robot[3], field)
            game_data.main_gui.Refresh()
    if direction == game_data.NW_DIR:
        if moving_robot[2] > 0 and moving_robot[3] < game_data.f_height:
            field.DeleteFigure(moving_robot[1])
            draw_red(field, robot, moving_robot[2] - 1, moving_robot[3] + 1)
            check_robot(game_data.DAD, moving_robot[0], moving_robot[2] - 1, moving_robot[3] + 1, field)
            game_data.main_gui.Refresh()

def robot_look(robot, direction, user):
    response = [0, 0, game_data.NOTHING, 0]
    if user == game_data.DAD:
        moving_robot = game_data.red_positions[robot]
    else:
        moving_robot = game_data.blue_positions[robot]
    # print(moving_robot[2], moving_robot[3])
    if direction == game_data.NORTH_DIR:
        count = 1
        while count < game_data.f_height * game_data.sight_line and response[2] == game_data.NOTHING:
            response = check_robot2(user, moving_robot, moving_robot[2], moving_robot[3] + count, 'North', count, direction)
            count += 1
    if direction == game_data.NW_DIR:
        count = 1
        while count < game_data.f_height * game_data.sight_line and response[2] == game_data.NOTHING:
            response = check_robot2(user, moving_robot, moving_robot[2] - count, moving_robot[3] + count, 'Northwest',
                         count, direction)
            count += 1
    if direction == game_data.WEST_DIR:
        count = 1
        while count < game_data.f_height * game_data.sight_line and response[2] == game_data.NOTHING:
            response = check_robot2(user, moving_robot, moving_robot[2] - count, moving_robot[3], 'West', count, direction)
            count += 1
    if direction == game_data.SW_DIR:
        count = 1
        while count < game_data.f_height * game_data.sight_line and response[2] == game_data.WALL:
            response = check_robot2(user, moving_robot, moving_robot[2] - count, moving_robot[3] - count, 'Southwest',
                         count, direction)
            count += 1
    if direction == game_data.SOUTH_DIR:
        count = 1
        while count < game_data.f_height * game_data.sight_line and response[2] == game_data.NOTHING:
            response = check_robot2(user, moving_robot, moving_robot[2], moving_robot[3] - count, 'South', count, direction)
            count += 1
    if direction == game_data.SE_DIR:
        count = 1
        while count < game_data.f_height * game_data.sight_line and response[2] == game_data.NOTHING:
            response = check_robot2(user, moving_robot, moving_robot[2] - count, moving_robot[3] - count, 'Southeast',
                         count, direction)
            count += 1
    if direction == game_data.EAST_DIR:
        count = 1
        while count < game_data.f_height * game_data.sight_line and response[2] == game_data.NOTHING:
            response = check_robot2(user, moving_robot, moving_robot[2] + count, moving_robot[3], 'East', count, direction)
            count += 1
    if direction == game_data.NE_DIR:
        count = 1
        while count < game_data.f_height * game_data.sight_line and response[2] == game_data.NOTHING:
            response = check_robot2(user, moving_robot, moving_robot[2] + count, moving_robot[3] + count, 'Northeast',
                         count, direction)
            count += 1
    return response

def robot_shoot(field, robot, direction, user):
    if user == game_data.DAD:
        moving_robot = game_data.red_positions[robot]
        element = draw_shooting(field, user, robot, direction)
    else :
        moving_robot = game_data.blue_positions[robot]
        element = draw_shooting(field, user, robot, direction)

    if direction == game_data.NORTH_DIR:
        count = 1
        while count < game_data.f_height * game_data.shoot_line:
            check_robot3(field, user, moving_robot, moving_robot[2], moving_robot[3] + count, 'North', count)
            count += 1
    if direction == game_data.NW_DIR:
        count = 1
        while count < game_data.f_height * game_data.shoot_line:
            check_robot3(field, user, moving_robot, moving_robot[2] - count, moving_robot[3] + count, 'Northwest', count)
            count += 1
    if direction == game_data.WEST_DIR:
        count = 1
        while count < game_data.f_height * game_data.shoot_line:
            check_robot3(field, user, moving_robot, moving_robot[2] - count, moving_robot[3], 'West', count)
            count += 1
    if direction == game_data.SW_DIR:
        count = 1
        while count < game_data.f_height * game_data.shoot_line:
            check_robot3(field, user, moving_robot, moving_robot[2] - count, moving_robot[3] - count, 'Southwest', count)
            count += 1
    if direction == game_data.SOUTH_DIR:
        count = 1
        while count < game_data.f_height * game_data.shoot_line:
            check_robot3(field, user, moving_robot, moving_robot[2], moving_robot[3] - count, 'South', count)
            count += 1
    if direction == game_data.SE_DIR:
        count = 1
        while count < game_data.f_height * game_data.shoot_line:
            check_robot3(field, user, moving_robot, moving_robot[2] - count, moving_robot[3] - count, 'Southeast', count)
            count += 1
    if direction == game_data.EAST_DIR:
        count = 1
        while count < game_data.f_height * game_data.shoot_line:
            check_robot3(field, user, moving_robot, moving_robot[2] + count, moving_robot[3], 'East', count)
            count += 1
    if direction == game_data.NE_DIR:
        count = 1
        while count < game_data.f_height * game_data.shoot_line:
            check_robot3(field, user, moving_robot, moving_robot[2] + count, moving_robot[3] + count, 'Northeast', count)
            count += 1
    return element

def check_robot(user, moving_robot, x_coord, y_coord, field):
    for robot, element, x, y, exist in game_data.red_positions:
        if (x == x_coord and y == y_coord and moving_robot != robot and exist == True):
            kill_robot(field, game_data.DAD, robot)
            print('Dad robot #' + str(robot + 1) + ' has been run over')
    for robot, element, x, y, exist in game_data.blue_positions:
        if (x == x_coord and y == y_coord and moving_robot != robot and exist == True):
            kill_robot(field, game_data.JACKSON, robot)
            print('Jackson robot #' + str(robot + 1) + ' has been run over')

def check_robot2(user, moving_robot, x_coord, y_coord, dir, count, look_dir):
    temp = game_data.f_length
    dad = False
    jackson = False
    tempR = 0
    for robot, element, x, y, exist in game_data.red_positions :
        if(x_coord == 0 or x_coord == game_data.f_length or y_coord == 0 or y_coord == game_data.f_height):
            #print('Wall has been seen in ' + str(dir) + ' ' + str(count) + ' spaces away.')
            return (0, count, game_data.WALL, look_dir)
        if(x == x_coord and y == y_coord and exist == True) :
            if(count < temp):
                temp = count
                dad = True
                tempR = robot

    for robot, element, x, y, exist in game_data.blue_positions :
        if(x_coord == 0 or x_coord == game_data.f_length or y_coord == 0 or y_coord == game_data.f_height):
            #print('Wall has been seen in ' + str(dir) + ' ' + str(count) + ' spaces away.')
            return (0, count, game_data.WALL, look_dir)
        if(x == x_coord and  y == y_coord and exist == True) :
            if(count < temp):
                temp = count
                jackson = True
                tempR = robot

    if(temp != game_data.f_length):
        if(jackson == True):
            #print('Jackson robot ' + str(tempR) + ' has been seen in ' + str(dir) + ' ' + str(temp) + ' spaces away.')
            return (tempR, count, game_data.JACKSON, look_dir)
        if(dad == True):
            #print('Dad robot ' + str(tempR) + ' has been seen in ' + str(dir) + ' ' + str(count) + ' spaces away.')
            return (tempR, count, game_data.DAD, look_dir)

    return (0, 0, game_data.NOTHING, 0)


def check_robot3(field, user, moving_robot, x_coord, y_coord, dir, count):
    temp = game_data.f_length
    dad = False
    jackson = False
    tempR = 0
    for robot, element, x, y, exist in game_data.red_positions :
        if(x == x_coord and y == y_coord and exist == True) :
            if(count < temp):
                temp = count
                dad = True
                tempR = robot
    for robot, element, x, y, exist in game_data.blue_positions :
        if(x == x_coord and  y == y_coord and exist == True) :
            if(count < temp):
                temp = count
                jackson = True
                tempR = robot

    if(temp != game_data.f_length):
        if(jackson == True):
            print('Jackson robot ' + str(tempR) + ' has been shot at ' + str(dir) + ' ' + str(temp) + ' spaces away.')
            kill_robot(field, game_data.JACKSON, tempR)
            game_data.blue_positions[tempR] = (tempR, 0, x, y, False)
        if(dad == True):
            print('Dad robot ' + str(tempR) + ' has been shot at ' + str(dir) + ' ' + str(temp) + ' spaces away.')
            kill_robot(field, game_data.DAD, tempR)
            game_data.red_positions[tempR] = (tempR, 0, x, y, False)
    #else:
        #print('no robots were seen')

def kill_robot(field, user, robot):
    if user == game_data.DAD:
        dead_robot = game_data.red_positions[robot]
        if game_data.red_element[robot] != 0:
            field.DeleteFigure(game_data.red_element[robot])
            game_data.main_gui.Refresh()
            game_data.red_element[robot] = 0
    else:
        dead_robot = game_data.blue_positions[robot]
        if game_data.blue_element[robot] != 0:
            field.DeleteFigure(game_data.blue_element[robot])
            game_data.main_gui.Refresh()
            game_data.blue_element[robot] = 0

    x_coord = dead_robot[2]
    y_coord = dead_robot[3]
    old_element = dead_robot[1]

    field.DeleteFigure(old_element)
    element1 = field.DrawCircle((x_coord, y_coord), 3, line_color='black', fill_color='orange')
    element2 = field.DrawLine((x_coord - 10, y_coord + 10), (x_coord + 10, y_coord - 10), color='orange')
    element3 = field.DrawLine((x_coord + 10, y_coord + 10), (x_coord - 10, y_coord - 10), color='orange')
    element4 = field.DrawLine((x_coord - 10, y_coord), (x_coord + 10, y_coord), color='orange')
    element5 = field.DrawLine((x_coord, y_coord + 10), (x_coord, y_coord - 10), color='orange')
    game_data.main_gui.Refresh()
    time.sleep(2)
    field.DeleteFigure(element1)
    field.DeleteFigure(element2)
    field.DeleteFigure(element3)
    field.DeleteFigure(element4)
    field.DeleteFigure(element5)
#
#   Remove next command for that robot
#
    if user == game_data.DAD:
        print('Dad Robot #' + str(robot + 1) + ' has been removed')
        game_data.red_next[robot] = (0, 0, 0)
    else:
        game_data.blue_next[robot] = (0, 0, 0)
        print('Jackson Robot #' + str(robot + 1) + ' has been removed')

def draw_shooting(field, user, robot, direction):
    if user == game_data.DAD:
        x_coord = game_data.red_positions[robot][2]
        y_coord = game_data.red_positions[robot][3]
        color = 'red'
    else:
        x_coord = game_data.blue_positions[robot][2]
        y_coord = game_data.blue_positions[robot][3]
        color = 'blue'

    if direction == game_data.NORTH_DIR:
        element = field.DrawLine((x_coord, y_coord), (x_coord, y_coord + (game_data.f_height * game_data.shoot_line)), color=color)
    elif direction == game_data.NE_DIR:
        element = field.DrawLine((x_coord, y_coord), (x_coord + (game_data.f_height * game_data.shoot_line), y_coord + (game_data.f_height * game_data.shoot_line)), color=color)
    elif direction == game_data.EAST_DIR:
        element = field.DrawLine((x_coord, y_coord), (x_coord + (game_data.f_height * game_data.shoot_line), y_coord), color=color)
    elif direction == game_data.SE_DIR:
        element = field.DrawLine((x_coord, y_coord), (x_coord + (game_data.f_height * game_data.shoot_line), y_coord - (game_data.f_height * game_data.shoot_line)), color=color)
    elif direction == game_data.SOUTH_DIR:
        element = field.DrawLine((x_coord, y_coord), (x_coord, y_coord - (game_data.f_height * game_data.shoot_line)), color=color)
    elif direction == game_data.SW_DIR:
        element = field.DrawLine((x_coord, y_coord), (x_coord - (game_data.f_height * game_data.shoot_line), y_coord - (game_data.f_height * game_data.shoot_line)), color=color)
    elif direction == game_data.WEST_DIR:
        element = field.DrawLine((x_coord, y_coord), (x_coord - (game_data.f_height * game_data.shoot_line), y_coord), color=color)
    elif direction == game_data.NW_DIR:
        element = field.DrawLine((x_coord, y_coord), (x_coord + (game_data.f_height * game_data.shoot_line), y_coord - (game_data.f_height * game_data.shoot_line)), color=color)

    return element

def start_game(field_of_play, user):
    if user == 'Jackson':
        while True:
            jackson_robots.jackson_robot1(field_of_play)
            dad_robots.dad_robot1(field_of_play)
            game_data.main_gui.Refresh()

            jackson_robots.jackson_robot2(field_of_play)
            dad_robots.dad_robot2(field_of_play)
            game_data.main_gui.Refresh()

            jackson_robots.jackson_robot3(field_of_play)
            dad_robots.dad_robot3(field_of_play)
            game_data.main_gui.Refresh()

            jackson_robots.jackson_robot4(field_of_play)
            dad_robots.dad_robot4(field_of_play)
            game_data.main_gui.Refresh()

            jackson_robots.jackson_robot5(field_of_play)
            dad_robots.dad_robot5(field_of_play)
            game_data.main_gui.Refresh()
#
#   Check for a winner
#
            jackson_ct = 0
            for jackson_left in game_data.blue_next:
                if jackson_left[2] > 0:
                    jackson_ct += 1
            dad_ct = 0
            for dad_left in game_data.red_next:
                if dad_left[2] > 0:
                    dad_ct += 1

            if jackson_ct == 0:
                print('Dad wins!')
                break
            if dad_ct == 0:
                print('Jackson wins!')
                break
    else:
        while True:
            dad_robots.dad_robot1(field_of_play)
            jackson_robots.jackson_robot1(field_of_play)
            game_data.main_gui.Refresh()

            dad_robots.dad_robot2(field_of_play)
            jackson_robots.jackson_robot2(field_of_play)
            game_data.main_gui.Refresh()

            dad_robots.dad_robot3(field_of_play)
            jackson_robots.jackson_robot3(field_of_play)
            game_data.main_gui.Refresh()

            dad_robots.dad_robot4(field_of_play)
            jackson_robots.jackson_robot4(field_of_play)
            game_data.main_gui.Refresh()

            dad_robots.dad_robot5(field_of_play)
            jackson_robots.jackson_robot5(field_of_play)
            game_data.main_gui.Refresh()
#
#   Check for a winner
#
            jackson_ct = 0
            for jackson_left in game_data.blue_next:
                if jackson_left[2] > 0:
                    jackson_ct += 1
            dad_ct = 0
            for dad_left in game_data.red_next:
                if dad_left[2] > 0:
                    dad_ct += 1

            if jackson_ct == 0:
                print('Dad wins!')
                break
            if dad_ct == 0:
                print('Jackson wins!')
                break

