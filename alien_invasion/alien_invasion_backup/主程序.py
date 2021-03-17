import pygame
from set_class import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group  # 创建一个编组用于存储所有的有效bullet,使用该编组在屏幕上绘制兹迪纳,并更新每颗子弹位置
from game_starts import GameStarts
from buotton import Button
from Scoreboard import Scoreboard
from lose_ship import ShowLose


# from alien import Alien


def run_game():
    # 创建游戏窗口
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)  # 加括号传入一个参数
    )  # display.set_mode(resolution=(0, 0))第一个参数为一个二元组,表示宽和高
    pygame.display.set_caption("Alien Invasion")
    screen.fill(ai_settings.bg_color)

    # 创建按钮
    play_button = Button(ai_settings, screen, "Play")
    play_button.draw_button()
    pygame.display.flip()

    # 存储游戏统计信息的实例
    starts = GameStarts(ai_settings)
    sb = Scoreboard(ai_settings, screen, starts)

    # 失败后显示
    string = "You lost a ship!"
    sl = ShowLose(ai_settings, screen, string)

    # 导入飞船
    ship = Ship(ai_settings, screen)

    # 创建编组
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始主循环:
    while True:
        # 响应玩家指令
        gf.check_events(ai_settings, screen, ship, aliens, bullets, starts, play_button)  # 代替上面语句

        if starts.game_active:
            # 根据指令更新飞船位置
            ship.update()

            # 根据指令更新子弹
            gf.update_bullets(ai_settings, screen, starts, sb, bullets, ship, aliens)
            gf.update_aliens(ai_settings, starts, screen, aliens, ship, bullets, sl)

        gf.update_screen(ai_settings, screen, sb, ship, bullets, aliens, play_button, starts)  # 重新绘制屏幕


run_game()
