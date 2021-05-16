#
'''
class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']
'''

'''
coke_for_me = ()
for element in coke_for_me.formula:
    print(element)
'''
'''
coke_for_China = CocaCola()
coke_for_China.local_logo = 'kekoukele'  # 创建实例属性

print(coke_for_China.local_logo)
'''

'''
class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']

    def drink(coke):
        print('Energy!')


coke = CocaCola()
coke.drink()
'''

'''
class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']
    def drink(self, how_much):

        if how_much == 'a sip':
            print('Cool~')
        elif how_much =='whole bottle':
            print('Headache!')


ice_coke = CocaCola()
ice_coke.drink('a sip')
'''

'''
class CocaCola():
    formula = ['caffeine', 'sugar', 'water', 'soda']

    def __init__(self):
        self.local_logo = ' 可口可乐 '

    def drink(self):
        print('Energy!')


coke = CocaCola()
print(coke.local_logo)
'''

'''
class CocaCola():
    formula = ['caffeine', 'sugar', 'water', 'soda']

    def __init__(self):
        for element in self.formula:
            print('Coke has {}!'.format(element))

    def drink(self):
        print('Energy!')


coke = CocaCola()
coke.drink()

'''

'''
class CocaCola():
    formula = ['caffeine', 'sugar', 'water', 'soda']

    def __init__(self, logo_name):
        self.local_logo = logo_name

    def drink(self):
        print('Energy!')


coke = CocaCola(' 可口可乐 ')
print(coke.local_logo)
'''


class CocaCola():
    calories = 140
    sodium = 45
    total_carb = 39
    caffeine = 34
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Natural Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine'
    ]

    def __init__(self, logo_name):
        self, local_logo = logo_name

    def drink(self):
        print('You got {} cal energy!'.format(self.calories))


class TestA:
    attr = 1


obj_a = TestA()

TestA.attr = 42
print(obj_a.attr)


class TestA():
    attr = 1


obj_a = TestA()
obj_b = TestA()
print(obj_b.attr)


class TestA:
    attr = 1

    def __int__(self):
        self.attr = 42


obj_a = TestA()
print(obj_b.attr)

obj1 = 1
obj2 = 'String!'
obj3 = []
obj4 = {}
print(type(obj1), type(obj2), type(obj3), type(obj4))


class Cook(object):
    def __init__(self, one, two):
        self.In_one = one
        self.In_two = two

    def fry(self):
        self.In_one = self.In_one + '搅拌'
        self.In_two = self.In_two + '切片'
        return self.In_one + self.In_two + '炒'


breakfast = Cook('鸡蛋', '番茄')
print('%s' % (breakfast.fry()))
