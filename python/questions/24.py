"""
【程序24】
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
"""
def rever_num(num):#递归输出
    if num==num_len-1:
        print(input_number[num],end='')
    else:
        rever_num(num+1)
        print(input_number[num],end='')
input_number=input('请输出数字:')
num_len=len(input_number)
print('该数字有%d 位' %num_len)
rever_num(0)