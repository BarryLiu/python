#coding=utf-8
import os

import requests
import argparse
from bs4 import BeautifulSoup


class BqgBookDownload(object):
    """
    爬取https://m.bqg5200.com网站下的小说,这个网站挺简单的没有做防爬机制,
    脚本使用 直接python 运行就可以,指定 参数-u为爬取指定小说的章节,如果中途到哪章节中断了直接-u 加中断的那节url继续向后面爬取
    """
    def __init__(self,name,host_url,start_url):
        self.host_url=host_url
        self.curr_url= start_url
        self.num=0
        self.file= open(name,'wb')
        self.header = referer = {
            'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
            'Referer':'https://m.bqg5200.com'
        }
        # if os.path.exists(name):

    def parse(self):

        if len(self.curr_url.split('-'))<3: # url/wapbook-小说id-章节id,  如果拆分小于3说明最后一章了
            return
        url = self.host_url+self.curr_url
        # url = 'http://www.baidu.com'
        html = requests.session().get(url=url,headers=self.header,verify=False)
        b_html = BeautifulSoup(html.content,'html.parser')
        title = b_html.select_one('#nr_title').text
        content = b_html.select_one('#nr1').text

        print('当前爬取【%s】,路径【%s】'%(title,url))
        self.file.writelines('')
        self.file.writelines('')
        self.file.write(title.encode())
        self.file.write(content.encode())

        self.curr_url=b_html.select_one('#pb_next')['href']
        self.num=self.num+1
        if(self.num%10==0):
            self.file.flush()
        # 继续递归
        self.parse()
        pass

    def download(self):

        self.parse();
        self.file.flush()
        self.file.close()
        pass


# 运行程序
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help=('要爬取章节的第一章url.eg:https://m.bqg5200.com/wapbook-2893-1637168/'),default='https://m.bqg5200.com/wapbook-2893-1637168/')
    parser.add_argument('-f', '--filename', help=('小说名称,eg:九星霸体诀'),default='九星霸体诀')
    args = parser.parse_args()
    url = args.url
    filename= args.filename

    print('开始下载',url,filename)
    try:
        # downloader = BqgBookDownload('abcd.txt','https://m.bqg5200.com','/wapbook-2893-1637168')
        downloader = BqgBookDownload(filename+'.txt',url[:21],url[21:]) # 除去域名是21个下标
        downloader.download()
        print('下载完成',url,filename)
    except Exception as e:
        print('下载出错',e)
        downloader.file.flush()
        downloader.file.close()
    print('run succ')
