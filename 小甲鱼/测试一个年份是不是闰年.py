# coding=utf-8
"""                                                  #个人方案
year = int (raw_input ("请输入一个年份: "))
if (year % 4 == 0) and (year % 100 != 0):
    print (year, "是闰年")
elif (year % 400 == 0):
    print (year, "是闰年")
else:
    print (year, "不是闰年")
"""

#  输出结果中“不是闰年”或“是闰年”处为乱码
"""
                                                      #参考答案
temp = raw_input("请输入一个你年份: ")
while not temp.isdigit():  # isdigit 是指确保temp中全是数字
    temp = input ("抱歉，您的输入有误，请输入一个整数：")
year = int (temp)
if year/400 == int (year/400):   #这个为确认year/4后得到的是整数，不是浮点数，即year能被400整除
                                              # 等价于 year%400 == 0
    print (temp + "是闰年")
else:
    if (year/4 == int (year/4)) and (year/100 != int(year/100)):
        print (temp + "是闰年")
    else:
        print (temp + "不是闰年")

"""
                                                     #个人修改
year = int (raw_input ("请输入一个年份: "))
if (year % 400 == 0):
    print year, "是闰年"
else:
    if (year % 4 == 0) and (year % 100 != 0):
        print year, "是闰年"
    else:
        print year, "不是闰年"
        
#  输出结果正确
# Python 2.0版本中，print后面不要加（），否则括号内的汉子输出为乱码
