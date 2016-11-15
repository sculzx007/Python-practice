class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

        #以上为__init__的使用方法
        
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

#这是创建一个类

#下面建立一个类的实例

myBall = Ball("red", "samll", "down")        #属性作为  __init__()的参数作为输入            
myBall.direction = "down"
myBall.color = "red"
myBall.size = "small"

#设置了一些属性

print "I just created a ball."
print "My ball is ", myBall.size
print "My ball is ", myBall.color
print "My ball's direction is ", myBall.direction
print "Now I'm going to bounce the ball"
print
myBall.bounce                               #使用一个方法
print "Now the ball's direction is ", myBall.direction

"""
输出结果：
I just created a ball.
My ball is  small
My ball is  red
My ball's direction is  down
Now I'm going to bounce the ball

Now the ball's direction is  down
"""
