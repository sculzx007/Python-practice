#coding=utf-8

# 交换三个值
#题目：快速交换x, y, z的值
#  x, y, z = ,1 2, 3

                                  #个人答案
"""
x = 1
y = 2
z = 3
t = x
x = y
y = z
z = t
print x
print y
print z
"""


                                  #参考答案
x = 1
y = 2
z = 3
x, y, z = z, x, y
print x
print y
print z

"""
输出结果：
3
1
2

目的：学会使用三个数直接的快速交换
"""
