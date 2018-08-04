"""
【程序38】
题目：写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
"""
def strlen(val):
    return len(val)

if __name__ == "__main__":
    print("main函数")
    a = input("input a String")
    print("length:",strlen(a))

