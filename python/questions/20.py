"""
【程序20】
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
1.程序分析：请抓住分子与分母的变化规律。
"""

child = 2
parent = 1
temp = 0
result = 0
for i in range(0,20):
    temp = child+parent
    a = temp / child
    child = temp
    result = result+a

print("最后20项总和是:",result)