from match import *
from data import data, alliances, elims_order


def index_dict_symmetry(d, a, b):
    return d[a][b] if a < b else 1 - d[b][a]


def elims_win(alliances, sims):
    elims_data = {}

    for i in range(1, 8):
        elims_data[i] = {}

    for i in range(1, 9):
        for j in range(1, 9):
            if i < j:
                elims_data[i][j] = sim_win_chance(data, alliances[i], alliances[j], sims)

    return elims_data


def elims_round(elims_data, a, b):
    ab = {}
    for i in a:
        s = 0
        for j in b:
            s += index_dict_symmetry(elims_data, i, j) * b[j]
        ab[i] = a[i] * s
    for i in b:
        s = 0
        for j in a:
            s += index_dict_symmetry(elims_data, i, j) * a[j]
        ab[i] = b[i] * s
    return ab


def calc_elims(elims_data, l):
    for i, e in enumerate(l):
        if type(e[0]) == dict:
            l[i] = elims_round(elims_data, *e)
        else:
            l[i] = calc_elims(elims_data, e)
    return elims_round(elims_data, *l)


# TODO make this use Match
if __name__ == "__main__":
    elims_data = elims_win(alliances, 1000)

    for k in elims_data:
        print(k, elims_data[k])
    print()

    d = calc_elims(elims_data, elims_order)
    d = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]
    for k, v in d:
        print(k, v, sep="\t")
