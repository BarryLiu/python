"""
【程序10】
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在 第10次落地时，共经过多
少米？第10次反弹多高？
"""
start = 100
sums = 0
for i in range(10):
    sums+=start
    start=int(start/2)
    pass

print("共经过%d米,第10次反弹%d米。"%(sums,start))
