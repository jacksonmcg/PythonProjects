import math

import spread_functions

#############################################################################################
#                                                                                           #
#   Local test code                                                                         #
#                                                                                           #
#############################################################################################

if __name__ == '__main__':

    team_name = input('Home team: ')
    team_stats = spread_functions.get_team_data(team_name)

    team_name2 = input('Away team: ')
    team_stats2 = spread_functions.get_team_data(team_name2)

    if team_stats != 'NOT FOUND':
        wins = team_stats[1]
        losses = team_stats[2]
        ties = team_stats[3]
        points_for = team_stats[4]
        points_against = team_stats[5]
        #print(team_name, wins, losses, ties, points_for, points_against)
    else:
        print('Team name was not found')

    if team_stats2 != 'NOT FOUND':
        wins = team_stats2[1]
        losses = team_stats2[2]
        ties = team_stats2[3]
        points_for = team_stats2[4]
        points_against = team_stats2[5]
        #print(team_name, wins, losses, ties, points_for, points_against)
    else:
        print('Team name was not found')

    totalGames = (team_stats[1] + team_stats2[1] + team_stats[2] + team_stats2[2])

    pd = ((team_stats[4] - team_stats[5]) - (team_stats2[4] - team_stats2[5]))/totalGames
    wvl = ((team_stats[1] - team_stats[2]) - (team_stats2[1] - team_stats2[2]))*(totalGames/8)
    spread = (pd + wvl + 2)/2

    if spread >= 8:
        spreadDiff = 0
        spread = spread - spreadDiff

    if((spread * 2)%2 == 0):
        spread = math.trunc(spread)
    else:
        spread = math.trunc(spread) + 0.5


    if(spread > 0):
        print(team_name + ' ' + str(spread) + ' over ' + team_name2)
    else:
        spread = 0 - spread
        print(team_name2 + ' ' + str(spread) + ' over ' + team_name)

    #print(spread)

