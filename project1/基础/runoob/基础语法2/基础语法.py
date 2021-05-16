#!/user/bin/python3
# windows下可以不用写上面一行注释

import sys; x = 'runoob'; sys.stdout.write(x + '\n')
# 可以在同一行使用多条语句, 语句用分号隔开,write函数能调用Anystr在控制台得到字符数(好像不行
# )

x = "a"
y = "b"
# 不换行输出通过在print末尾加end = " "(在末尾加上了空格)
# ex:
print(x, end=" ")
print(y, end=" ")

print('命令行参数:')
for i in sys.argv:
    print(i)
print('\n python 路径', sys.path)

from sys import argv, path  # 导入特定成员
print('path:', path)  # 因为已经导入path成员, 此处引用不需要用sys.引用
