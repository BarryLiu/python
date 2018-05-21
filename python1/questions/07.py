
"""
【程序7】
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
1.程序分析：利用while语句,条件为输入的字符不为'\n'.
"""

def compate_count(str):
    str_num = 0
    spac_num = 0
    figue_num = 0

    for strs in str:
        if strs.isalpha():
            str_num +=1
        elif strs.isdigit():
            figue_num +=1
        elif strs.isspace():
            spac_num +=1
        else:
            pass
    print('英文字母有：%d' %str_num)
    print('数字有：%d'%figue_num)
    print('空格有：%d'%spac_num)
    # for i in range(str.__len__()):
        # print(str[i:i+1])

    # for i in str:
        # print(i)
    pass


s = "adsfs23344,252_5   2"
compate_count(s)