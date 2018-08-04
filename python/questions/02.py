# coding=utf-8



"""
 【程序2】
    题目：判断101-200之间有多少个素数，并输出所有素数。
    1.程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，
    则表明此数不是素数，反之是素数。
"""
import sys
print(sys.getdefaultencoding())
for i in range(101,200):
    # print(i)
    flag = True # 默认是素数
    for j in range(2,i):
        # print(i,j)
        if i%j==0:
            flag = False
            break
    if flag:
        print("%d是素数"%i)

print("计算完成！")





#====================================================
def is_even(input_value):
    try:
        num = int(input_value)
        if(num%2==0):
            print("%d是偶数"%num)
        else:
            print("%d不是偶数"%num)

    except Exception:
        print("except:","请输入数字")
    finally:
        print("finally:","计算结束")


# input_value = input("请输入一个数判断是不是偶数:\n")
# is_even(input_value)


