# coding=utf-8
"""方法1：使用普通的语句来实现对年龄和年级的同时限定

age = float (raw_input ("Enter your age: "))
grade = float (raw_input ("Enter your grade: "))
if age >=8:
    if grade >=3:
        print "You can play this game"  #双重条件进行限定，表示只有当两个if都成立时才会输出
    else:
        print "Sorry, you grade is too low!"
else:
    print "Sorry, you can't play the game"

#  整个程序中，实际上只有4个语句
"""

# 方法2：使用and语句来实现对年龄和年级的同时限定

age = float (raw_input ("Enter your age: "))
grade = float (raw_input ("Enter your grade: "))
if age >= 8 and grade >=3:   #用 and 结合多个条件
    print "You can play this game!"
else:
    print "Sorry, you can't play the game"

""" and 可以连接很多个条件，这个与C语言有区别"""
