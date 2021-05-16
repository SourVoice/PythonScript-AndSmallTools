# 字符 "" 是假，其他都是真；
# 成员运算符
a = 10
b = 20
lsit = [1, 2, 3, 4, 5]
if a in list:
    print("1 - 变量 a 在给定的列表中list 中")
else:
    print("1 - 变量 a 不在给定列表 list 中")
if b not in list:
    print("2 - b 不在给定列表 list 中")
else:
    print("2 - 变量 b 在给定列表 list 中")

# 修改变量 a 的值
a = 2
if a in list:
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")

# 身份运算符
# !/user/bin/python3
a = 20
b = 20
if a is b:
    print("1 - a 和 b 有相同的标识(地址)")
else:
    print("2 - a 和 b 没有相同标识")
if id(a) == id(b):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")
b = 30
if a is b:
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if a is not b:
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")
