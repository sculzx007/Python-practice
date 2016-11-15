# 目的：使用小矩形画出一个正弦曲线
"""
import pygame, sys
import math                   #因为需要用到 sin() 函数，所以需要导入math 模块
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
for x in range (0, 640):                    #从左到右循环，由x=0到x=639
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)   #计算每个点的垂直坐标（y坐标）
    pygame.draw.rect(screen, [0, 0, 0],[x, y, 1, 1], 1)     #使用小矩形来画点
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

"""
                                                   # 改进方法
# 目的：使用小矩形画出一个正弦曲线，并用一条直线将其连接起来

import pygame, sys
import math                   #因为需要用到 sin() 函数，所以需要导入math 模块
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
plotPoints = []
for x in range (0, 640):                    #从左到右循环，由x=0到x=639
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)   #计算每个点的垂直坐标（y坐标）
    plotPoints.append([x, y])              #将各个点添加到列表中
pygame.draw.lines(screen, [0, 0, 0], False, plotPoints, 2)     #使用draw_lines()函数画出整条曲线
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
