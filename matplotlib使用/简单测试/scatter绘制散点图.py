import matplotlib.pyplot as plt

# 传递下面两个参数以绘制一系列点(可以写成表达式)

x_value = list(range(1, 1001))
y_value = [x ** 2 for x in x_value]  # 迭代表达式

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues,
            edgecolors='none', s=10)  # 参数设置点的大小
# edgecolors=参数设置了点的轮廓
# c=''修改数据点颜色,可以设置RGB值
# c参数设置成y的列表,使用参数cmap来告诉pyplot使用哪个颜色映射(映射可以从matplotlib官网找到color example)

# 设置图标标题y_value# 设定图标标题并为坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Number", fontsize=14)

# 设定刻度样式,axis指定影响两个轴,major表示主刻度
plt.tick_params(axis='both', which='major', labelsize=14)


# 设定坐标轴取值范围
plt.axis([0, 1100, 0, 1100000])
plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')  # 改行将生成的图保存进该目录,第二个参数表示裁掉多余空白区域
