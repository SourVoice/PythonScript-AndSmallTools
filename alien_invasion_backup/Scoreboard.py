import pygame.font


class Scoreboard(object):
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, starts):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.starts = starts

        # 显示得分信息时使用的字体设置
        self.text_color = (20, 20, 20)  # 字体颜色
        self.font = pygame.font.SysFont(None, 48)  # 默认字体, 字号48

        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """将圆整的得分渲染到屏幕"""
        rounded_score = round(self.starts.score, -1)  # round表示将小数精确,第二个参数表示精确度,负数表示最近的10,,100,...整倍
        score_str = "{:,}".format(rounded_score)  # 字符串格式设置指令,插入逗号
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        # 显示在右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20  # 分数增大会向左移,所以将其锁定右边
        self.score_rect.top = 20

    def show_score(self):
        """在计分板上显示"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_high_score(self):
        """将最高分渲染为图像"""
        high_score = round(self.starts.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # 设置在最顶端
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
