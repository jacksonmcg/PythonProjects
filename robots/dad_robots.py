import game_functions as gf
import game_data as gd
import random
##########################################################
#                                                        #
#   Dad Robot #1                                         #
#                                                        #
##########################################################
def dad_robot1(field_of_play):
    previous_cmd = gd.red_next[gd.ROBOT1][0]
    response = gf.execute_cmd(gd.ROBOT1, gd.red_next[gd.ROBOT1], gd.DAD, field_of_play)
    turn_ct = gd.red_next[gd.ROBOT1][2]
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
#           gd.red_next[gd.ROBOT1] = (gd.MOVE, direction, turn_ct + 1)
#
        gd.red_next[gd.ROBOT1] = (gd.MOVE, gd.NORTH_DIR, turn_ct + 1)

##########################################################
#                                                        #
#   Dad Robot #2                                         #
#                                                        #
##########################################################
def dad_robot2(field_of_play):
    previous_cmd = gd.red_next[gd.ROBOT2][0]
    response = gf.execute_cmd(gd.ROBOT2, gd.red_next[gd.ROBOT2], gd.DAD, field_of_play)
    turn_ct = gd.red_next[gd.ROBOT2][2]
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
#           gd.red_next[gd.ROBOT2] = (gd.MOVE, direction, turn_ct + 1)
#
        gd.red_next[gd.ROBOT2] = (gd.MOVE, gd.EAST_DIR, turn_ct + 1)

##########################################################
#                                                        #
#   Dad Robot #3                                         #
#                                                        #
##########################################################
def dad_robot3(field_of_play):
    previous_cmd = gd.red_next[gd.ROBOT3][0]
    response = gf.execute_cmd(gd.ROBOT3, gd.red_next[gd.ROBOT3], gd.DAD, field_of_play)
    turn_ct = gd.red_next[gd.ROBOT3][2]
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
#           gd.red_next[gd.ROBOT3] = (gd.MOVE, direction, turn_ct + 1)
#
        gd.red_next[gd.ROBOT3] = (gd.MOVE, gd.SOUTH_DIR, turn_ct + 1)

##########################################################
#                                                        #
#   Dad Robot #4                                         #
#                                                        #
##########################################################
def dad_robot4(field_of_play):
    previous_cmd = gd.red_next[gd.ROBOT4][0]
    response = gf.execute_cmd(gd.ROBOT4, gd.red_next[gd.ROBOT4], gd.DAD, field_of_play)
    turn_ct = gd.red_next[gd.ROBOT4][2]
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
#           gd.red_next[gd.ROBOT4] = (gd.MOVE, direction, turn_ct + 1)
#
        gd.red_next[gd.ROBOT4] = (gd.MOVE, gd.WEST_DIR, turn_ct + 1)

##########################################################
#                                                        #
#   Dad Robot #5                                         #
#                                                        #
##########################################################
def dad_robot5(field_of_play):
    previous_cmd = gd.red_next[gd.ROBOT5][0]
    response = gf.execute_cmd(gd.ROBOT5, gd.red_next[gd.ROBOT5], gd.DAD, field_of_play)
    turn_ct = gd.red_next[gd.ROBOT5][2]
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
#           gd.red_next[gd.ROBOT5] = (gd.MOVE, direction, turn_ct + 1)
#
        gd.red_next[gd.ROBOT5] = (gd.SHOOT, random.randrange(0, 8), turn_ct + 1)
