import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
# plot中加入该参数
input_values = [1, 2, 3, 4, 5]
plt.plot(input_values, squares, linewidth=5)  # 决定绘制粗细,在只有一个参数下,plot默认第一个对应x坐标为0

# 设置图表标题,为坐标轴加上标签
plt.title("Square Numbers", fontsize=24)  # fontsize指定文字大小
plt.xlabel("Value", fontsize=14)  # 设置刻度标记和文字大小
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)  # 设定刻度样式,刻度标记字号设为14,both表示两个轴

plt.show()
