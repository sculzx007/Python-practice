#目的：学会插入一张已经存在的图片
"""
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([1366, 768])
screen.fill([255, 255, 255])
ball = pygame.image.load("篮球.jpg")  #插入所需的图片
screen.blit (ball, [0,0])                                  #定义图片在screen中的位置
                                         #   screen.blit()函数的作用是把图像“复制”到screen上
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

"""
                                                           #改进-1

#目的：让图片发生移动
"""
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([1366, 768])
screen.fill([255, 255, 255])
ball = pygame.image.load("篮球.jpg")  #插入所需的图片
screen.blit (ball, [0,0])                                  #定义图片在screen中的位置
                                         #   screen.blit()函数的作用是把图像“复制”到screen上
pygame.display.flip()

pygame.time.delay(2000)
screen.blit(ball, [200, 200])
# 以上三行代码是将图片移动一定的位置。
                                 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

"""

                                                           #改进-2

#目的：让图片发生移动，并擦去第一张图片
"""
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([1366, 768])
screen.fill([255, 255, 255])
ball = pygame.image.load("篮球.jpg")  #插入所需的图片
screen.blit (ball, [0,0])                                  #定义图片在screen中的位置
                                         #   screen.blit()函数的作用是把图像“复制”到screen上
pygame.display.flip()

pygame.time.delay(2000)
screen.blit(ball, [200, 200])
pygame.draw.rect(screen, [255, 255, 255], [0, 0, 180, 178], 0)
# 上面这行代码的作用是用一个白色的矩形将原图进行覆盖
pygame.display.flip()
                                 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
"""

                                                          #改进-3

#目的：让图片发生移动，并擦去第一张图片，且能流畅的移动球

"""
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([1366, 768])
screen.fill([255, 255, 255])
ball = pygame.image.load("篮球.jpg")  #插入所需的图片
screen.blit (ball, [0,0])                                  #定义图片在screen中的位置
                                         #   screen.blit()函数的作用是把图像“复制”到screen上
x = 180
y = 178
screen.blit(ball, [x, y])          #指复制图像到[x, y]这个位置
pygame.display.flip()
for looper in range (1, 100):
    pygame.time.delay(20)                                 #20指20毫秒，即0.02秒
    pygame.draw.rect(screen,[255, 255, 255], [x, y, 180, 178], 0)
    x = x + 5
    screen.blit(ball, [x, y])
    pygame.display.flip()
                                 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

"""

                                                          #改进-4

#目的：让图片发生移动，并擦去第一张图片，且能流畅的移动，碰到边界后能弹回

"""
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([1366, 768])
screen.fill([255, 255, 255])
ball = pygame.image.load("篮球.jpg")  #插入所需的图片
screen.blit (ball, [0,0])                                  #定义图片在screen中的位置
                                         #   screen.blit()函数的作用是把图像“复制”到screen上
x = 180
y = 178
x_speed = 10
                                 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    pygame.time.delay(20)                                                       #20指20毫秒，即0.02秒
    pygame.draw.rect(screen,[255, 255, 255], [x, y, 180, 178], 0)
    x = x + x_speed
    if x > screen.get_width() - 180 or x < 0:          #当球碰到窗口的任意一边时
        x_speed = - x_speed                                 #改变速度的方向，（由x_speed的正负号决定）

'''
将显示球的代码放在这里，也就是放在while循环内部，这样球就可以不停的进行反弹
'''
    screen.blit (ball, [x, y])
    pygame.display.flip()

"""

                                                                 #改进-5

#目的：让图片发生移动，并擦去第一张图片，且能流畅的移动，碰到边界后能弹回（水平和垂直方向）

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([1366, 768])
screen.fill([255, 255, 255])
ball = pygame.image.load("篮球.jpg")  #插入所需的图片
screen.blit (ball, [0,0])                                  #定义图片在screen中的位置
                                         #   screen.blit()函数的作用是把图像“复制”到screen上
x = 180
y = 178
x_speed = 10
y_speed = 10                      #为y-speed增加代码，即为垂直运动
                                 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    pygame.time.delay(20)                                                       #20指20毫秒，即0.02秒
    pygame.draw.rect(screen,[255, 255, 255], [x, y, 180, 178], 0)
    x = x + x_speed
    y = y + y_speed
    if x > screen.get_width() - 180 or x < 0:          #当球碰到窗口的任意一边时
        x_speed = - x_speed                                 #改变速度的方向，（由x_speed的正负号决定）
    if y > screen.get_height()-178 or y < 0:
        y_speed = -y_speed
    screen.blit (ball, [x, y])
    pygame.display.flip()
