import pygame
import sys


"""
# 创建空的pygame窗口
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化背景

    screen = pygame.display.set_mode((1200, 800))  # 创建显示窗口,名为screen# screen:宽(像素),高(像素)

    pygame.display.set_caption("Alien Invasion")
    # 设置背景色:
    bg_color = (230, 230, 230)
    screen.fill(bg_color)
    # 开始游戏主循环(控制游戏的事件循环)
    while True:
        # 监视键盘和鼠标时间
        for event in pygame.event.get():  # 事件就是用户玩游戏时执行的操作 # pygame.event.get()用来访问pygame侦测到的事件

            if event.type == pygame.QUIT:  # 检测到玩家单击了游戏窗的关闭按钮
                sys.exit()  # 退游指令
        screen.fill(bg_color)  # 每次循环都重新绘制屏幕
        # 使最近绘制的屏幕可见
        pygame.display.flip()  # 每次while循环都会执行这一指令,用于绘制空屏幕,擦去旧屏幕


run_game()
# 将以上设置封装成类:
"""



