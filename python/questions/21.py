"""
【程序21】
题目：求1+2!+3!+...+20!的和
1.程序分析：此程序只是把累加变成了累乘。
"""

result = 0
num=1

for i in range(1,21):
    num = num * i
    result = result + num
print("result is %d" % result)