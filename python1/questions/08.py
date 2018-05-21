"""
【程序8】
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，
"""

a = 2

result=a
# pow() 次方
for i in range(5):
    a = a*10
    result = result + a
print("结果是:",result)

