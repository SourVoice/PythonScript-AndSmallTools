list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print("更行后列表:", list)
# append向列表尾部添加一个新元素

# append是浅拷贝,即只拷贝了引用
a_list = []
num = [2]
a_list.append(num)
print(id(num) == id(a_list[0]))
# 上面这种情况会使num改变同时也改变了a_list
# 改变num时直接使用num=[1]会改变id,而使用num[0]=1则不会\
# 改变id,同时a_list也改变

import copy
# 采用深拷贝解决:
a_list.append(copy.deepcopy(num))
