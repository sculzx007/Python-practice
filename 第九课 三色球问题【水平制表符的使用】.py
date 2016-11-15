# coding=utf-8

"""
                                                            题目
有红、黄、蓝三种颜色的求，其中红球 3 个，黄球 3 个，绿球 6 个。先将这
12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种
颜色搭配。
"""
                                                            #题目

print "red\tyellow\tblue"    #使用 \t 目的应该为将结果按照红黄绿竖排                          
for red in range (0, 4):
    for yellow in range (0, 4):
        for green in range (2, 7):      #范围是2-7的原因是绿球必定有一个，
                                                  #否则红球加黄球的个数只有7个
            if red + yellow + green == 8:
                print red, "\t", yellow, "\t", green   #

"""
学习：

\r :回车符

\n :换行符

\t :水平制表符

\v :垂直制表符

\f :换页符

"""

"""
输出结果：
red	yellow	blue
0 	2 	6
0 	3 	5
1 	1 	6
1 	2 	5
1 	3 	4
2 	0 	6
2 	1 	5
2 	2 	4
2 	3 	3
3 	0 	5
3 	1 	4
3 	2 	3
3 	3 	2
"""
        
