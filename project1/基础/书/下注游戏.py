# 小游戏
import random


# 摇骰子
def roll_dice(numbers=3, points=None):
    print('<<<<< ROLL THE DICE ! >>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1, 7)
        points.append(point)
        numbers = numbers - 1
    return points


# 三次骰子结果
def roll_result(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <= 10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'


# 开始函数
def start_game(money_you_have):
    print('Now you have' + str(money_you_have) + ' to bet.')
    print('<<<<< GAME STARTS! >>>>>')
    choices = ['Big', 'Small']
    your_choice = input('Big or Small :')
    if your_choice in choices and money_you_have > 0:
        money_you_bet = int(input('How much you wanna bet ? -'))
        points = roll_dice()  # 投掷骰子
        total = sum(points)
        youWin = your_choice == roll_result(total)
        if youWin:
            print('The points are', points, 'You win !')
            money_you_have = money_you_have + money_you_bet
            print('You win' + str(money_you_bet) + '\n' + 'Now you have' + str(money_you_have))
        else:
            print('The points are', points, 'You lose !')
            money_you_have = money_you_have - money_you_bet

            print('You lose' + str(money_you_bet) + '\n' + 'Now you have' + str(money_you_have))
    elif money_you_have <= 0:
        return print('<<<<< Game Over >>>>>')
    start_game(money_you_have)


money_you_have = 1000
start_game(money_you_have)
