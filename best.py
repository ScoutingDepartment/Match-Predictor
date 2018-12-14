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
                team_data[team]['count'] += 1
                team_data[team]['score'] += scores[0]
            else:
                team_data[team] = {'count': 1, 'score': scores[0]}

        for team in [team.team for team in match.blue_alliance.teams]:
            if team in list(team_data.keys()):
                team_data[team]['count'] += 1
                team_data[team]['score'] += scores[1]
            else:
                team_data[team] = {'count': 1, 'score': scores[1]}

    team_scores = {}
    for k in team_data:
        team_scores[k] = team_data[k]['score'] / team_data[k]['count']

    return team_scores


def ave_wins(data, sims):
    team_data = {}
    for i in range(sims):
        teams = random.choices(list(data.keys()), k=6)

        match = make_match(data, teams[:3], teams[-3:])
        scores = match.sim()

        for team in [team.team for team in match.red_alliance.teams]:
            if team in list(team_data.keys()):
                team_data[team]['count'] += 1
                team_data[team]['wins'] += int(scores[0] > scores[1])
            else:
                team_data[team] = {'count': 1, 'wins': int(scores[0] > scores[1])}

        for team in [team.team for team in match.blue_alliance.teams]:
            if team in list(team_data.keys()):
                team_data[team]['count'] += 1
                team_data[team]['wins'] += int(scores[1] > scores[0])
            else:
                team_data[team] = {'count': 1, 'wins': int(scores[1] > scores[0])}

    team_scores = {}
    for k in team_data:
        team_scores[k] = team_data[k]['wins'] / team_data[k]['count']

    return team_scores


def ave_rp(data, sims):
    team_data = {}
    for i in range(sims):
        teams = random.choices(list(data.keys()), k=6)

        match = make_match(data, teams[:3], teams[-3:])
        scores = match.sim()

        for team in [team.team for team in match.red_alliance.teams]:
            if team in list(team_data.keys()):
                team_data[team]['count'] += 1
                team_data[team]['rp'] += int(scores[0] > scores[1]) * 2
                team_data[team]['rp'] += match.red_alliance.sample_auto_quest(only_whole=True)
                team_data[team]['rp'] += match.red_alliance.sample_face_the_boss(only_whole=True)
            else:
                team_data[team] = {'count': 1,
                                   'rp': int(scores[0] > scores[1]) * 2 +
                                         match.red_alliance.sample_auto_quest(only_whole=True) +
                                         match.red_alliance.sample_face_the_boss(only_whole=True)
                                   }

        for team in [team.team for team in match.blue_alliance.teams]:
            if team in list(team_data.keys()):
                team_data[team]['count'] += 1
                team_data[team]['rp'] += int(scores[0] > scores[1]) * 2
                team_data[team]['rp'] += match.blue_alliance.sample_auto_quest(only_whole=True)
                team_data[team]['rp'] += match.blue_alliance.sample_face_the_boss(only_whole=True)
            else:
                team_data[team] = {'count': 1,
                                   'rp': int(scores[0] > scores[1]) * 2 +
                                         match.blue_alliance.sample_auto_quest(only_whole=True) +
                                         match.blue_alliance.sample_face_the_boss(only_whole=True)
                                   }

    team_scores = {}
    for k in team_data:
        team_scores[k] = team_data[k]['rp'] / team_data[k]['count']

    return team_scores


# TODO optimze (generification)
if __name__ == "__main__":
    for k, v in sorted(ave_rp(data, 100000).items(), key=lambda item: item[1], reverse=True):
        print(k, v, sep="\t")
