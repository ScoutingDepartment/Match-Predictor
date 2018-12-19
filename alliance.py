from team import *

class Alliance:
    def __init__(self, *teams: Team):
        self.teams = teams
        self.auto_line = []
        self.auto_scale = [0, 0]
        self.auto_switch = [0, 0]
        self.scale = [0, 0]
        self.near_switch = [0, 0]
        self.far_switch = [0, 0]
        self.exchange = [0, 0]
        self.climbing = []

        self.auto_scales=[]


        autos = []
        for team in teams:
            autos.append([team.team, team.auto_scale[0]])
        autos = sorted(autos, key=lambda item: item[1])

        for team in teams:
            self.auto_line.append(team.auto_line)

            if team.team != autos[0]:
                self.auto_scale[0] += team.auto_scale[0]
                self.auto_scale[1] = math.sqrt(self.auto_scale[1] ** 2 + team.auto_scale[1] ** 2)
            else:
                self.auto_switch[0] = team.auto_switch[0]
                self.auto_switch[1] = self.auto_switch[1]

            self.scale[0] += team.scale[0] * team.auto_line
            self.scale[1] = math.sqrt(self.scale[1] ** 2 + team.scale[1] ** 2)

            self.near_switch[0] += team.near_switch[0] * team.auto_line
            self.near_switch[1] = math.sqrt(self.near_switch[1] ** 2 + team.near_switch[1] ** 2)

            self.far_switch[0] += team.far_switch[0]
            self.far_switch[1] = math.sqrt(self.far_switch[1] ** 2 + team.far_switch[1] ** 2)

            self.exchange[0] += team.exchange[0]
            self.exchange[1] = math.sqrt(self.exchange[1] ** 2 + team.exchange[1] ** 2)

            self.climbing.append(team.climbing)

        self.auto_quest = np.prod(self.auto_line)
        self.face_the_boss = \
            self.climbing[0] * self.climbing[1] * (1 - self.climbing[2]) + \
            self.climbing[0] * (1 - self.climbing[1]) * self.climbing[2] + \
            (1 - self.climbing[0]) * self.climbing[1] * self.climbing[2] + \
            self.climbing[0] * self.climbing[1] * self.climbing[2]

        if self.face_the_boss > 1:
            print(self.climbing)

    def sample_auto_quest(self, only_positive=True, only_whole=False):
        r = int(random.random() < self.auto_quest)

        if only_whole:
            r = round(r)

        return r

    def sample_auto_scale(self, only_positive=True, only_whole=False):
        r = -1
        if only_positive:
            while r < 0:
                r = random.normalvariate(self.auto_scale[0], self.auto_scale[1])
        else:
            r = random.normalvariate(self.auto_scale[0], self.auto_scale[1])
        if only_whole:
            r = round(r)

        return r

    def sample_auto_switch(self, only_positive=True, only_whole=False):
        r = -1
        if only_positive:
            while r < 0:
                r = random.normalvariate(self.auto_switch[0], self.auto_switch[1])
        else:
            r = random.normalvariate(self.auto_switch[0], self.auto_switch[1])
        if only_whole:
            r = round(r)

        return r

    def sample_scale(self, only_positive=True, only_whole=False):
        r = -1
        if only_positive:
            while r < 0:
                r = random.normalvariate(self.scale[0], self.scale[1])
        else:
            r = random.normalvariate(self.scale[0], self.scale[1])
        if only_whole:
            r = round(r)

        return r

    def sample_near_switch(self, only_positive=True, only_whole=False):
        r = -1
        if only_positive:
            while r < 0:
                r = random.normalvariate(self.near_switch[0], self.near_switch[1])
        else:
            r = random.normalvariate(self.near_switch[0], self.near_switch[1])
        if only_whole:
            r = round(r)

        return r

    def sample_far_switch(self, only_positive=True, only_whole=False):
        r = -1
        if only_positive:
            while r < 0:
                r = random.normalvariate(self.far_switch[0], self.far_switch[1])
        else:
            r = random.normalvariate(self.far_switch[0], self.far_switch[1])
        if only_whole:
            r = round(r)

        return r

    def sample_exchange(self, only_positive=True, only_whole=False):
        r = -1
        if only_positive:
            while r < 0:
                r = random.normalvariate(self.exchange[0], self.exchange[1])
        else:
            r = random.normalvariate(self.exchange[0], self.exchange[1])
        if only_whole:
            r = round(r)

        return r

    def sample_face_the_boss(self, only_positive=True, only_whole=False):
        r = int(random.random() < self.face_the_boss)

        if only_whole:
            r = round(r)

        return r

    def sample_all(self, only_positive=True, only_whole=False):
        return [
            self.sample_auto_quest(only_positive, only_whole),
            self.sample_auto_scale(only_positive, only_whole),
            self.sample_auto_switch(only_positive, only_whole),
            self.sample_scale(only_positive, only_whole),
            self.sample_near_switch(only_positive, only_whole),
            self.sample_far_switch(only_positive, only_whole),
            self.sample_exchange(only_positive, only_whole),
            self.sample_face_the_boss(only_positive, only_whole)
        ]


def make_alliance(data, teams):
    if type(teams[0]) != Team:
        for i, e in enumerate(teams):
            teams[i] = data[e]
    return Alliance(*teams)