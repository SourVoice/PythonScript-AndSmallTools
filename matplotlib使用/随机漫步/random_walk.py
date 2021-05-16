import get_step as gs


class RandomWalk(object):
    """"""

    def __init__(self, num_points=5000):
        """初始化漫步,设为默认值"""
        self.num_points = num_points

        # 随机漫步始于(0,0),给出坐标
        self.x_values = [0]
        self.y_values = [0]
        self.gs = gs

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            # 步方向和距离都随机
            x_step = gs.get_steps()
            y_step = gs.get_steps()

            # 去掉原地踏步
            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step  # x_value[-1]索引表示最后一个元素
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
