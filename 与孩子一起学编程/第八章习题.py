# coding=utf-8

                                        #第一题 

# table = int (raw_input ("which multiplication table would you like?\n"))
# print "Here's your table:"
# for i in range (1,11):   #设定一个范围
#     j = table * i        #定义一个变量，让它等于输入的数字和i的乘积
#     print  table, "x", i, " = ", j

                                        #第二题

# 不会……

                                         #第三题
    
table = int (raw_input ("which multiplication table would you like?\n"))
max = int (raw_input ("How high do you want to go?\n"))
print "Here's your table:"
for i in range (1, max+1):     #max + 1 表示从1一直乘到输入的数字max（因为range默认取的数值是上限减1）
    j = table * i
    print  table, "x", i, " = ", j
