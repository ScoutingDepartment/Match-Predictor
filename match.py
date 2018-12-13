from team import *
import random


def sim_ownership(a, b, offset_a=0, offset_b=0):
    A = [random.random() for _ in range(round(a))]
    B = [random.random() for _ in range(round(b))]
    l = sorted(A + B)

    a_count = offset_a
    b_count = offset_b
    p = 0

    am = 0
    bm = 0
    tm = 0

    for i in l:
        s = i - p
        if a_count > b_count:
            am += s
        elif b_count > a_count:
            bm += s
        else:
            tm += s

        if i in A:
            a_count += 1
        if i in B:
            b_count += 1
        p = i

    s = 1 - p

    if a_count > b_count:
        am += s
    elif b_count > a_count:
        bm += s
    else:
        tm += s
    return (am, tm, bm)


def sim_match(r_auto_line=0, r_auto_scale=0, r_auto_switch=0, r_scale=0, r_near_switch=0, r_far_switch=0,
              r_exchange=0, r_climb=0, b_auto_line=0, b_auto_scale=0, b_auto_switch=0, b_scale=0,
              b_near_switch=0, b_far_switch=0, b_exchange=0, b_climb=0):
    red_points = 0
    blue_points = 0

    # auto line
    red_points += 5 * min((r_auto_line, 3))
    blue_points += 5 * min((b_auto_line, 3))

    # auto scale
    r_win, tie, b_win = sim_ownership(r_auto_scale, b_auto_scale)
    red_points += 2 * 15 * r_win
    blue_points += 2 * 15 * b_win

    # auto switch
    red_points += 2 * 15
    blue_points += 2 * 15

    # scale
    r_win, tie, b_win = sim_ownership(r_scale, b_scale, offset_a=r_auto_scale, offset_b=b_auto_scale)
    red_points += 135 * r_win
    blue_points += 135 * b_win

    # red switch
    r_win, tie, b_win = sim_ownership(r_near_switch, b_far_switch, offset_a=r_auto_switch)
    red_points += 135 * r_win
    blue_points += 0 * b_win

    # blue switch
    r_win, tie, b_win = sim_ownership(r_far_switch, b_near_switch, offset_b=b_auto_switch)
    red_points += 0 * r_win
    blue_points += 135 * b_win

    exch = {0: 0 * 5,  # 0
            1: 10 + 1 * 5,  # 15
            2: 10 + 2 * 5,  # 20
            3: 30 + 3 * 5,  # 45
            4: 30 + 10 + 4 * 5,  # 60
            5: 30 + 10 + 5 * 5,  # 65
            6: 30 + 20 + 6 * 5,  # 80
            7: 30 + 20 + 7 * 5,  # 85
            8: 30 + 20 + 8 * 5,  # 90
            9: 30 + 20 + 9 * 5  # 95
            }

    # exchange
    red_points += exch[min((round(r_exchange) + 3, 9))]
    blue_points += exch[min((round(b_exchange) + 3, 9))]

    # climb
    red_points += 30 * min((r_climb, 3))
    blue_points += 30 * min((b_climb, 3))

    return [red_points, blue_points]


def sim_match_based_on_teams(data, r, b):
    if type(r) != Alliance:
        for i, e in enumerate(r):
            r[i] = data[e]
        for i, e in enumerate(b):
            b[i] = data[e]
        return sim_match(*Alliance(*r).sample_all(), *Alliance(*b).sample_all())
    else:
        return sim_match(*r.sample_all(), *b.sample_all())


def sim_win_chance(data, r, b, sims):
    if type(r) != Alliance:
        r = make_alliance(data, r)
        b = make_alliance(data, b)

    wins = 0
    for i in range(sims):
        scores = sim_match_based_on_teams(data, r, b)
        if scores[0] > scores[1]:
            wins += 1
    return wins / sims


class Match:
    def __init__(self, red_alliance: Alliance, blue_alliance: Alliance):
        self.red_alliance = red_alliance
        self.blue_alliance = blue_alliance

        self.sims = 0
        self.red_wins = 0
        self.blue_wins = 0

    def sim(self):
        return sim_match(*self.red_alliance.sample_all(), *self.blue_alliance.sample_all())

    def win_chance(self, sims, update=True, ret=True):
        red_wins = 0
        blue_wins = 0
        for i in range(sims):
            scores = self.sim()
            if scores[0] > scores[1]:
                red_wins += 1
            elif scores[1] > scores[0]:
                blue_wins += 1

        if update:
            self.red_wins += red_wins
            self.blue_wins += blue_wins
            self.sims += sims

        if ret:
            return (red_wins + (sims - red_wins - blue_wins) / 2) / sims

    def red_win_chance(self):
        return self.red_wins / self.sims

    def blue_win_chance(self):
        return self.blue_wins / self.sims


def make_match(data, red, blue):
    if type(red) != Alliance:
        return Match(make_alliance(data, red), make_alliance(data, blue))
    return Match(red, blue)


if __name__ == "__main__":
    from data import data

    match = make_match(data, [865, 494, 4917], [5406, 2481, 2451])
    match.win_chance(10000)
    print(match.red_win_chance())
