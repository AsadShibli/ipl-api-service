import pandas as pd, numpy as np
from collections import OrderedDict
ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)

def team():
    teams = list(set(list(matches.Team1)+ list(matches.Team2)))
    teams_dict = {
        'teams':teams
    }
    return teams_dict


def teamVTeamAPI(team1, team2):
    valid_teams = list(set(list(matches['Team1']) + list(matches['Team2'])))

    if team1 in valid_teams and team2 in valid_teams:
        temp_df = matches[((matches.Team1==team1) & (matches.Team2==team2) ) | ((matches.Team1==team2) & (matches.Team2==team1))]

        total_matches = temp_df.shape[0]
        matches_won_team1 = temp_df.WinningTeam.value_counts()[team1]
        matches_won_team2 = temp_df.WinningTeam.value_counts()[team2]
        draws = total_matches - (matches_won_team1+ matches_won_team2)

        response = OrderedDict()
        response['total_matches'] = str(total_matches)
        response[team1] = str(matches_won_team1)
        response[team2] = str(matches_won_team2)
        response['draws'] = str(draws)

        return response
    else:
        return {'message':'invalid team name'}


