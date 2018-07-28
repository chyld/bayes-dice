import random


class BayesDice:
    # ------------------------------------------------------------ #
    def __init__(self):
        self.dice = [4, 6, 8]
        self.data = {die: 0.33 for die in self.dice}
    # ------------------------------------------------------------ #

    def choose_die(self):
        self.die = random.choice(self.dice)
    # ------------------------------------------------------------ #

    def roll_die(self):
        return random.randint(1, self.die)
    # ------------------------------------------------------------ #

    def update_priors(self, roll):
        denominator = list(map(lambda die: (0 if roll > die else (1 / die)) * self.data[die], self.dice))
        self.data = {self.dice[i]: numerator / sum(denominator) for i, numerator in enumerate(denominator)}
        self.debug(roll, denominator)
    # ------------------------------------------------------------ #

    def debug(self, roll, denominator):
        print('-' * 50)
        print('die:', self.die, 'roll:', roll)
        print('denominator:', denominator)
        print('data:', self.data)
        print('sum of priors:', sum(self.data.values()))
        print('sum of denominator:', sum(denominator))
    # ------------------------------------------------------------ #
