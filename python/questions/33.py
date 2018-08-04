"""
【程序33】
题目：打印出杨辉三角形（要求打印出10行如下图）
1.程序分析：
        1
       1 1
     1 2 1
    1 3 3 1
   1 4 6 4 1
1 5 10 10 5 1
"""
#初始化三角
a = []
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)
#计算杨辉三角
for i in range(10):
    a[i][0] = 1
    a[i][i] = 1
for i in range(2,10):
    for j in range(1,i):
        a[i][j] = a[i-1][j-1] + a[i-1][j]
 #输出三角
for i in range(10):
     for j in range(i+1):
         print (a[i][j],end=",")
     print()
