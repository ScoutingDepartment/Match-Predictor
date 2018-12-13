from data import data, schedule
from match import *
from team import *


def sim_quals(data, schedule, sims, n=0):
    schedule = schedule[n:]

    results = {}
    for match in schedule:
        match = make_match(data, match[:3], match[-3:])

        match.win_chance(sims)

        for team in [team.team for team in match.red_alliance.teams]:
            if team not in list(results.keys()):
                results[team] = {'win': [], 'auto': [], 'climb': []}

            results[team]['win'].append(match.red_win_chance())
            results[team]['auto'].append(match.red_alliance.auto_quest)
            results[team]['climb'].append(match.red_alliance.face_the_boss)

        for team in [team.team for team in match.blue_alliance.teams]:
            if team not in list(results.keys()):
                results[team] = {'win': [], 'auto': [], 'climb': []}
            results[team]['win'].append(match.blue_win_chance())
            results[team]['auto'].append(match.blue_alliance.auto_quest)
            results[team]['climb'].append(match.blue_alliance.face_the_boss)

    return results


def calc_rp(rpd, current_rp={}):
    for team in rpd:
        rp = 0
        count = 0
        for i in range(len(rpd[team]['win'])):
            rp += 2 * rpd[team]['win'][i]
            rp += rpd[team]['auto'][i]
            rp += rpd[team]['climb'][i]
            count += 1
        if team in current_rp:
            rpd[team] = (rp + current_rp[team]['sum']) / (count + current_rp[team]['count'])
        else:
            rpd[team] = rp / count
    return rpd


def predict_rank(team, data, schedule, sims, n=0, current_rp={}):  # TODO optimise
    schedule = schedule[n:]
    t = team

    sum_rank = 0

    for i in range(sims):
        rp = calc_rp(sim_quals(data, schedule, 1), current_rp)
        rp = sorted(rp.items(), key=lambda item: item[1], reverse=True)

        rank = list(dict(rp).keys()).index(t) + 1

        sum_rank += rank
    return sum_rank / sims


if __name__ == '__main__':
    print(predict_rank(5406, data, schedule, 100))
