"""
题目：利用递归方法求5!。
1.程序分析：递归公式：fn=fn_1*4! ====120
"""
def f(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return (x * f(x-1))
print(f(5))


# ------------

f = 1
for i in range(1,6):
    f = f * i
print(f)