import csv

import matplotlib.pyplot as plt
from matplotlib import pyplot as py
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)  # 传递给csv,创建阅读器对象
    header_row = next(reader)  # csv模块内置next,用于换行(原理是迭代器)
    # print(header_row)  # 阅读器以逗号分割对象# 这里只进行了一行的操作

    dates = []
    highs = []
    lows = []
    for row in reader:
        """加入异常处理"""
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:  # 显示缺失数据日期
            print(current_date, 'missing data')
        else:  # 无异常进行下一行
            dates.append(current_date)
            lows.append(low)
            highs.append(high)

for index, column_header in enumerate(header_row):  # 该方法(csv内)获得每个元素的索引和值('enumerate is useful for obtaining an indexed list:'原注释)
    print(index, column_header)

fig = plt.figure(dpi=128)  # 设置分辨率和窗口尺寸(figsize参数为空表示默认)
plt.plot(dates, highs, c='red', alpha=0.5)  # high数据显示为红色
plt.plot(dates, lows, c='blue', alpha=0.5)  # low数据显示为蓝色, alpha参数表示颜色透明度（0-1取值）
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  # 指定填充区域和填充颜色
plt.title("Daily high and low temperatures of Death Valley,CA - 2014", fontsize=18)

plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # 自动设为不重叠

plt.ylabel("Temperature(F)", fontsize=16)
# 设置刻度:
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
