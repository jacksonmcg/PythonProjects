f_length = 150
f_height = 80
sight_line = .60
shoot_line = .40
#
#   Below robot positions have the following elements
#       Robot number
#       Circle drawn element
#       X coordinate
#       Y coordinate
#
blue_positions = [(0, 0, 0, 0, True), (0, 0, 0, 0, True), (0, 0, 0, 0, True), (0, 0, 0, 0, True), (0, 0, 0, 0, True)]
red_positions = [(0, 0, 0, 0, True), (0, 0, 0, 0, True), (0, 0, 0, 0, True), (0, 0, 0, 0, True), (0, 0, 0, 0, True)]
#
#   Below robot positions have the following elements
#       Command to execute (MOVE, LOOK, SHOOT)
#       Direction (NORTH_DIR, NE_DIR, EAST_DIR, etc.)
#       Turn count - number of turns since the battle started
#
blue_next = [(0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 1)]
red_next = [(0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 1)]

blue_element = [0, 0, 0, 0, 0]        # drawn line element if last command for JACKSON was a SHOOT
red_element = [0, 0, 0, 0, 0]         # drawn line element if last command for DAD was a SHOOT
main_gui = ''
time_delay = 0.04

NORTH_DIR = 0
NE_DIR = 1
EAST_DIR = 2
SE_DIR = 3
SOUTH_DIR = 4
SW_DIR = 5
WEST_DIR = 6
NW_DIR = 7

JACKSON = 'blue'
DAD = 'red'
WALL = 'wall'
NOTHING = 'nothing'

MOVE = 1
LOOK = 2
SHOOT = 3

ROBOT1 = 0
ROBOT2 = 1
ROBOT3 = 2
ROBOT4 = 3
ROBOT5 = 4
