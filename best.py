from match import *
from data import data


def ave_score(data, sims):
    team_data = {}
    for i in range(sims):
        teams = random.choices(list(data.keys()), k=6)

        match = make_match(data, teams[:3], teams[-3:])
        scores = match.sim()

        for team in [team.team for team in match.red_alliance.teams]:
            if team in list(team_data.keys()):
                team_data[team]['c'] += 1
                team_data[team]['s'] += scores[0]
            else:
                team_data[team] = {'c': 1, 's': scores[0]}

        for team in [team.team for team in match.blue_alliance.teams]:
            if team in list(team_data.keys()):
                team_data[team]['c'] += 1
                team_data[team]['s'] += scores[1]
            else:
                team_data[team] = {'c': 1, 's': scores[1]}

    team_scores = {}
    for k in team_data:
        team_scores[k] = team_data[k]['s'] / team_data[k]['c']

    return team_scores


def ave_wins(data, sims):
    team_data = {}
    for i in range(sims):
        teams = random.choices(list(data.keys()), k=6)

        match = make_match(data, teams[:3], teams[-3:])
        scores = match.sim()

        for team in [team.team for team in match.red_alliance.teams]:
            if team in list(team_data.keys()):
                team_data[team]['c'] += 1
                team_data[team]['s'] += int(scores[0] > scores[1])
            else:
                team_data[team] = {'c': 1, 's': int(scores[0] > scores[1])}

        for team in [team.team for team in match.blue_alliance.teams]:
            if team in list(team_data.keys()):
                team_data[team]['c'] += 1
                team_data[team]['s'] += int(scores[1] > scores[0])
            else:
                team_data[team] = {'c': 1, 's': int(scores[1] > scores[0])}

    team_scores = {}
    for k in team_data:
        team_scores[k] = team_data[k]['s'] / team_data[k]['c']

    return team_scores


# TODO make ave_rp
# TODO optimze (generification)
if __name__ == "__main__":
    for k, v in sorted(ave_wins(data, 100000).items(), key=lambda item: item[1], reverse=True):
        print(k, v, sep="\t")
