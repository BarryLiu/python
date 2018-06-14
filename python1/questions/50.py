"""
【程序50】
题目：有五个学生，每个学生有3门课的成绩，从键盘输入以上数据（包括学生号，姓名，三门课成绩），计算

出平均成绩，况原有的数据和计算出的平均分数存放在磁盘文件"stud"中。
"""

import os
stus = [{"name":"tom","java":80,"php":55,"python":40},
        {"name":"tom","java":80,"php":55,"python":40},
        {"name":"tom","java":80,"php":55,"python":40}]

f = open("stud.txt","w")
f.write(str(stus))
f.close()
print("success!")