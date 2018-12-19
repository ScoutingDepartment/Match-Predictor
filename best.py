from match import *
from data import data
from elims import *
from copy import deepcopy
import timeit


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


def best_1st(data, sims):
    return ave_wins(data, sims)


def best_2nd(data, rankings, best_1st, elims_order, sims):
    results = {}
    for sim in range(sims):
        if sim%(sims/100)==0:
            print(100*sim/sims,"%")
        picked = [*rankings]
        alliance_numbers = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}

        if sim==0:
            a2=deepcopy(alliance_numbers)
            for i in range(8):
                pick = list(set(picked) & set(rankings))[0]
                picked.pop(picked.index(pick))
                a2[i + 1].append(pick)

                pick = list(set(picked) & set(best_1st))[0]
                picked.pop(picked.index(pick))
                a2[i + 1].append(pick)

        alliance_numbers=deepcopy(a2)
        print(alliance_numbers)

        for i in range(8):
            alliance_numbers[i + 1].append(random.choice(rankings))

        alliances=deepcopy(alliance_numbers)
        for i in list(alliances.keys()):
            alliances[i] = make_alliance(data, alliances[i])

        elim_results = sim_elims(alliances, deepcopy(elims_order), 10)

        for i in list(elim_results.keys()):
            if alliance_numbers[i][-1] not in results:
                results[alliance_numbers[i][-1]] = [elim_results[i]]
            else:
                results[alliance_numbers[i][-1]].append(elim_results[i])
    for i in list(results.keys()):
        results[i] = sum(results[i]) / len(results[i])
    return results


# TODO optimze (generification)
if __name__ == "__main__":
    rank_d = ave_rp(data, 10000)
    ranks = sorted(rank_d, key=rank_d.get, reverse=True)

    b1d = best_1st(data, 10000)
    b1 = sorted(b1d, key=b1d.get, reverse=True)

    for k, v in sorted(b1d.items(), key=lambda item: item[1], reverse=True):
        print(k, v, sep="\t")
    print()

    for k, v in sorted(best_2nd(data, ranks, b1, elims_order, 1000).items(), key=lambda item: item[1], reverse=True):
        print(k, v, sep="\t")



