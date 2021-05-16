# 类
'''
class CocaCoca:
    it_taste = 'So good!'


coke_for_bum = CocaCoca()
coke_for_president = CocaCoca()

print(coke_for_bum.it_taste)
print(coke_for_president.it_taste)
'''


class CocaCoca:
    formula = ['caffeine', 'sugar', 'water', 'soda']


coke_for_you = CocaCoca()
coke_for_me = CocaCoca()
print(CocaCoca.formula)
print(coke_for_me.formula)
print(coke_for_you.formula)

# for element in coke_for_me.formula():
#    print(element)


print(4 & 8)  # 按位与与运算,都为1才为1
print(4 | 8)  # 按位或,有1即为1
print(4 << 8)  # 位运算,右移,高位溢出,低位补零(截断)
print(4 >> 8)  # 位运算,左移,高位补零,低位溢出(截断)  # 位运算速度快
