"""
【程序13】
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
1.程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后的结果满足
如下条件，即是结果。请看具体分析：
"""

# ----------算法1(有错)---------
# for i in range(1,1000):
#     for j in range(10,100):
#         for k in range(13,100):
#             if(i+100==j*j and i+168== k*k):
#                 print(i)
#                 break;
#                 pass

# https://blog.csdn.net/yueqinglkong/article/details/22805293
print("------算法2---------------")
import math
for i in range(10000):
    a = math.sqrt(i+100)
    b = math.sqrt(i+268)
    if( a == int(a) and  b == int(b) ):
        print("%(i)d是完全平方数,a=%(a)d,b=%(b)d"%{"i":i,"a":a,"b":b})
        pass

print("---------算法3------------")
import math
for i in range(11,83):
    a =  math.pow(i,2)-100
    b =  math.sqrt(a + 100 + 168);
    if b == int(b):
        print("%(i)d是完全平方数,a=%(a)d,b=%(b)d"%{"i":i,"a":a,"b":b})
        pass
