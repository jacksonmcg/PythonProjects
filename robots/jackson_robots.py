import game_functions as gf
import game_data as gd
import random

##########################################################
#                                                        #
#   Jackson Robot #1                                     #
#                                                        #
##########################################################
def jackson_robot1(field_of_play):
    previous_cmd = gd.blue_next[gd.ROBOT1][0]
    response = gf.execute_cmd(gd.ROBOT1, gd.blue_next[gd.ROBOT1], gd.JACKSON, field_of_play)
    turn_ct = gd.blue_next[gd.ROBOT1][2]
    if turn_ct > 0:
#
#   if turn_ct = 0, then Robot is dead.  If so, above if statement will skip the code below.
#
#   if previous_cmd = gd.LOOK, then 'response' has the following information:
#       if the wall is seen --> (0, distance, WALL, direction)
#       if robot is seen -----> (robot #, distance, robot owner (JACKSON or DAD), direction)
#       if nothing is seen ---> (0, 0, NOTHING, 0)
#
#   Below Function must set the next command using the robot # (gd.ROBOT1, gd.ROBOT2, etc)
#       Allowable commands are --> gd.MOVE, gd.LOOK, gd.SHOOT
#           command must be followed by a DIRECTION (gd.NORTH_DIR, gd.NW_DIR, etc)
#           then command is following by turn_ct + 1
#       Example:
#           gd.blue_next[gd.ROBOT1] = (gd.MOVE, direction, turn_ct + 1)

        variable = random.randrange(0,8)
#
        if turn_ct % 3 == 0:
            gd.blue_next[gd.ROBOT1] = (gd.MOVE, variable, turn_ct + 1)
        elif turn_ct % 3 == 1:
            gd.blue_next[gd.ROBOT1] = (gd.LOOK, variable, turn_ct + 1)
        else:
            if previous_cmd == gd.LOOK:
                if response[2] == gd.DAD and response[1] < gd.f_height / 4:
                    gd.blue_next[gd.ROBOT1] = (gd.SHOOT, response[3], turn_ct + 1)
            else:
                gd.blue_next[gd.ROBOT1] = (gd.MOVE, variable, turn_ct + 1)


##########################################################
#                                                        #
#   Jackson Robot #2                                     #
#                                                        #
##########################################################
def jackson_robot2(field_of_play):
    previous_cmd = gd.blue_next[gd.ROBOT2][0]
    response = gf.execute_cmd(gd.ROBOT2, gd.blue_next[gd.ROBOT2], gd.JACKSON, field_of_play)
    turn_ct = gd.blue_next[gd.ROBOT2][2]
    if turn_ct > 0:
#
#   if turn_ct = 0, then Robot is dead.  If so, above if statement will skip the code below.
#
#   if previous_cmd = gd.LOOK, then 'response' has the following information:
#       if the wall is seen --> (0, distance, WALL, direction)
#       if robot is seen -----> (robot #, distance, robot owner (JACKSON or DAD), direction)
#       if nothing is seen ---> (0, 0, NOTHING, 0)
#
#   Below Function must set the next command using the robot # (gd.ROBOT1, gd.ROBOT2, etc)
#       Allowable commands are --> gd.MOVE, gd.LOOK, gd.SHOOT
#           command must be followed by a DIRECTION (gd.NORTH_DIR, gd.NW_DIR, etc)
#           then command is following by turn_ct + 1
#       Example:
#           gd.blue_next[gd.ROBOT2] = (gd.MOVE, direction, turn_ct + 1)

        variable = random.randrange(0, 8)

        if turn_ct % 2 == 0:
            gd.blue_next[gd.ROBOT2] = (gd.MOVE, variable, turn_ct + 1)
        else:
            gd.blue_next[gd.ROBOT2] = (gd.SHOOT, variable, turn_ct + 1)

##########################################################
#                                                        #
#   Jackson Robot #3                                     #
#                                                        #
##########################################################
def jackson_robot3(field_of_play):
    previous_cmd = gd.blue_next[gd.ROBOT3][0]
    response = gf.execute_cmd(gd.ROBOT3, gd.blue_next[gd.ROBOT3], gd.JACKSON, field_of_play)
    turn_ct = gd.blue_next[gd.ROBOT3][2]
    if turn_ct > 0:
