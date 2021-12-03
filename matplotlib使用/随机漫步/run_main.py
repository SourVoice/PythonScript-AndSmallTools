import matplotlib.pyplot as plt
from random_walk import RandomWalk

if __name__ == '__main__':

    while True:
        rw = RandomWalk(12000)  # 增大点数二十万(12-18)一下较好(原始尺寸下),这样已经太慢了而且再大图形将不好看了
        rw.fill_walk()
        plt.figure(dpi=128, figsize=(10, 6))  # 设置matplotlib尺寸(英寸),还可以指定分辨率,背景色.dpi=为分辨率参数(每英寸)

        points_numbers = list(range(rw.num_points))  # 随机一些点来进行颜色映射
        # 绘制更明显的起点和终点
        plt.scatter(0, 0, c='green', edgecolors='none', s=100)
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
        # 起点和终点的位置在前面, 以表示在绘制整体之前
        plt.scatter(rw.x_values, rw.y_values, c=points_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
        # edgecolors用来设置每个点的轮廓(消除后更清楚)
        # plt.axes().get_xaxis().set_visible(False)
        # plt.axes().get_yaxis().set_visible(False)  # 隐藏坐标轴

        plt.show()

        keep_running = input("make another walk?(y/n)")
        if keep_running == 'n':
            break
