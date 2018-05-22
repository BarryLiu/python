#  【程序1】
# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一
# 对兔子，假如兔子都不死，问每个月的兔子总数为多少对？
# 1.程序分析： 兔子的规律为数列1,1,2,3,5,8,13,21....

sum=0 # 总兔子数
a = 0
b = 1
month = 0 # 第几个月
input_value = input("要看第几月兔子数:\n")

# 占位符使用
# print("I am %s,age %d" % ('barry', 18,))
# print("i am %(n1)s,age %(n2)d " % {"n1":'barry', "n2": 18})
try:
    end_month = int(input_value)

    # print(sum,a,d,type(input_value))
    while month<end_month:
        a=b
        b=sum
        sum=b+a
        month+=1
        print('第%d个月,兔子%d只!'%(month,sum))
except Exception:
    print("except: 请输入数字")
finally:
    print("finally: 计算结束,兔子总数:",sum)

