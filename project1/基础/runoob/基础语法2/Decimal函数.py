import decimal

from flask import ctx

decimal.getcontext().prec = 4  # 指定精度(四位小数)
val1 = decimal.Decimal(1) / decimal.Decimal(7)
print(val1)

with decimal.localcontext() as cxt:  # 控制台语句(下面三个)
    ctx.prec = 2
    decimal.Decimal('1.00') / decimal.Decimal('3.00')
