import sys

a_list = [1, 2, 3, 4]
it = iter(a_list)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素

print(next(it))  # 迭代器能够库遍历对象位置,
# 所以下一次的迭代对象为上一迭代迭代的下一个元素


# 迭代器对象可以使用常规的for语句进行遍历
print('--------------------------------------------------')
b_list = [1, 2, 3, 4]
it = iter(b_list)
for xi in it:
    print(xi, end=' ')

print()
print('---------------------------------------------------')
# 使用next()函数创建迭代器
"""
c_list = [1, 2, 3, 4]
it = iter(c_list)

while True:
    try:
        print(next(it))
    except Exception as e:
        print('---------------------------')
"""


# 写了这段代码后出现unreachable?,still don't know how to solve it
# so I ## the above code


# 创建一个返回数字的迭代器,初始值为1,主部递增1:
# 将一个类最为了一个迭代器
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):  # __next__返回下一个迭代器对象
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
mysister = iter(myclass)  # iter返回一个特殊的迭代器

print(next(mysister))
print(next(mysister))
print(next(mysister))
print(next(mysister))
print(next(mysister))
print('----------------------------------------------------------')


class Mynumbers2(object):
    def __iter__(self):  # 创建迭代器
        self.a = 1
        return self

    def __next__(self):  # 含有__next__()函数的对象都是迭代器
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = Mynumbers2()
myiter = iter(myclass)

for x in myiter:
    print(x)

print('==========================生成器===========================================')


def fibonacci(n):
    a, b = 0, 1
    counter = 0
    while True:
        if counter > n:
            return
        yield a  # 每次遇到yield函数会暂停并保存当前信息,返回yield值,运行next时从此处迭代
        a, b = b, a + b
        counter += 1


# 看起来就是一个尾递归

f = fibonacci(10)
while True:
    try:
        print(next(f), end=' ')  # 碰到next后才执行yield后面语句
    except StopIteration:
        sys.exit()
# https://www.runoob.com/w3cnote/python-yield-used-analysis.html
