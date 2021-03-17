class GameStarts(object):

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_starts()

        # 游戏启动时处于非活动状态
        self.game_active = False

        # 不重置最高分
        self.high_score = 0

    def reset_starts(self):
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
