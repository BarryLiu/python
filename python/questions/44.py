"""
【程序44】
题目：一个偶数总能表示为两个素数之和。
"""

#不理解
import math  #验证1000以内大于2的偶数是两个素数之和
def prime_number(n):  #获取素数
    a=[p for p in range(2,n) if 0 not in [p%d for d in range (2,int(math.sqrt(p))+1)]]#列表推导式
    return a
a=prime_number(1000)

print(a)
