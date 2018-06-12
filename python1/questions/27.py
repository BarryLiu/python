"""
【程序27】
题目：求100之内的素数
"""
for i in range(100):
    flag = True
    for j in range(2,i):
        if i%j==0:
            flag = False
            break
    if flag:
        print("%d 是素数"%i)
