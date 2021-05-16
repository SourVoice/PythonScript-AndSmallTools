import csv

import matplotlib.pyplot as plt
from matplotlib import pyplot as py
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)  # 传递给csv,创建阅读器对象
    header_row = next(reader)  # csv模块内置next,用于换行(原理是迭代器)
    # print(header_row)  # 阅读器以逗号分割对象# 这里只进行了一行的操作

    dates = []
    highs = []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
    print(highs)

for index, column_header in enumerate(header_row):  # 该方法(csv内)获得每个元素的索引和值('enumerate is useful for obtaining an indexed list:'原注释)
    print(index, column_header)

fig = plt.figure(dpi=128)  # 设置分辨率和窗口尺寸(figsize参数为空表示默认)
plt.plot(dates, highs, c='red')  # high数据显示为红色
plt.title("Daily high temperatures, July 2014", fontsize=24)

plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # 自动设为不重叠

plt.ylabel("Temperature(F)", fontsize=16)
# 设置刻度:
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
