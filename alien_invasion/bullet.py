import pygame
from pygame.sprite import Sprite  # 精灵将游戏中相关的元素编组,进而同时操作编组中所有元素


class Bullet(Sprite):
    """管理子弹"""

    def __init__(self, ai_settings, screen, ship):
        # 在飞船位置处创建一个子弹对象
        super(Bullet, self).__init__()  # Bullet类继承了导入的精灵(Sprite)
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形,再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)  # pygame.Rect()从空白开始创建了一个矩形
        # 前两个参数表示创建矩形的位置,下面两行将矩形移动到了正确的位置

        self.rect.centerx = ship.rect.centerx  # 对齐飞船的中心
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置,便于微调子弹速度
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新子弹 位置
        self.y -= self.speed_factor

        # 更新子弹的rect设置(bullet的y给到)
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
