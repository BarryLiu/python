#coding:utf-8

# 有几个文件想按一定规则重命名,
import os
import re
path = os.getcwd()
path = path +'\img\\'
path = 'D:\gitSpace\LessOrMore\_posts\\'
print("path:",path)
def rename(path):
    filelist = os.listdir(path)
    for files in filelist:
        file_url=os.path.join(path,files);
        if os.path.isdir(file_url):
            pass
        new_url=path+'2018-05-01-'+file_url.split('\\')[-1]
        # patten = "[0-9]";
        # 是不是 201*** 开头如果是就返回
        if(file_url.split('\\')[-1].startswith('201')):
            pass
        print(file_url,'-------',new_url)
        os.rename(file_url,new_url)



# def settitle(file_path):
#     file = open(file_path,'w+')
#     content = file.readlines();
#     # print(content)
#     file.write("<***>1")
#     file.write("<***>2")
#     file.writelines(content)
#
#     # file.closed
#     file.flush()
#     # print(file.read())
#     file.close()
#     print(file)

rename(path);


# settitle('D:\gitSpace\_posts\2018-05-01-note9.md')
# settitle('test.txt')

