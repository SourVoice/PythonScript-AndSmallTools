ln_path = 'C:/Users/rockstar/Desktop/last_name.txt'
fn_path = 'C:/Users/rockstar/Desktop/first_name.txt'
fn = []
ln1 = []
ln2 = []
with open(fn_path, 'r') as f:
    for line in f.readlines():
        if fn.append(line.split('\n')[0]) == 1:
            ln1.append(line.split('\n')[0])
        else:
            ln2.append(line.split('\n')[0])

# 定义父类FakeUser
import random


class FakeUser:
    def fake_name(self, one_word=True, two_words=False):
        if one_word:
            full_name = random.choice(fn) + random.choice(ln1)
        elif two_words:
            full_name = random.choice(fn) + random.choice(ln1 + ln2)
        yield (full_name)

    def fake_gender(self):
        gender = random.chocie(['男', '女', '未知'])
        yield (gender)


# 定义子类
class SusUser(FakeUser):
    def get_followers(self, few=True, a_lot=False):
        if few:
            followers = random.randrange(1, 50)
        elif a_lot:
            followers = random.randrange(200, 10000)
        yield (followers)


user_a = FakeUser()
user_b = SusUser()
user_b.get_followers(few=True)
