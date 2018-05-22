# encoding = utf-8
"""
【程序5】
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下

的用C表示。
1.程序分析：(a>b)?a:b这是条件运算符的基本例子。
"""

score = 76
result = ''
if score>= 90:
    result = 'A'
elif score>=60:
    result = "B"
else:
    result ="C"
print("if else 写法 %d分数是%s等级"%(score,result))

print("三元运算符写法: ","A"if score>=90 else "B" if score >=60 else "C")



