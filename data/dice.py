import random
class Dice():
    @classmethod
    def d4_rolled(cls):
        d4_range = range(1, 5)
        d4_rolled = random.choice(d4_range)
        return d4_rolled

    @classmethod
    def d6_rolled(cls):
        d6_range = range(1, 7)
        d6_rolled = random.choice(d6_range)
        return d6_rolled

    @classmethod
    def d8_rolled(cls):
        d8_range = range(1, 9)
        d8_rolled = random.choice(d8_range)
        return d8_rolled

    @classmethod
    def d10_rolled(cls):
        d10_range = range(1, 11)
        d10_rolled = random.choice(d10_range)
        return d10_rolled

    @classmethod
    def d12_rolled(cls):
        d12_range = range(1, 13)
        d12_rolled = random.choice(d12_range)
        return d12_rolled

    @classmethod
    def d20_rolled(cls):
        d20_range = range(1, 21)
        d20_rolled = random.choice(d20_range)
        return d20_rolled
