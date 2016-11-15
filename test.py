#coding=utf-8

# 第一个
"""
i = 10
while i:
    print("I love you")
    i = i +1
"""

"""
输出结果：无限输出 I love you
"""

# 第二个

while true:
    while true:
        break
        print 1
    print 2
    break
print 3

"""
输出结果：输出错误！
                   true没有定义
"""
