class Settings(object):
    """储存所有设置"""

    def __init__(self):
        """初始化游戏设置"""

        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed_factor = 1.5  # 速度限制(每次循环最多移动的距离)
        self.ship_limit = 3

        # 开始设置bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 设置外星人速度
        self.alien_speed_factor = 0.08  # 横向移动速度
        self.fleet_drop_speed = 2  # 向下移动速度
        self.fleet_direction = 1  # 设置移动方向

        """以下为游戏的难度增加和失败重置模块"""
        # 加快游戏的速度
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # 游戏结束后重置难度
        self.initialize_dynamic_settings()

        # 计分
        self.alien_points = 50

    def initialize_dynamic_settings(self):
        """游戏配置随游戏的进行而变化(重新配置为初始状态)"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.08

        # fleet_direction使游戏开始外星人总向右移动
        self.fleet_direction = 1

    def increase_speed(self):
        """随等级提高速度配置"""
        # 提高了1.1倍
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        # 得分也响应提高
        self.alien_points *= int(self.alien_points * self.score_scale)
