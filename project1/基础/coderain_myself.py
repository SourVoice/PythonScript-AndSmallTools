from pygame.sprite import Sprite
import pygame
import random
from random import randint
from pygame.locals import *  # 自动导入pygame的所有常量

high_speed = 2
low_speed = 1
font_color = (0, 150, 0)
screen_width = 400
screen_height = 100
screen_color = (0, 0, 0)
font_name = "D:/pythonFile/项目/coderain/font.ttf"
font_size = 20
frequency = 60  # 显示帧数
font_num = 10  # 一列占10个像素


def random_speed():
    return randint(low_speed, high_speed)


def random_position():
    return randint(0, screen_width), randint(0, screen_height)


def random_text():
    return random.choice("I love you!")


class Show(Sprite):  # 精灵组类
    def __init__(self, born_position):
        super(Show, self).__init__()
        self.font = pygame.font.Font(font_name, font_size)
        self.image = self.font.render(str(random_text()), True, font_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = born_position
        self.speed = random_speed()

    def update(self):  # 重写了update
        self.rect = self.rect.move(0, self.speed)  # x轴不移动,仅沿y轴移动
        if self.rect.top > screen_height:
            self.kill()


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('code_rain')
screen.fill(screen_color)
# pygame.display.flip()
group = pygame.sprite.Group()
group_nums = int(screen_width / font_num)

clock = pygame.time.Clock()  # 创建一个敲钟

while True:
    time = clock.tick(frequency)  # 敲钟率
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((0, 0, 0))
    for i in range(0, group_nums):
        group.add(Show((i * font_num, -font_num)))

    group.update()
    group.draw(screen)  # 专门用于精灵组的画面渲染
    pygame.display.flip()  # 刷新屏幕
