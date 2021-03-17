import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        """外星人继承精灵组"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # 更改图形大小
        self.image = pygame.transform.smoothscale(self.image, (self.rect.width // 2, self.rect.height // 2))
        self.rect.width /= 2
        self.rect.height /= 2

        # 设置外星人在屏幕上的位置
        self.rect.x = self.rect.width  # x代表rect的 左边距
        self.rect.y = self.rect.height  # y代表rect的上边距

        # 储存准确位置
        self.x = float(self.rect.x)

    def check_edges(self):
        """检测屏幕边缘"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:  # 图像右坐标大于屏幕右坐标
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        """绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """向右或左移动外星人"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction  # self.x跟踪外星人位置
        self.rect.x = self.x
