"""
【程序30】
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
1. 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，
依次后移一个位置。
"""

new_num = 22
a = [1,4,6,9,13,16,19,28,40,100]
print(a)# old
a.append(new_num)
print(a)# append
a.sort();
print(a)# sort
b = a[0:len(a)-1]
print(b)# 新数据


