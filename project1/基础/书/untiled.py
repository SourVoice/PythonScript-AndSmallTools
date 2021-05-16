num = 1
string = '1'
num2 = int(string)
print(num + num2)

words = 'words' * 3
print(words)

word = 'a long long word'
num = 12
string = 'bang!'
total = string * (len(word) - num)
print(total)

word = 'friend'
find_the_evil_in_your_friends = word[0] + word[2:4] + word[-3:-1]
print(find_the_evil_in_your_friends)

url = 'http://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg'
file_name = url[-10:]

print(file_name)

phone_number = '13856-666-0006'
hiding_number = phone_number.replace(phone_number[:9], '*' * 9)
print(hiding_number)

search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'

print(search + ' is at ' + str(num_a.find(search)) + ' to ' + str(num_a.find(search) + len(search)) + ' of num_a')
print(search + ' is at ' + str(num_b.find(search)) + ' to ' + str(num_b.find(search) + len(search)) + ' of num_b')

print('{} a word she can get what she {} for.'.format('With', 'came'))
print('{preposition} a word she can get what she {verb} for.'.format(preposition='With', verb='came'))
print('{0} a word she can get what she {1} for.'.format('With', 'came'))


# city = input("write down the name of the city:")
# url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)


def fahrenheit_converter(c):
    fahrenheit = c * 9 / 5 + 32
    return str(fahrenheit) + 'F'


C2F = fahrenheit_converter(35)
print(C2F)

lyric_length = len('I Cry Out For Magic!')
print(lyric_length)


def fahrenheit_converter(c):
    fahrenheit = c * 9 / 5 + 32
    return print(str(fahrenheit) + 'F')


C2F = fahrenheit_converter(35)
print(C2F)


# weight = input("the weight you want to transform:")
# print(str(int(weight) / 1000) + 'kg')


# def pythagorean_theorem(a, b):
#    return int(a * a + b * b)


# hypotenuse = pythagorean_theorem(input('a='), input('b='))
# print('the right angle is:', hypotenuse)


def trapezoid_area(base_up, base_down, height):
    return print(1 / 2 * (base_up + base_down) * height)


trapezoid_area(1, 2, 3)
base_up = 1
base_down = 2
height = 3

trapezoid_area(height, base_down, base_up)

# trapezoid_area(1,2)参数缺一不可

print('   *', '  * *', ' * * *', '   |  ')
print('   *', '  * *', ' * * *', '   |  ', sep='\n')


# img.save(img_new, img_format, quality=100)图片加水印默认水印质量100

# file = open('C://Users/rockstar/Desktop/text1.txt', 'w')
# file.write('Hello World')


def text_create(name, msg):
    desktop_path = 'C://Users/rockstar/Desktop/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')


# text_create(input("the name of your text on the desktop: "), 'hello world')


def text_filter(word, censored_word='lame', changed_word='Awesome'):
    return word.replace(censored_word, changed_word)


# text_filter('Python is lame')


def censored_text_create(name, msg):
    clean_msg = text_filter(msg)
    text_create(name, clean_msg)


album = ['Black Star', 'David Bowie', 25, True]
album.append('new song')
print(album[0], album[-1])
print('Black Star' in album)

the_Eddie = 'Eddie'
name = 'Eddie'
print(the_Eddie == name)
print(the_Eddie is name)

a_thing = None
print(a_thing)


def account_login():
    password = input('Password:')
    password_correct = password = '12345'
    if password_correct:
        print('Login success!')
    else:
        print('Wrong password or invalid input!')
        account_login()


# account_login()


password_list = ['*#*#', '12345']


def account_login():
    password = input('Password:')
    password_correct = password == password == password_list[-1]
    password_correct_reset = password == password_list[0]  # 当输入密码等于密码列表第一个元素(即重置密码的'口令'),dit
    # 第一个元素指'*#*#'
    if password_correct:
        print('Login success!')
    elif password_correct_reset:
        new_password = input('Enter a new password:')
        password_list.append(new_password)
        print('Your password has changed successfully!')
        account_login()
    else:
        print('Wrong password or invalid input!')
        account_login()


# account_login()


# 循环(loop)
# for every_letter in 'Hello world':
#    print(every_letter)


for num in range(1, 11):
    print(str(num) + ' + 1 =', num + 1)
'''
上段代码等同于:
num = 1
print(str(num) + ' + 1 =', num+1)
num = 2
print(str(num) + ' + 1 =', num + 1)
`
`
`
num=10
print(str(num) + ' + 1 =', num + 1)
'''

songslist = ['Holy Diver', 'Thunderstruck', 'Rebel Rebel']
for song in songslist:
    if song == 'Holy Diver':
        print(song, ' - Dio')
    elif song == 'Thunderstruck':
        print(song, ' - AC/DC')
    elif song == 'Rebel Rebel':
        print(song, ' - David Bowie')

'''
for i in range(1, 10):
    for j in range(1, 10):
        print('{} X {} = {}'.format(i, j, i * j))
'''

'''
while 1 < 3:
    print('1 is smaller than 3')
'''

