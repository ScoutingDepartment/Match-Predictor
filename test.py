import random

a = 0
b = 2

ao = 1
bo = 0

granularity = 60
sims = 10000


def sim(a, b):
    A = [random.random() for _ in range(a)]
    B = [random.random() for _ in range(b)]
    l = sorted(A + B)

    ac = 0
    bc = 0
    p = 0

    am = 0
    bm = 0
    tm = 0

    for i in l:
        s = i - p
        if ac > bc:
            am += s
        elif bc > ac:
            bm += s
        else:
            tm += s
        if i in A:
            ac += 1
        if i in B:
            bc += 1
        p = i
    s = 1 - p
    if ac > bc:
        am += s
    elif bc > ac:
        bm += s
    else:
        tm += s
    return (am, tm, bm)


def sim_point(a, b, ao, bo, point=1 / 2):
    A = [random.random() for _ in range(a)]
    B = [random.random() for _ in range(b)]
    l = sorted(A + B + [point])

    ac = ao
    bc = bo

    for i in l:
        if i in A:
            ac += 1
        if i in B:
            bc += 1
        if i == point:
            break
    if ac > bc:
        return 'a'
    if bc > ac:
        return 'b'
    return 't'


AA = []

for i in range(0, granularity):
    A = 0
    T = 0
    B = 0

    for j in range(sims):
        n = sim_point(a, b, ao, bo, i / granularity)
        A += int(n == 'a')
        # T+=int(n=='t')
        # B+=int(n=='b')

    AA.append(A / sims)

for i in AA:
    print(i)
