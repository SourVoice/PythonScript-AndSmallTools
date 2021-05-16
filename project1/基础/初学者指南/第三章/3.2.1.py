import random
die1 = random.randint(1, 6)  # 产生包括两端的参数
die2 = random.randrange(6) + 1  # randrange是随机产生0~(参数-1)

total = die1 + die2
print("You rolled a", die1, "and a", die2, "for a total of", total)
