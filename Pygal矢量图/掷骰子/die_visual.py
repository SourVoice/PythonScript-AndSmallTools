import pygal

from die import Die

die_1 = Die()
die_2 = Die()
results = []  # 反回结果填进这里
for roll_num in range(1000):
    """摇一百次"""
    result = die_1.roll() + die_2.roll()  # 摇两枚骰子
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)  # 返回value在results总数
    frequencies.append(frequency)

"""创建一个直方图"""
hist = pygal.Bar()  # 创建对象实例

hist.title = "Results of rolling one D6 1000 times."  # 显然明了
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']  # x轴标签
hist.x_title = "Result"  # x轴标题
hist.y_title = "Frequency of Result"
hist.add("D6 + D6", frequencies)  # 添加标签标识(图例D6)
hist.render_to_file('die_visual.svg')  # 渲染为svg格式并保存,使用web打开
