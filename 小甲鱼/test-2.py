# coding=utf-8
number = int (raw_input ("请输入一个整数: "))
while number:
    i = number - 1
    while i:
        print (" ")
        i = i - 1
    j = number
    while j:
        print ("*")
        j = j - 1
    print
    number = number -1


"""输出结果：根据输入的数字，排列出*号，例如，输入：3
    则结果为：
*
*
*

 
*
*

*

"""
