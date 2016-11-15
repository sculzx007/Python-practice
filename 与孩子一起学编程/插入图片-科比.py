#目的：学会插入一张已经存在的图片
"""
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([750, 752])
screen.fill([255, 255, 255])
kobe = pygame.image.load("科比退役.png")  #插入所需的图片
screen.blit (kobe, [0,0])                                  #定义图片在screen中的位置
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
screen = pygame.display.set_mode([1440, 900])
screen.fill([255, 255, 255])
kobe = pygame.image.load("科比退役.png")  #插入所需的图片
screen.blit (kobe, [0,0])                                  #定义图片在screen中的位置
                                         #   screen.blit()函数的作用是把图像“复制”到screen上
pygame.display.flip()

pygame.time.delay(2000)    #表示2秒后显示新的图像
screen.blit(kobe, [250, 250])
pygame.display.flip()
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
screen = pygame.display.set_mode([1440, 900])
screen.fill([255, 255, 255])
kobe = pygame.image.load("科比退役.png")  #插入所需的图片
screen.blit (kobe, [0,0])                                  #定义图片在screen中的位置
                                         #   screen.blit()函数的作用是把图像“复制”到screen上
pygame.display.flip()

pygame.time.delay(2000)
screen.blit(kobe, [250, 250])
pygame.draw.rect(screen, [255, 255, 255], [0, 0, 750, 752], 0)
# 上面这行代码的作用是用一个白色的矩形将原图进行覆盖
pygame.display.flip()
                                 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
"""

                                                          #改进-2

#目的：让图片发生移动，并擦去第一张图片

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([1440, 900])
screen.fill([255, 255, 255])
kobe = pygame.image.load("科比退役.png")  #插入所需的图片
screen.blit (kobe, [0,0])                                  #定义图片在screen中的位置
                                         #   screen.blit()函数的作用是把图像“复制”到screen上
pygame.display.flip()

pygame.time.delay(2000)
screen.blit(kobe, [250, 250])
pygame.draw.rect(screen, [255, 255, 255], [0, 0, 750, 752], 0)
# 上面这行代码的作用是用一个白色的矩形将原图进行覆盖
pygame.display.flip()
                                 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
