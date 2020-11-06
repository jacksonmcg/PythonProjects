import web_scape
import requests
import injury
import teamstats

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#############################################################################################
#                                                                                           #
#   Local test code                                                                         #
#                                                                                           #
#############################################################################################

if __name__ == '__main__':

    print('0: Exit')

    gameID = web_scape.get_game_identifier(1)
    count = 1

    while gameID != -1 :
        # print(gameID)

        gameURL = 'https://www.espn.com/nfl/game/_/gameId/'
        gameURL += gameID
        # print(gameURL)

        gamePage = requests.get(gameURL)
        web_obj = str(gamePage.content)

        teamPoint = web_obj.find('/nfl/team/_/name')

        longName = web_obj.find('long-name', teamPoint)
        greaterThan = web_obj.find('>', longName)
        lessThan = web_obj.find('<', longName)
        team1 = web_obj[greaterThan + 1:lessThan]

        longName = web_obj.find('long-name', lessThan)
        greaterThan = web_obj.find('>', longName)
        lessThan = web_obj.find('<', longName)
        team2 = web_obj[greaterThan + 1:lessThan]

        print(str(count) + ': ' + team1 + ' at ' + team2)

        count = count + 1
        gameID = web_scape.get_game_identifier(count)

    print('-----------------------------------------')
    name = input("Which game would you like to select?\n")
    print('-----------------------------------------')

    while 1:
        try:
            gameID = web_scape.get_game_identifier(int(name))
            break
        except ValueError:
            name = input("Please type a number\n")
            print('-----------------------------------------')
            continue

    while int(name) != 0:
        while gameID != -1:
            # print(gameID)

            gameURL = 'https://www.espn.com/nfl/game/_/gameId/'
            gameURL += gameID
            # print(gameURL)

            gamePage = requests.get(gameURL)
            web_obj = str(gamePage.content)

            teamPoint = web_obj.find('/nfl/team/_/name')

            longName = web_obj.find('long-name', teamPoint)
            greaterThan = web_obj.find('>', longName)
            lessThan = web_obj.find('<', longName)
            team1 = web_obj[greaterThan + 1:lessThan]

            longName = web_obj.find('long-name', lessThan)
            greaterThan = web_obj.find('>', longName)
            lessThan = web_obj.find('<', longName)
            team2 = web_obj[greaterThan + 1:lessThan]

            # Grabbing scoring summary
            start1 = web_obj.find('<div id="gamepackage-scoring-summary"')
            startScore = web_obj.find('<tr class="highlight">', start1)
            endScore = web_obj.find('<footer class="button-container">', start1)
            # print(web_obj[startScore:endScore])

            sendString = web_obj[startScore:endScore]
            scores = web_scape.scoring_list(sendString)

            # print(scores)
            if scores == -1:
                print("Game log not found... reporting injuries and team stats")
                injury_list = injury.get_injuries(gameURL)
                team_list = teamstats.get_team_stats(gameURL)

                # print(team_list)
                # print('\t' + team_list[0] + ' ' + team_list[1])
                count = 2
                while count < len(team_list) :
                    print(team_list[count] + '\n' + team_list[0] + ': ' + team_list[count+1] + '\t' + team_list[1] + ': ' + team_list[count+2])
                    count += 3

                print('-----------------------------------------')
                count = 0
                while count < len(injury_list):
                    print(str(injury_list[count][0]) + ': ' + str(injury_list[count][1]) + ' (' + str(injury_list[count][2]) + '), ' + str(injury_list[count][3]))
                    count += 1

                print('-----------------------------------------')
                name = input("Which game would you like to select?\n")
                if int(name) == 0:
                    break
                else:
                    gameID = web_scape.get_game_identifier(int(name))
                    print('-----------------------------------------')
            else:
                # Dummy data
                # scores = [(7, 1, '7:03', 'Houston'), (3, 3, '8:03', 'Tennessee'), (7, 4, '10:03', 'Tennessee')]

                count = 0
                score1 = 0
                score2 = 0
                qCounter = 0

                while count < len(scores):
                    if scores[count][0] == team1:
                        # score1 += scores[count][0]
                        if scores[count][1] == 'TD':
                            score1 += 7
                        elif scores[count][1] == 'FG':
                            score1 += 3
                    elif scores[count][0] == team2:
                        # score2 += scores[count][0]
                        if scores[count][1] == 'TD':
                            score2 += 7
                        elif scores[count][1] == 'FG':
                            score2 += 3
                    while int(scores[count][3]) > int(qCounter):
                        qCounter += 1
                        print('Quarter ' + str(qCounter))
                    print(str(scores[count][2]) + ': ' + team1 + ': ' + str(score1) + " | " + team2 + ': ' + str(score2))
                    count += 1

                print('-----------------------------------------')
                name = input("Which game would you like to select?\n")
                print('-----------------------------------------')
                while 1:
                    try:
                        gameID = web_scape.get_game_identifier(int(name))
                        break
                    except ValueError:
                        name = input("Please type a number\n")
                        print('-----------------------------------------')
                        continue
                if int(name) == 0:
                    break
                else:
                    gameID = web_scape.get_game_identifier(int(name))
        else:
            print('Game not found.')
            print('-----------------------------------------')
            name = input("Which game would you like to select?\n")
            print('-----------------------------------------')
            while 1:
                try:
                    gameID = web_scape.get_game_identifier(int(name))
                    break
                except ValueError:
                    name = input("Please type a number\n")
                    print('-----------------------------------------')
                    continue
            if int(name) == 0:
                break
            else:
                gameID = web_scape.get_game_identifier(int(name))
    # else:

    print('Exited program.')