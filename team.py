import random
import math
import numpy as np


class Team:
    def __init__(self, team, auto_line, auto_scale, auto_switch, scale, near_switch, far_switch, exchange, climbing):
        self.team = team
        self.auto_line = auto_line
        self.auto_scale = auto_scale
        self.auto_switch = auto_switch
        self.scale = scale
        self.near_switch = near_switch
        self.far_switch = far_switch
        self.exchange = exchange
        self.climbing = climbing

    def sample_auto_line(self, only_positive=True, only_whole=False):
        r = int(random.random() < self.auto_line)

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

    def sample_climbing(self, only_positive=True, only_whole=False):
        r = int(random.random() < self.climbing)

        if only_whole:
            r = round(r)

        return r

    def sample_all(self, only_positive=True, only_whole=False):
        return [
            self.sample_auto_line(only_positive, only_whole),
            self.sample_auto_scale(only_positive, only_whole),
            self.sample_auto_switch(only_positive, only_whole),
            self.sample_scale(only_positive, only_whole),
            self.sample_near_switch(only_positive, only_whole),
            self.sample_far_switch(only_positive, only_whole),
            self.sample_exchange(only_positive, only_whole),
            self.sample_climbing(only_positive, only_whole)
        ]


def make_team(raw_data, team_number):
    return Team(team_number, *raw_data[team_number])
