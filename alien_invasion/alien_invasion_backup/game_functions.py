import sys
import pygame
from bullet import Bullet
from alien import Alien
import time
from lose_ship import ShowLose


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height -
                         (4 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def get_number_aliens_x(ai_setting, alien_width):
    """一行可以构建的外星人的数量"""
    available_space_x = ai_setting.screen_width - 2 * alien_width  # 创建外星人可用空间
    number_alien_x = int(available_space_x / (2 * alien_width))  # 一个外星人占两个人的宽度(函数range需要一个整数做参数)
    return number_alien_x


def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    alien = Alien(ai_setting, screen)  # alien有了Alien的属性
    alien_width = alien.rect.width  # alien图像的宽度赋到alien_width中

    # 创建新一个(下面一行)并将其加到该行
    alien.x = alien_width + 2 * alien_width * alien_number  # 外星人位置(左边距)的计算
    alien.rect.x = alien.x  # 左边距赋到图形的横坐标
    aliens.add(alien)  # 编组进aliens

    # 新创建一行
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number + 50


# 创建外星人群
def create_fleet(ai_setting, screen, ship, aliens):
    # 重构函数
    # 获取行可容纳量
    alien = Alien(ai_setting, screen)
    number_alien_x = get_number_aliens_x(ai_setting, alien.rect.width)

    # 获取可创建行数
    alien_height = alien.rect.height
    ship_height = ship.rect.height
    number_rows = get_number_rows(ai_setting, ship_height, alien_height)
    # 通过for循环创建一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_setting, screen, aliens, alien_number, row_number)


# 重构处理按键函数,将KEYDOWN和KEYUP分开
def check_event_keydown(event, ai_settings, screen, ship, bullets):
    """按下按键"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, bullets, screen, ship)


def fire_bullets(ai_settings, bullets, screen, ship):
    """创建一颗新子弹并将其加入到编组"""
    # 加入子弹限制
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullets = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullets)


def check_event_keyup(event, ship):
    """松开按键"""
    if event.key == pygame.K_RIGHT:  # event.key是接受的按键响应
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def check_events(ai_settings, screen, ship, aliens, bullets, starts, play_button):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()  # get_pos返回一个元组包含单击时的x,y
            check_play_button(ai_settings, screen, starts, ship, aliens, bullets, play_button, mouse_x,
                              mouse_y)

        elif event.type == pygame.KEYDOWN:
            check_event_keydown(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_event_keyup(event, ship)


def check_play_button(ai_settings, screen, starts, ship, aliens, bullets, play_button, mouse_x, mouse_y):
    """玩家单击play:"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    # 位于区域内点击后,并且非活跃才能启动,防止游戏中途点击play后重置游戏
    if button_clicked and (not starts.game_active):  # 该函数检测单击时的x,y是否位于play.rect内
        # 隐藏光标:
        pygame.mouse.set_visible(False)

        # 重新配置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 重置游戏,活跃设置为False
        starts.reset_starts()
        starts.game_active = True

        # 清空外星人和子弹
        aliens.empty()
        bullets.empty()

        # 创建新的外星人群组,使飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_bullets(ai_settings, screen, starts, sb, bullets, ship, aliens):
    bullets.update()  # 更新子弹状态,bullets位于编组,所以编组自动对每个bullets都调用了该函数
    # 消除消失的子弹
    for bullet in bullets.copy():  # 遍历副本?:源列表正向删除会使下一个元素向前移动,会改变列表,而对副本遍历不会出现源列表错位问题
        # bullets[::]也可以创建副本
        if bullet.rect.bottom <= 0:  # 子弹底部消失
            bullets.remove(bullet)
    # print(len(bullets))  # 核实
    # 检查是否有子弹击中外星人(重构)
    check_bullet_alien_collisions(ai_settings, screen, starts, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, starts, sb, ship, aliens, bullets):
    # 检查是否有子弹击中外星人
    # groupcollide能自动检测两组精灵中元素的碰撞,并返回一个字典
    # 检测rect的重叠,并添加到一键一值对,两个实参TRUE告诉删除bullet和alien(True表示删除)
    """
    Given two groups, this will find the intersections between all sprites in each group. It returns a dictionary
    of all sprites in the first group that collide. The value for each item in the dictionary is a list of the
    sprites in the second group it collides with. The two dokill arguments control if the sprites from either group
    will be automatically removed from all groups. Collided is a callback function used to calculate if two sprites
    are colliding. it should take two sprites as values, and return a bool value indicating if they are colliding. If
    collided is not passed, all sprites must have a "rect" value, which is a rectangle of the sprite area that will
    be used to calculate the collision. < Python 3.7 (项目) >
    """
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():  # collision返回一个字典,所以我们检查键值而不是键,其中子弹为键,与子弹相关的值(这里时发生碰撞的外星人)都是一个列表,所以统计列表长度
            starts.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(starts, sb)

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


# 每次while后的屏幕更新替换为对应下面函数
def update_screen(ai_settings, screen, sb, ship, bullets, alien, play_button, starts):
    screen.fill(ai_settings.bg_color)

    if starts.game_active is True:
        # 绘制子弹
        for bullet in bullets.sprites():  # 绘制位置一定要在屏幕绘制好之后
            bullet.draw_bullet()

        # 绘制飞船
        ship.blitme()

        # 绘制外星人(要求在绘制前两者之后)
        alien.draw(screen)  # 只有draw函数能绘制编组,之前定义的blitme没用了

        # 显示最高分
        sb.show_score()

        pygame.display.flip()

    # 绘制按钮在所有的之后,且进位于游戏非活动
    if starts.game_active is False:
        play_button.draw_button()

        pygame.display.flip()


def check_fleet_edges(ai_settings, aliens):
    """检测边缘"""
    for alien in aliens.sprites():
        if alien.check_edges():  # 若在边缘,执行下面函数
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """整群外星人下移,并改变方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1  # 改变方向


def ship_hit(ai_settings, starts, screen, ship, aliens, bullets, sl):
    """响应碰撞"""
    if starts.ship_left >= 1:
        # 飞船数减一
        starts.ship_left -= 1

        # 清空外星人列表和子弹列表
        bullets.empty()
        aliens.empty()

        # 创建新的外星人,并重置飞船的位置
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sl.prep_msg()
        sl.show_msg()
        pygame.display.flip()
        time.sleep(1.0)
    else:
        starts.game_active = False  # 玩家损失了所有飞船,运用此参数(game_active)来控制主程序的运行
        pygame.mouse.set_visible(True)  # 结束后显示光标


def update_aliens(ai_settings, starts, screen, aliens, ship, bullets, sl):
    """更新外星人编组"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人与飞船碰撞
    # 该函数专门用于检测精灵和编组成员的碰撞,并在找到碰撞成员后停止遍历
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, starts, screen, ship, aliens, bullets, sl)

    # 检测外星人触底
    check_aliens_bottom(ai_settings, starts, screen, ship, aliens, bullets, sl)


def check_aliens_bottom(ai_settings, starts, screen, ship, aliens, bullets, sl):
    """检查外星人触底"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom == screen_rect.bottom:
            ship_hit(ai_settings, starts, screen, ship, aliens, bullets, sl)
            break  # 无需检查其他外星人


def check_high_score(starts, sb):
    """检查最高分的诞生"""
    if starts.score > starts.high_score:
        starts.high_score = starts.score
        sb.prep_high_score()
