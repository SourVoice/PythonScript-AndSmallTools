import pygame


# 引入飞船类

class Ship(object):
    def __init__(self, ai_settings, screen):  # 引用对象和screen,screen用于指定飞船绘制位置
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_setting = ai_settings  # ship获取了set_settings的所有属性(从主函数传入ai_settings,这里面由让ai_settings获取其属性)

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(
            'images/ship.bmp')  # 加载图像,该函数返回飞船的surface(surface是pygame的画图对象，可以理解为画板,就是返回画面内容到屏幕上)
        self.rect = self.image.get_rect()  # rect对象用于储存矩形属性(将图像属性放置于rect对象中)
        self.screen_rect = screen.get_rect()  # get_rect()返回rect,详情看:/
        # https://blog.csdn.net/weixin_39480632/article/details/81273020

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  # 前面表示飞船中心x坐标,并将其设为screen的矩形的属性
        self.rect.bottom = self.screen_rect.bottom  # 飞船下边缘的y坐标设置为表示屏幕的矩形的属性bottom

        # 再飞船的rect属性中存储小数值
        self.center = float(self.rect.centerx)  # 定义了一个可以储存小数的新属性

        # 设置移动属性
        self.move_right = False  # 设置移动标志
        self.move_left = False

    def update(self):  # 移动属性为True时,调用下面的更新飞船位置的方法
        """根据移动标志调整飞船位置"""
        # 更新ship的center值
        # 使用if检测ship是否触及屏幕右(左)边缘
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor

        # rect左边缘的x坐标大于零,则飞船未触及(因为pygame中左上角为(0, 0))
        if self.move_left and self.rect.left > 0:
            # 优先使用if语句,在玩家同时按住两个按键时,将先增大飞船的rect.centerx值,再降低这个值,从而飞船位置不变(同时判断两个if语句)(若使用elif值,
            # 更新center值,也就是只更新小数部分
            self.center -= self.ai_setting.ship_speed_factor  # 则右箭头处于领先位置,操作会不准确)

        # 更新rect对象的属性
        self.rect.centerx = self.center

    def center_ship(self):
        """重置飞船位置"""
        self.center = self.screen_rect.centerx

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)  # 由self.rect绘制飞船到屏幕上
