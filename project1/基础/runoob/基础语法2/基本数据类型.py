var1 = 1
var2 = 10
# del var1  # 删除了var1,所以下一句会报错(删除对象引用)
# print(var1)

# del var1, var2
# print(var1, var2)


# string:====================================================

str = 'Runoob'
print(str)
print(str[0:-1])
print(str[2:5])  # 不包含第二个
print(str * 2)  # 输出两次
print(r'Ru\noob')  # 加r时转意字符不发生

# list===========================================================
list = ['abcd', '7806', '2.23', 'runoob', '70.9']
tinylist = [123, 'runoob']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

letters = ['r', 'u', 'u', 'n', 'o', 'o', 'b']
element = letters[1:4:2]  # 第三个参数为截取步数,第一个,第三个
# 第三个参数若为负数表示逆项读
print(element)
# 关于列表的创建细节补充：
# >>> o = {1, 2, 3}
# >>> type(o)
# <class 'set'>
# >>> o = {}              ----------------空的认为是字典
# >>> type(o)
# <class 'dict'>
print('\n')


def reverse_Words(input):
    # 用空格分隔字符串
    input_Words = input.split(" ")  # split()划分为列表的函数

    # inputs_Words[-1: :-1]
    # 第二个参数为空, 表示移动到列表末尾\
    # 第三个-1表示步长, -1表示逆向,
    input_Words = input_Words[-1::-1]

    # 重新组合字符串
    output = ' '.join(input_Words)
    return output


if __name__ == '__main__':
    input = 'I like runoob'
    rw = reverse_Words(input)
    print(rw + '\n')

# !/user/bin/python3
# 元组(tuple)-----------------------------------------------

tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tuple + tinytuple)
print('\n')

tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素,需要加逗号
tup = (1, 2, 3, 4, 5, 6)
print(tup[0])
print(tup[1:5])
# tup[0] = 11  # 修改元组元素的操作是非法的
print('\n')

# 集合(...)---------------------------------------------------
a = set('abracadabra')
b = set('alacazam')
# 集合具有数学性质,打印时有互异性,其他数据类型则无这一性质
set_text = {'tom', 'tom', 'jerry'}
print(set_text)

print(a)
print(a - b)  # 差集
print(a | b)  # 并集
print(a & b)  # 交集
print(a ^ b)  # 不同时存在
print('\n')

# 字典{}------------------------------------------------------
# 键(key): 值(value),key不可变
# !/user/bin/python3
dict = {}
dict['one'] = "1 - 教程"
dict[2] = "2 - 工具"
tinydict = {
    'name': 'runoob',
    'code': 1,
    'site': 'www.runoob.com'
}
print(dict['one'])
print(dict[2])
print(tinydict)  # 输出完整字典
print(tinydict.keys())  # 输出所有键值
print(tinydict.values())  # 输出所有的值
# 构造函数  dict(),直接从键值对序列中构建字典
# 下面语句在控制台使用:
# dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
# {x: x * 2 for x in (2, 4, 6)}
# dict(Runoob = 1, Google = 2, Taobao = 3)
# 输出字典的key和value
for c in dict:
    print(c, ':', dict[c])
# 或者:
print('\n')
for c in dict:
    print(c, end=':')
    print(dict[c])
# 仅打印c的话仅打印所有的key
# 字典推导式
p = {i: str(i) for i in range(1, 5)}
print("p:", p)

# 更精确的浮点数计算
from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))