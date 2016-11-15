# coding=utf-8

# continue的使用——跳过这一循环，直接进行下一循环

for i in range (1, 6):
    print                     # 为何会多出一个print？
    print "i = ", i,         # i 后面的逗号表示print后不换行
    print "Hello, How"
    if i == 3:
        continue
    print "are you today?"

""" 输出结果
i =  1 Hello, How
are you today?

i =  2 Hello, How
are you today?

i =  3 Hello, How

i =  4 Hello, How
are you today?

i =  5 Hello, How
are you today?
"""
    
    
