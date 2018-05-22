"""
【程序8】
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，
"""

a = 5
b = 5
result=0
# pow() 次方
c = 0
for i in range(b):
    c = c*10 + a
    result += c
print("结果是:",result)

