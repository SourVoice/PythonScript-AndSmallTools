import random


def get_steps():
    direction = random.choice([-1, 1])
    distance = random.choice([0, 1, 2, 3, 4, 5])
    step_value = direction * distance
    return step_value