'''
count = 0
while True:
    print('Repeat this line !')
    count = count + 1
    if count == 5:
        break
'''
password_list = ['*#*#', '12345']


def account_login():
    tries = 3
    while tries > 0:
        password = input('Password:')
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]
        if password_correct:
            print('Login success')
        elif password_reset:
            new_password = input('Enter a new password :')
            password_list.append(new_password)
            print('Password has changed successfully!')
            account_login()
        else:
            print('Wrong password or invalid input!')
            tries = tries - 1
            print(tries, 'times left')
    else:
        print('Your account has been suspended')


# account_login()


def text_create():
    for i in range(1, 10):
        desktop_path = 'C://Users/rockstar/Desktop/'
        name = str(i)
        file_path = desktop_path + name + '.txt'
        file = open(file_path, 'w')
        file.write(name)
        i = i + 1
        file.close()


# text_create()
# 已完成,别调用


a_list = [1, 2, 3]
print(sum(a_list))
import random

point1 = random.randrange(1, 7)
point2 = random.randrange(1, 7)
point3 = random.randrange(1, 7)

print(point1, point2, point3)
print()

'''
====================小游戏===================================
<<<<< GAME STARTS >>>>>
Big or Small:Big
<<<<< ROLE THE DICE >>>>>
THe points are [2,6,3] You Lose
'''

'''
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

            print('You lose' + str(money_you_bet) + '\n' +'Now you have' + str(money_you_have))
    elif money_you_have <= 0:
        return print('<<<<< Game Over >>>>>')
    start_game(money_you_have)

money_you_have = 1000
start_game(money_you_have)
'''
print("\n")

# 列表(list)============================================
Weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(Weekday[0])
all_in_list = [
    1,
    1.0,
    'a word',  # 浮点数
    print(1),  # 函数
    True,  # 布尔值
    [1, 2],  # 列表中的列表
    (1, 2),  # 元组
    {'key': 'vale'}  # 字典
]

# 列表的增删
fruit = ['pineapple', 'pear']
fruit.insert(1, 'grape')
print(fruit)
# 第二种方式:
fruit[0:0] = ['Orange']
print(fruit)
# 列表的删除
fruit = ['pineapple', 'pear', 'grape']
# fruit.move('grape')  #该句不正确
# 替换
fruit[0] = 'Grapefruit'
periodic_table = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
print(periodic_table[0])
print(periodic_table[-2])
print(periodic_table[0:3])
print(periodic_table[-10:-7])
print(periodic_table[:9])
# 会报错(反过来找位置)
# print(periodic_table['H'])
print("\n")  # 下一个

# 字典======================================================
a = {'key': 123, 'key': 123}
print(a)

NASDAQ_code = {
    'BIDU': 'Baidu',
    'SINA': 'Sina',
    'YOKU': 'Youku'
}
# key_text = {[]: 'a Test'}  # key不能是变量
# print(key_test)


# 字典添加元素
NASDAQ_code.update({'FB': 'Facebook', 'TSLA': 'Tesla'})
print(NASDAQ_code)

# 删除元素(字典)
del NASDAQ_code['FB']
print(NASDAQ_code['TSLA'])
print(NASDAQ_code)
print("\n")

# 元组========================================================
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(letters[0])
print()

# 集合=========================================================
a_set = {1, 2, 3, 4}
a_set.add(5)
a_set.discard(5)

'''
# 列表排序
num_list = [6, 2, 7, 4, 1, 3, 5]
print(sorted(num_list))  # 正序排列
print(sorted(num_list, reverse=True))  # 逆序排列
'''

# 整理列表
for a, b in zip(num, str):  # 同时整理两个列表
    print(b, 'is', a)

a = []
for i in range(1, 11):
    a.append(i)

# 列表解析式
b = [i for i in range(1, 11)]

import time

a = []
t0 = time.clock()
for i in range(1, 20000):
    a.append(i)
print(time.clock() - t0, 'seconds process time')

t0 = time.clock()
b = [i for i in range(1, 20000)]
print(time.clock() - t0, 'seconds process time')

# 列表推导式
a = [i ** 2 for i in range(1, 10)]
c = [j for j in range(1, 10)]
k = [n for n in range(1, 10) if n % 2 == 0]
z = [letter.lower() for letter in 'ABCDEFGHIJKLMN']
# 字典推导式
d = {i: i + 1 for i in range(4)}
# g = {i: j for i.j in zip(range(1, 6), 'abcde')}
# g = {i: j.upper() for i, j in zip(range(1, 6), 'abcde')}


# 获取列表元素的索引
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for num, letter in enumerate(letters):
    print(letter, 'is', num + 1)

lyric = 'The night begin to shine, the night begin to shine'
words = lyric.split()
'''
path = 'C://Users/rockstar/Desktop/w.txt'
with open(path, 'r', encoding='UTF-8') as text:
    words = [raw_word.strip(string.punctuation.lower() for raw_word in text.read().split)]
    words_index = set(words)
    counts_dict = {index: words.count(index_dict[x], reverse=True)}
    print(words)
    for word in words:
        print('{}-{} times'.format(word, words.count(word)))
'''
