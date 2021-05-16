name = '柏林'
print(name)
print('标识', id(name))  # 地址
print('类型', type(name))
print(1.1 + 2.2)

from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))

s1 = 128
f1 = 98.7
s2 = '76 77'
ff = True
s3 = 'hello'
print(int(s1), type(int(s1)))  # 将str转换成int,字符串必须为数字串
# print(int(s2), type(int(s2)))  # 将str转换成int,报错,小数串算字符串
# print(int(s3), type(int(s3)))  # str转int必须为整数串


# present = input('大声想要什么礼物呢?')
# input默认返回str
# 计算前必须进行转换


print(9 // -4)  # 向下取整,的负三(  // 整除符号 )
print(9 % -3)  # 一正一负遵循公式: 余数 = 被除数 - 除数*商
# (0 , 除数)为余数范围


a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))

# 交换两变量
a, b = b, a

'''
一个变量包含 :1. 标识, 2. 类型, 3. 值
比价对象标识的运算符符:  is

'''
a = 10
b = 10
print(a is b)  # 说明运用了相同的地址(指向了同一个对象)
print(a == b)
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
print(list1 == list2)  # 列表的值相同
print(list1 is list2)  # 列表的地址不同
print(id(list1))
print(id(list2))
# 否定判断:  is not
