import pygame.font  # 将文本渲染至屏幕


class Button(object):

    def __init__(self, ai_settings, screen, msg):  # msg应为一个str类型
        """初始化按钮属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮尺寸
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)  # 按钮设置为亮绿色
        self.text_color = (255, 255, 255)  # 白色文本
        self.font = pygame.font.SysFont(None, 48)  # None指定使用默认字体渲染

        # 创建按钮的rect
        self.rect = pygame.Rect(0, 0, self.width, self.height)  # 设置图像的大小
        self.rect.center = self.screen_rect.center  # 居中

        # 创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像,并浮于按钮上方居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)  # bool实参表示反锯齿功能的开启和关闭

        self.msg_image_rect = self.msg_image.get_rect()  # 获得渲染的图像对象
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制按钮"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
