import sys


def fabonicco(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        else:
            yield a  # 后面可以加多个数据,返回元组
            a, b = b, a + b
            counter += 1


f = iter(fabonicco(10))
while True:
    try:
        print(next(f))
    except:
        sys.exit()
