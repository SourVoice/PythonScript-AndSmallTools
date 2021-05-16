from random import randint


class Die():
    """表示一个骰子"""

    def __init__(self, num_side=6):
        """默认为六面"""
        self.num_sides = num_side

    def roll(self):
        """反回随机值"""
        return randint(1, self.num_sides)

