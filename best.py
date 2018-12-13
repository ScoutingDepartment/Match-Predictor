from match import *
from data import data


def best_score(data, sims):
    team_data = {}
    for i in range(sims):
        teams = random.choices(list(data.keys()), k=6)
        r = teams[:3]
        b = teams[-3:]
        scores = sim_match_based_on_teams(data, r, b)

        for team in r:
            if team in list(team_data.keys()):
                team_data[team]['c'] += 1
                team_data[team]['s'] += scores[0]
            else:
                team_data[team] = {'c': 1, 's': scores[0]}

        for team in b:
            if team in list(team_data.keys()):
                team_data[team]['c'] += 1
                team_data[team]['s'] += scores[1]
            else:
                team_data[team] = {'c': 1, 's': scores[1]}

    team_scores = {}

    for k in team_data:
        team_scores[k] = team_data[k]['s'] / team_data[k]['c']
    return team_scores


def best_wins(data, sims):
    team_data = {}
    for i in range(sims):
        teams = random.choices(list(data.keys()), k=6)
        r = teams[:3]
        b = teams[-3:]
        scores = sim_match_based_on_teams(data, r, b)

        for team in r:
            if team in list(team_data.keys()):
                team_data[team]['c'] += 1
                team_data[team]['s'] += int(scores[0] > scores[1])
            else:
                team_data[team] = {'c': 1, 's': int(scores[0] > scores[1])}

        for team in b:
            if team in list(team_data.keys()):
                team_data[team]['c'] += 1
                team_data[team]['s'] += int(scores[1] > scores[0])
            else:
                team_data[team] = {'c': 1, 's': int(scores[1] > scores[0])}

    team_scores = {}

    for k in team_data:
        team_scores[k] = team_data[k]['s'] / team_data[k]['c']
    return team_scores


def f(s, n):
    return str(s) + " " * (n - len(str(s)))


# TODO make this use Match
if __name__ == "__main__":
    for  k, v in sorted(best_wins(data, 100000).items(), key=lambda item: item[1], reverse=True):
        print(f(k.team, 4), v, sep="\t")
