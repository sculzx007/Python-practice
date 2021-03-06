#coding=utf-8

                                                          # 原题
"""
编写一个程序，求 100~999 之间的所有水仙花数。
如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。
"""
                                                          # 个人答案
"""                                                          
j = 0
k = 0
m = 0
i = 100* j + 10* k + m

while 100 <= i <= 999:
    if i == j ** 3 + k ** 3 + m ** 3:
        print i, "是水仙数"
        i += 1
    else:
        i += 1
print
"""

"""
输出结果：没有输出结果
"""

                                                          # 参考答案

for i in range(100, 1000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10)**3    #  这是什么意思？？ sum = sum + （个位数的立方）？
        temp //= 10　　# //是浮点数的除法，等价于 temp = temp // 10
    if sum == i:
        print i,"是水仙数"
