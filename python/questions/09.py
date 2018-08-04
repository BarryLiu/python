"""
【程序9】
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程 找出1000以内的所有完
数。
"""

for i in range(1,1000):

    sums =0
    items = []
    for j in range(1,i):
        if(i%j==0):
            sums+=j
            items.append(j)
        pass
    if(i==sums):
        print("%d 是完数!"%i,"质数是",items)
    pass
