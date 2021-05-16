# !/usr/bin/python3
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b  # 12 = 0000 1100
print("1 - c 的值为: ", c)

c = a | b  # 61 = 0011 1101
print("2 - c 的值为: ", c)

c = a ^ b  # 49 = 0011 0001
print("3 - c 的值为: ", c)  # 两位相异为1

c = ~a  # -61 = 1100  0011
print("4 - c 的值为: ", c)  # 按位取反

a = 111
isinstance(a, int)
a = 1112
isinstance(a, int)


# ============================type()==判断未知数据类型=============================
# ============================instance()===================================
# isinstance()会认为子类属于一种父类类型:(主要用于判断是否A继承了B类)
class father(object):
    pass


class son(father):
    pass


if __name__ == '__main__':
    print(type(son()) == father)  # False
    print(isinstance(son(), father))  # True
    print(type(son()))  # <class '__main__.son'>
    print(type(son))  # <type 'type'>
