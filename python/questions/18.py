"""
【程序18】
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向

队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

1.程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除， 则表明此数不是素数，反

之是素数。
"""

print("沙发发发发啊")

team = ('x','y','z')

print("-------------case1-这里有问题--------------")
for i in range(3):
    for j in range(3):
        for k in range(3):
            a = team[i]
            b = team[j]
            c = team[k]
            if(a != b and b !=c and c != a )and ('x'!=a and 'x' != c and 'y' !=c):
                print('a vs',a)
                print('b vs',b)
                print('c vs',c)
                pass


print("-------------case2---------------")

for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print('order is a -- %s' % (chr(i)))
                        print('order is b -- %s' % (chr(j)))
                        print('order is c -- %s' % (chr(k)))