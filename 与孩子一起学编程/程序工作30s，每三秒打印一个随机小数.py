                                                         #个人答案
"""
import random, time
number = random.random()
second = time.sleep(3)
time = 30
while 0 <= time <=30:
    print number
    time = time - 3
print "Ending"
"""

"""
输出结果:
0.989621555003
0.989621555003
0.989621555003
0.989621555003
0.989621555003
0.989621555003
0.989621555003
0.989621555003
0.989621555003
0.989621555003
0.989621555003
Ending
"""

                                                         #参考答案
import random, time
for i in range(10):
    print random.random()
    time.sleep(3)