#
#   if turn_ct = 0, then Robot is dead.  If so, above if statement will skip the code below.
#
#   if previous_cmd = gd.LOOK, then 'response' has the following information:
#       if the wall is seen --> (0, distance, WALL, direction)
#       if robot is seen -----> (robot #, distance, robot owner (JACKSON or DAD), direction)
#       if nothing is seen ---> (0, 0, NOTHING, 0)
#
#   Below Function must set the next command using the robot # (gd.ROBOT1, gd.ROBOT2, etc)
#       Allowable commands are --> gd.MOVE, gd.LOOK, gd.SHOOT
#           command must be followed by a DIRECTION (gd.NORTH_DIR, gd.NW_DIR, etc)
#           then command is following by turn_ct + 1
#       Example:
#           gd.blue_next[gd.ROBOT3] = (gd.MOVE, direction, turn_ct + 1)
#

        variable = random.randrange(0, 8)

        if previous_cmd == gd.LOOK:
            if response[2] == gd.DAD and response[1] < gd.f_height / 4:
                gd.blue_next[gd.ROBOT3] = (gd.SHOOT, response[3], turn_ct + 1)
            else:
                gd.blue_next[gd.ROBOT3] = (gd.MOVE, variable, turn_ct + 1)
        else:
            gd.blue_next[gd.ROBOT3] = (gd.LOOK, variable, turn_ct + 1)

##########################################################
#                                                        #
#   Jackson Robot #4                                     #
#                                                        #
##########################################################
def jackson_robot4(field_of_play):
    previous_cmd = gd.blue_next[gd.ROBOT4][0]
    response = gf.execute_cmd(gd.ROBOT4, gd.blue_next[gd.ROBOT4], gd.JACKSON, field_of_play)
    turn_ct = gd.blue_next[gd.ROBOT4][2]
    if turn_ct > 0:
#
#   if turn_ct = 0, then Robot is dead.  If so, above if statement will skip the code below.
#
#   if previous_cmd = gd.LOOK, then 'response' has the following information:
#       if the wall is seen --> (0, distance, WALL, direction)
#       if robot is seen -----> (robot #, distance, robot owner (JACKSON or DAD), direction)
#       if nothing is seen ---> (0, 0, NOTHING, 0)
#
#   Below Function must set the next command using the robot # (gd.ROBOT1, gd.ROBOT2, etc)
#       Allowable commands are --> gd.MOVE, gd.LOOK, gd.SHOOT
#           command must be followed by a DIRECTION (gd.NORTH_DIR, gd.NW_DIR, etc)
#           then command is following by turn_ct + 1
#       Example:
#           gd.blue_next[gd.ROBOT4] = (gd.MOVE, direction, turn_ct + 1)
#

        variable = random.randrange(0, 8)

        if turn_ct % 6 == 0:
            gd.blue_next[gd.ROBOT4] = (gd.MOVE, variable, turn_ct + 1)
        else:
            if previous_cmd == gd.LOOK:
                if response[2] == gd.DAD and response[1] < gd.f_height / 4:
                    gd.blue_next[gd.ROBOT4] = (gd.SHOOT, response[3], turn_ct + 1)
            else :
                gd.blue_next[gd.ROBOT4] = (gd.LOOK, variable, turn_ct + 1)


##########################################################
#                                                        #
#   Jackson Robot #5                                     #
#                                                        #
##########################################################
def jackson_robot5(field_of_play):
    previous_cmd = gd.blue_next[gd.ROBOT5][0]
    response = gf.execute_cmd(gd.ROBOT5, gd.blue_next[gd.ROBOT5], gd.JACKSON, field_of_play)
    turn_ct = gd.blue_next[gd.ROBOT5][2]
    if turn_ct > 0:
#
#   if turn_ct = 0, then Robot is dead.  If so, above if statement will skip the code below.
#
#   if previous_cmd = gd.LOOK, then 'response' has the following information:
#       if the wall is seen --> (0, distance, WALL)
#       if robot is seen -----> (robot #, distance, robot owner (JACKSON or DAD))
#       if nothing is seen ---> (0, 0, NOTHING)
#
#   Below Function must set the next command using the robot # (gd.ROBOT1, gd.ROBOT2, etc)
#       Allowable commands are --> gd.MOVE, gd.LOOK, gd.SHOOT
#           command must be followed by a DIRECTION (gd.NORTH_DIR, gd.NW_DIR, etc)
#           then command is following by turn_ct + 1
#       Example:
#           gd.blue_next[gd.ROBOT5] = (gd.MOVE, direction, turn_ct + 1)
#
        variable = random.randrange(0, 8)

        gd.blue_next[gd.ROBOT5] = (gd.MOVE, variable, turn_ct + 1)
