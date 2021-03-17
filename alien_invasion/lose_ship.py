import pygame.font


class ShowLose(object):

    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.msg = msg

        # 尺寸
        self.text_color = (20, 20, 20)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_msg()
        self.show_msg()

    def prep_msg(self):
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.ai_settings.bg_color)

        # 显示位置
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.screen_rect.center

    def show_msg(self):
        self.screen.blit(self.msg_image, self.msg_rect)
