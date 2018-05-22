"""
【程序6】
题目：输入两个正整数m和n，求其最大公约数和最小公倍数。
1.程序分析：利用辗除法。
"""
m = 20
n = 50

a = m
while True:
    if int(m%a)==0 and int(n%a)==0 :
        print("最小公倍数是",a)
        break
    a -=1

b = m*n
for i in range(1,b):
    if int(i%m)==0 and int(i%n)==0:
        print('最大公约数是:',i)
        break




