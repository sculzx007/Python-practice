"""
import time
print "1"
time.sleep(2)                #sleep()函数可以用来增加一个延时
print "2"
time.sleep(2)
print "3"
time.sleep(2)

"""

# 该程序等价于以下代码
from time import sleep
print "Hello",
sleep(4)
print "world!"
