ln_path = 'C:/Users/rockstar/Desktop/last_name.txt'
fn_path = 'C:/Users/rockstar/Desktop/first_name.txt'
fn = []
ln1 = []
ln2 = []
with open(fn_path, 'r', encoding='UTF-8') as f:
    for line in f.readlines():
        if fn.append(line.split('\n')[0]) == 1:
            ln1.append(line.split('\n')[0])
        else:
            ln2.append(line.split('\n')[0])

import random


class FakeUser():
    def fake_name(self, amount=1, one_word=False, two_words=False):
        n = 0
        while n <= amount:
            if one_word:
                full_name = random.choice(fn) + random.choice(ln1)
            elif two_words:
                full_name = random.choice(fn) + random.choice(ln2)
            else:
                full_name = random.choice(fn) + random.choice(ln1 + ln2)
                yield full_name
                n += 1

    def fake_gender(self, amount=1):
        n = 0
        while n <= amount:
            gender = random.choice(['boy', 'girl', 'Unknown'])
            yield gender
            n += 1


class SunUser(FakeUser):
    def get_followers(self, amount=1, few=True, a_lot=False):
        n = 0
        while n <= amount:
            if few:
                followers = random.randrange(1, 50)
            elif a_lot:
                followers = random.randrange(200, 10000)
            yield followers
            n += 1


user_a = FakeUser()
user_b = SunUser()
for name in user_a.fake_names(30):
    print(name)
for gender in user_a.fake_gender(30):
    print(gender)
