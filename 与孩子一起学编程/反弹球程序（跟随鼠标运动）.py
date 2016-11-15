#目的：学会让程序响应鼠标的操作
#方法： 在while的for循环中，使用rect.center事件。

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
background = pygame.Surface(screen.get_size())
background.fill([255, 255, 255])
clock = pygame.time.Clock()
delay = 100
interval = 50
pygame.key.set_repeat(delay, interval)            #定义了当键盘一直按住时的操作，delay定义了开始重复前等待多长时间，interval则定义了按键要以多快的速度重复

class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self):
        if self.rect.left <= screen.get_rect().left or self.rect.right >= screen.get_rect().right:
            self.speed[0] = -self.speed[0]
        newpos = self.rect.move(self.speed)
        self.rect = newpos

my_ball = Ball("beach_ball.png", [10,0], [20,20])     #建立球的实例，速度为10像素/ms,位置为（20, 20）

held_down = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
#以下为定义当鼠标拖动时，球跟着鼠标动
            
        elif event.type == pygame.MOUSEBUTTONDOWN:       #当鼠标按下时，事件开始执行
            held_down = True
        elif event.type == pygame.MOUSEBUTTONUP:             #当鼠标松开时，事件结束
            held_down = False
        elif event.type == pygame.MOUSEMOTION:
            if held_down:                                                              #当鼠标拖动时，球才跟着移动
                my_ball.rect.center = event.pos
        
            
    clock.tick(30)            #这是时钟的代码
    screen.blit(background, (0, 0))
    my_ball.move()
    screen.blit(my_ball.image, my_ball.rect)
    pygame.display.flip()
