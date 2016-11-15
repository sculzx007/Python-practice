# coding=utf-8

"""建立一个程序，用户必须输入密码才能使用这个程序"""


code = 85412613
c = int (raw_input ("Please input code(six numbers): "))
if c == code:
    age = float (raw_input ("Enter your age: "))
    grade = float (raw_input ("Enter your grade: "))
    if age >= 8 and grade >=3:   #用 and 结合多个条件
        print "You can play this game!"
    else:
        print "Sorry, you can't play the game"
else:
    print "Your code is not correct!"

