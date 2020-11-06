import requests

def get_team_data(team_name):
    website = 'https://espn.com/nfl/standings'
    page = requests.get(website)
    web_obj = str(page.content)

    web_ptr = 0
    for team_ct in range(0,16):
        web_ptr = web_obj.find('title=', web_ptr + 1)
        web_ptr = web_obj.find('title=', web_ptr + 1)

        team_str = web_obj[web_ptr:web_ptr + 50]
        team_start = team_str.find('"', 1)

        team_end = team_str.find('"', team_start + 1)
        team_found = team_str[team_start + 1:team_end]

        if team_name == team_found:
            print(team_ct)

            stat_ptr = web_obj.find('STRK', web_ptr)

            if team_ct > 11:
                team_ct += 3
            elif team_ct > 7:
                team_ct += 2
            elif team_ct > 3:
                team_ct += 1

            for stat_ct in range(0,team_ct + 1):
                stat_ptr = web_obj.find('Table__TR Table__TR', stat_ptr + 1)

            wins_ptr = web_obj.find('stat-cell', stat_ptr)
            grt_than = web_obj.find('>', wins_ptr)
            less_than = web_obj.find('<', grt_than)
            wins = int(web_obj[grt_than + 1:less_than])

            loss_ptr = web_obj.find('stat-cell', wins_ptr + 1)
            grt_than = web_obj.find('>', loss_ptr)
            less_than = web_obj.find('<', grt_than)
            losses = int(web_obj[grt_than + 1:less_than])

            tie_ptr = web_obj.find('stat-cell', loss_ptr + 1)
            grt_than = web_obj.find('>', tie_ptr)
            less_than = web_obj.find('<', grt_than)
            ties = int(web_obj[grt_than + 1:less_than])
#
#   Throw away the next 5 data point.  Keep Points For and Poinst Against
#
            junk_ptr = tie_ptr + 5
            for bad_data in range(0,5):
                junk_ptr = web_obj.find('stat-cell', junk_ptr + 1)

            pfor_ptr = web_obj.find('stat-cell', junk_ptr + 1)
            grt_than = web_obj.find('>', pfor_ptr)
            less_than = web_obj.find('<', grt_than)
            points_for = int(web_obj[grt_than + 1:less_than])

            pagst_ptr = web_obj.find('stat-cell', pfor_ptr + 1)
            grt_than = web_obj.find('>', pagst_ptr)
            less_than = web_obj.find('<', grt_than)
            points_agst = int(web_obj[grt_than + 1:less_than])

            team_stats = (team_name, wins, losses, ties, points_for, points_agst)
            return team_stats

    web_ptr = web_obj.find('National Football Conference', web_ptr + 1)
    for team_ct in range(0,16):
        web_ptr = web_obj.find('title=', web_ptr + 1)
        web_ptr = web_obj.find('title=', web_ptr + 1)

        team_str = web_obj[web_ptr:web_ptr + 50]
        team_start = team_str.find('"', 1)

        team_end = team_str.find('"', team_start + 1)
        team_found = team_str[team_start + 1:team_end]

        if team_name == team_found:
            stat_ptr = web_obj.find('STRK', web_ptr)

            if team_ct > 11:
                team_ct += 3
            elif team_ct > 7:
                team_ct += 2
            elif team_ct > 3:
                team_ct += 1

            for stat_ct in range(0,team_ct + 1):
                stat_ptr = web_obj.find('Table__TR Table__TR', stat_ptr + 1)

            wins_ptr = web_obj.find('stat-cell', stat_ptr)
            grt_than = web_obj.find('>', wins_ptr)
            less_than = web_obj.find('<', grt_than)
            wins = int(web_obj[grt_than + 1:less_than])

            loss_ptr = web_obj.find('stat-cell', wins_ptr + 1)
            grt_than = web_obj.find('>', loss_ptr)
            less_than = web_obj.find('<', grt_than)
            losses = int(web_obj[grt_than + 1:less_than])

            tie_ptr = web_obj.find('stat-cell', loss_ptr + 1)
            grt_than = web_obj.find('>', tie_ptr)
            less_than = web_obj.find('<', grt_than)
            ties = int(web_obj[grt_than + 1:less_than])
#
#   Throw away the next 5 data point.  Keep Points For and Poinst Against
#
            junk_ptr = tie_ptr + 5
            for bad_data in range(0, 5):
                junk_ptr = web_obj.find('stat-cell', junk_ptr + 1)

            pfor_ptr = web_obj.find('stat-cell', junk_ptr + 1)
            grt_than = web_obj.find('>', pfor_ptr)
            less_than = web_obj.find('<', grt_than)
            points_for = int(web_obj[grt_than + 1:less_than])

            pagst_ptr = web_obj.find('stat-cell', pfor_ptr + 1)
            grt_than = web_obj.find('>', pagst_ptr)
            less_than = web_obj.find('<', grt_than)
            points_agst = int(web_obj[grt_than + 1:less_than])

            team_stats = (team_name, wins, losses, ties, points_for, points_agst)
            return team_stats

    return 'NOT FOUND'

