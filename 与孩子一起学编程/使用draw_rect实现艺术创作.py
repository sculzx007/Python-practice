#目的：创建100个随机位置和大小的正方形
"""
import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode([640, 480])      # 定义显示屏幕大小为640x480 像素
screen.fill ([255, 255, 255])                                   # 定义背景色为白色（RGB值为[255, 255, 255]）
for i in range(100):                                               # 选择创建正方形的个数
    width = random.randint(0,250)                          # 正方形宽度的范围，在0-250间随机选择一个
    height = random.randint(0, 100)                        # 正方形长度的范围
    top = random.randint(0, 400)
    left = random.randint(0, 500)                            # 这两行为正方形的位置
    pygame.draw.rect(screen, [0, 0, 0], [left, top, width, height], 1)                 #使用draw_rect()函数
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
"""
"""
输出结果：会随机生成100个形状大小不等，位置不一样的黑白色正方形
"""

#改进：随机生成100个位置、大小、形状、线宽不一致的正方形

import pygame, sys, random
from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode([640, 480])      # 定义显示屏幕大小为640x480 像素
screen.fill ([255, 255, 255])                                   # 定义背景色为白色（RGB值为[255, 255, 255]）
for i in range(100):                                               # 选择创建正方形的个数
    width = random.randint(0,250)                          # 正方形宽度的范围，在0-250间随机选择一个
    height = random.randint(0, 100)                        # 正方形长度的范围
    top = random.randint(0, 400)
    left = random.randint(0, 500)                            # 这两行为正方形的位置
    color_name = random.randint(THECOLORS.key())            #从THECOLORS.key()函数中随机选取颜色名字
    color = THECOLORS[color_name]                #根据颜色的名字输出不同的颜色
    line_width = random.randint(1, 3)                    #线宽范围为1-2
    pygame.draw.rect(screen, color, [0, 0, 0], [left, top, width, height], line_width)                 #使用draw_rect()函数
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

"""
输出结果：AttributeError: 'dict' object has no attribute 'key'  ，即不存在 key() 函数
"""
