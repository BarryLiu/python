"""
【程序19】
题目：打印出如下图案（菱形）
    *
   ***
 ******
********
 ******
  ***
   *
1.程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重 for循环，第一层控制

行，第二层控制列。
"""

# 打印输入5行
# num = 5
#
# for i in range(1,5):
#     for j in  range(num-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()
# for i in range(num-1):
#
#     pass

s = '*'
for i in range(1,8,2):
    t = (7-i)//2
    print(' '*t + s*i + ' '*t)
for i in reversed(range(1,6,2)):
    t = (7-i)//2
    print(' '*t + s*i + ' '*t)