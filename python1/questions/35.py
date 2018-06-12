"""
【程序35】
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
"""

arr = [54,22,1,55,9,2]
# print(max(arr))
# print(min(arr))
# print(arr.index(2))
max_val = max(arr)
min_val = min(arr)
arr.remove(max_val)
arr.remove(min_val)

arr.insert(0,max_val)
arr.insert(len(arr),min_val)
print(arr)