# -*-coding: utf-8 -*-
def dn():
    dgt = []
    num = []
    c = 0
    for c in range(2 ** 16):
        ch = chr(c)
        if ch.isdigit:
            dgt.append(ch)
        if ch.isnumeric():
            num.append(ch)
    print('digits:', dgt)
    print('numeric:', num)


dn()
