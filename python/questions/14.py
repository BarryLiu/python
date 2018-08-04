"""
【程序14】
题目：输入某年某月某日，判断这一天是这一年的第几天？
1.程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且

输入月份大于3时需考虑多加一天。
"""
import math

year_val = input("请输入年份:\n")
month_val = input("请输入月份:\n")
day_val = input("请输入日期:\n")
result = 0
try:
    year = int(year_val)
    month = int(month_val)
    day = int(day_val)
    result = day # 先给多出来的天数加了

    month_day = [31,0,31,30,31,30,31,31,30,31,30,31]
    for i in range(1,month):
        value = month_day[i-1]
        if i == 2 and month >2 :
            # 需要计算其是否瑞年
            if year%4==0 and year %100==0 or year%400==0:
                value = 29
            else :
                value = 28
        result += value
        pass
except:
    print("except: 程序出错")
finally:
    print("success! 从年初到现在一共的天数: result = ",result)