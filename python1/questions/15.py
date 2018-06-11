"""
【程序15】
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
1.程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y
的值进行交换，然后再用
与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
"""

x_val = input("请输入x: ")
y_val = input("请输入y: ")
z_val = input("请输入z: ")

try:
    x = int(x_val)
    y = int(y_val)
    z = int(z_val)

    # list 排序
    a = [x,y,z]
    print(sorted(a))

    #
except Exception as err:
    print("except! fail",err,type(err), isinstance(err,ValueError),isinstance(err,BaseException),isinstance(err,AttributeError))
finally:
    pass
