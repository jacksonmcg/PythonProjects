#
#   Grid is 600 in width and 300 in height
#
#   Moving - moves the robot in a particular direction, but does not allow the robot to go off the grid
#       if a robot "steps on" another robot, that robot is considered killed.  This routine returns the user
#       (DAD or JACKSON) of the dead robot.
#   Looking - tells a robot to look in a direction for up to 100 units of length.  If it can see anything
#       in that direction, it returns the user (either DAD or JACKSON or WALL) and how far away it is
#   Shooting - tells a robot to shoot in a direction for up to 50 units of length.  If it hits anything
#       in that direction, the hit robot is considered killed.  This routine returns the user (either DAD
#       or JACKSON) and the coordinates of the dead robot.
#
#   Robot Functions
#       Execute the previously stored command - stored as (command, direction)
#           Move(1), Look(2), Shoot(3)
#       Based on results of the previous command, calculate and store the next command
#