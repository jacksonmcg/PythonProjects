import requests

def scoring_list(web_log):
    return_list = []
    score_ptr = 0

    first_qtr = web_log.find('first Quarter')
    second_qtr = web_log.find('second Quarter')
    third_qtr = web_log.find('third Quarter')
    fourth_qtr = web_log.find('fourth Quarter')
    running_ptr = 0

    while score_ptr != -1:
        team_ptr = web_log.find('100&w', running_ptr)
        team_webstr = web_log[team_ptr-25:team_ptr]
        score_team = get_team_name(team_webstr)

        score_ptr = web_log.find('score-type',team_ptr)
        if score_ptr != -1:
            gtrThan = web_log.find('>',score_ptr)
            lessThan = web_log.find('<',gtrThan)
            score = web_log[gtrThan+1:lessThan]

            time_ptr = web_log.find('time-stamp',lessThan)
            gtrThan = web_log.find('>',time_ptr)
            lessThan = web_log.find('<',gtrThan)
            time_stamp = web_log[gtrThan+1:lessThan]

            if gtrThan < second_qtr:
                quarter = 1
            elif gtrThan < third_qtr:
                quarter = 2
            elif gtrThan < fourth_qtr:
                quarter = 3
            else:
                quarter = 4

            score_data = (score_team, score, time_stamp, quarter)
            return_list.append(score_data)
            running_ptr = time_ptr

    if running_ptr == 0:
        return -1
    else:
        return return_list

def get_game_identifier(game_no):
    website = 'https://espn.com/nfl/'
    page = requests.get(website)
    web_obj = str(page.content)

    web_ptr = 0
    for game_ctr in range(0,game_no * 2):
        game_str = 'www.espn.com/nfl/game/'
        web_ptr = web_obj.find(game_str, web_ptr+1)
        if web_ptr == -1:
            return(web_ptr)

    game_url_data = web_obj[web_ptr:web_ptr+100]
    game_id_ptr = game_url_data.find(('/gameId/')) + len('/gameId/')
    game_id = game_url_data[game_id_ptr:game_id_ptr+9]

    return game_id

def get_team_name(team_str):
    start_ptr = team_str.find('nfl/500/') + len('nfl/500/')
    end_ptr = team_str.find('.png')

    team_name = team_str[start_ptr:end_ptr]

    if team_name == 'ari':
        return ('Arizona')
    elif team_name == 'atl':
        return ('Atlanta')
    elif team_name == 'bal':
        return ('Baltimore')
    elif team_name == 'buf':
        return('Buffalo')
    elif team_name == 'car':
        return('Carolina')
    elif team_name == 'cin':
        return('Cincinnati')
    elif team_name == 'cle':
        return ('Cleveland')
    elif team_name == 'chi':
        return('Chicago')
    elif team_name == 'dal':
        return ('Dallas')
    elif team_name == 'den':
        return('Denver')
    elif team_name == 'det':
        return ('Detroit')
    elif team_name == 'gb':
        return ('Green Bay')
    elif team_name == 'hou':
        return('Houston')
    elif team_name == 'jax':
        return('Jacksonville')
    elif team_name == 'ind':
        return('Indianapolis')
    elif team_name == 'kc':
        return ('Kansas City')
    elif team_name == 'lv':
        return ('Las Vegas Raiders')
    elif team_name == 'lac':
        return ('Los Angeles Chargers')
    elif team_name == 'lar':
        return ('Los Angeles Rams')
    elif team_name == 'mia':
        return ('Miami')
    elif team_name == 'min':
        return('Minnesota')
    elif team_name == 'ne':
        return ('New England')
    elif team_name == 'no':
        return ('New Orleans')
    elif team_name == 'nyj':
        return('New York Jets')
    elif team_name == 'nyg':
        return('New York Giants')
    elif team_name == 'phi':
        return ('Philadelphia')
    elif team_name == 'pit':
        return ('Pittsburgh')
    elif team_name == 'sea':
        return ('Seattle')
    elif team_name == 'sf':
        return('San Francisco')
    elif team_name == 'tb':
        return ('Tampa Bay')
    elif team_name == 'ten':
        return('Tennessee')
    elif team_name == 'was':
        return ('Washington')
    else:
        return('unknown team')

#############################################################################################
#                                                                                           #
#   Local test code                                                                         #
#                                                                                           #
#############################################################################################

if __name__ == '__main__':

    game_nbr = 5
    result = get_game_identifier(game_nbr)

    if result != -1:
        print('Game ID = ' + str(result))
    else:
        print('Game was not found on Website')
