"""
【程序25】
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""
i = str(12321)
flag = True
for j in range(0,2):
    if i[j]!=i[4-j]:
        flag = False
        break
print(i,flag,"回文数")