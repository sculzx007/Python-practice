import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])                                          #这行代码的意思是使用白色背景填充窗口
pygame.draw.circle(screen, [255, 0, 0], [320, 240], 30, 0)
"""
draw.circle()函数表示画一个圆，
相应的属性：
在哪里画：screen，及显示表面
用什么颜色：[255, 0, 0]表示红色(RGB)
位置：[100, 100] 表示从左上角向下100像素再向右100像素的位置，这个位置是圆心
圆的半径：30像素
线宽：0，表示圆是完全填充的

"""
pygame.display.flip()                                         #    flip(翻转)

while True:                 #大小写是有区别的,大写的True表示真假，而小写的true则是一个变量
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()                   #这个函数的作用的定义窗口的"X"是退出游戏
    
