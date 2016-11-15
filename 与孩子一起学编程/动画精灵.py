#目的：创建一个动画精灵（以多个像素或图片组成的一个大像素或者大图片）
"""
import sys, pygame

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)                                     #初始化动画精灵
        self.image = pygame.image.load(image_file)                       #向其中加载图像文件
        self.rect = self.image.get_rect()                                         #得到定义图像边界的矩形
        self.rect.left, self.rect.top = location                                    #设置球的初始位置

size = width, height = 1366, 768
screen = pygame.display.set_mode(size)              #这两句也可以写成  screen = pygame.display.set_mode([1366, 768])
                                                         #但是这两句不仅设置了窗口大小，也定义了width 和 height 两个变量
screen.fill([255, 255, 255])
image_file = "篮球.jpg"
balls = []
for row in range (0, 3):                                       #    row为行数
    for colum in range(0,3):
        location = [colum*180 + 10, row*180 + 10]
        ball = MyBallClass(image_file, location)
        balls.append(ball)                                      #将球增加到列表中
for ball in balls:
    screen.blit(ball.image, ball.rect)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
"""

"""
输出结果：输出了一个3*3的图片矩阵
"""

                                                                     #改进-1

#目的：1.创建一个动画精灵（以多个像素或图片组成的一个大像素或者大图片），并且使其移动起来
#            2.学会使用move()函数，让球移动

"""
import sys, pygame
from random import *


#下面增加对球的定义

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)                                     #初始化动画精灵
        self.image = pygame.image.load(image_file)                       #向其中加载图像文件
        self.rect = self.image.get_rect()                                         #得到定义图像边界的矩形
        self.rect.left, self.rect.top = location                                    #设置球的初始位置
        self.speed = speed                                                             #为球创建一个speed属性


#下面增加对move的定义
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
           self.speed[0] = -slef.speed[0]                             #这几行代码用于检查是否碰到窗口的左右边界，如果碰到，则反弹（反向）

        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]                         #这几行代码用于检查是否碰到窗口的上下边界，如果碰到，则反弹（反向）

#以上为函数的定义
            
# 下面是主程序

size = width, height = 1366, 768
screen = pygame.display.set_mode(size)              #这两句也可以写成  screen = pygame.display.set_mode([1366, 768])
                                                         #但是这两句不仅设置了窗口大小，也定义了width 和 height 两个变量
screen.fill([255, 255, 255])
image_file = "篮球.jpg"
balls = []
for row in range (0, 3):                                       #    row为行数
    for colum in range(0,3):
        location = [colum*180 + 10, row*180 + 10]
        speed = [choice([-2, 2]), choice([-2,2])]
        ball = MyBallClass(image_file, location, speed)
        balls.append(ball)                                      #将球增加到列表中
"""
"""
for ball in balls:
    screen.blit(ball.image, ball.rect)
pygame.display.flip()

#这是源代码，将其移动到while循环中

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.time.delay(20)
    screen.fill([255, 255, 255])        #重新绘制屏幕，并不是“擦除”每一个球，而是重新画一个白色背景，重新画所有的球
    for ball in balls:
        ball.move()
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
"""

                                                                                        #改进-2

#目的：1. 创建一个动画精灵组（而不是列表），并且使其移动起来
#            2.学会 animate()函数的使用——该函数包含了碰撞检测的代码
#            3.学会 Python中group类的使用——该函数包含了碰撞检测的代码

import sys, pygame
from random import *

#下面增加对球的定义

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)                                     #初始化动画精灵
        self.image = pygame.image.load(image_file)                       #向其中加载图像文件
        self.rect = self.image.get_rect()                                         #得到定义图像边界的矩形
        self.rect.left, self.rect.top = location                                    #设置球的初始位置
        self.speed = speed                                                             #为球创建一个speed属性

#下面增加对move的定义
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
           self.speed[0] = -slef.speed[0]                             #这几行代码用于检查是否碰到窗口的左右边界，如果碰到，则反弹（反向）

        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]                         #这几行代码用于检查是否碰到窗口的上下边界，如果碰到，则反弹（反向）


#下面增加对animate()函数的定义

    def animate(group):
        screen.fill([255, 255, 255])
        for ball in group:            
            group.remove(ball)                            #从组中删除精灵

            if pygame.sprite.spritecollide(ball, group, False):                   #检查精灵与组之间的碰撞
                ball.speed[0] = -ball.speed[0]
                ball.speed[1] = -ball.speed[1]
                
            group.add(ball)                                  #将球再添加回原来的组中

            ball.move()
            screen.blit(ball.image, ball.rect)
        pygame.display.flip()
        pygame.time.delay(20)
            
#以上为函数的定义
            
# 下面是主程序

size = width, height = 1366, 768
screen = pygame.display.set_mode(size)              #这两句也可以写成  screen = pygame.display.set_mode([1366, 768])
                                                         #但是这两句不仅设置了窗口大小，也定义了width 和 height 两个变量
screen.fill([255, 255, 255])
image_file = "篮球.jpg"
group = pygame.sprite.Group()                           #创建精灵组
for row in range (0, 2):                                       #    row为行数
    for colum in range(0, 2):
        location = [colum*180 + 10, row*180 + 10]
        speed = [choice([-2, 2]), choice([-2,2])]
        ball = MyBallClass(image_file, location, speed)
        group.add(ball)                                         #将各个球加到组中
"""
for ball in balls:
    screen.blit(ball.image, ball.rect)
pygame.display.flip()
"""

#这是源代码，将其移动到while循环中

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    animate(group)                 #调用animate()函数并传入组group中



