import random


class BayesDice:
    # ------------------------------------------------------------ #
    def __init__(self):
        self.dice = [4, 6, 8, 12, 20]
        prior = 0.20
        self.data = {die: prior for die in self.dice}
        self.die = 0
    # ------------------------------------------------------------ #

    def choose_die(self):
        self.die = random.choice(self.dice)
    # ------------------------------------------------------------ #

    def roll_die(self):
        return random.randint(1, self.die)
    # ------------------------------------------------------------ #

    def update_priors(self, roll):
        def likelihood(die, roll):
            if roll > die:
                return 0
            return 1 / die
        denominator = [likelihood(die, roll) * self.data[die] for die in self.dice]
        for i in range(len(self.dice)):
            die = self.dice[i]
            numerator = denominator[i]
            self.data[die] = numerator / sum(denominator)
        print('die:', self.die, 'roll:', roll)
        for die, prior in self.data.items():
            print("{} : {:.2f}".format(die, prior))
        print('\n')
    # ------------------------------------------------------------ #
