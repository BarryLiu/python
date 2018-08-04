#coding=utf-8
import os
import requests,bs4
import logging
import time
from  urllib import parse

'''
下载萤火虫页面下的所以视频文件
http://bbs.huoying666.com/forum-53-1.html
'''
referer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://bbs.huoying666.com'
}
class DownloadHuoYing:

    def __init__(self):
        self.path ='files/yinghuochong'
        self.init_logger()
        self.init_fileroot()

    def init_fileroot(self):
        """创建存储文件目录"""
        if os.path.exists(self.path) == False:
            print('目录不存在')
            os.makedirs(self.path)

    def init_logger(self):
        # 初始化logger
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(self.path+'/test.log') #写入日志文件
        ch = logging.StreamHandler() # 用于输出到控制台
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # 输出格式formatter
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
        self.logger = logger

    def download_video(self,title,vid_url):
        "根据视频url下载视频,title,文件名: [文件名]_[url文件名]"
        file_name = parse.unquote(vid_url.split(r'/')[-1]) # parse.uniquote针对文件路径是中午生成文件名没有urldecode解码修复
        file_local_url = self.path+'/'+title+'_'+file_name
        if os.path.exists(file_local_url):
            self.logger.warning("该请求路径的文件存在,不重新下载.vid_url=【%s】,file_local_url=【%s】"%(vid_url,file_local_url))
            return False
        file = requests.get(vid_url,headers=referer)
        with open(file_local_url, "wb") as code:
            code.write(file.content)
        return True
        pass
    def detail_page(self,url):
        "一条数据内容页面 eg: url='http://bbs.huoying666.com/thread-3979-1-2.html'"
        self.logger.info("进入页面%s"%(url))
        
        
        detail = requests.get(url,headers=referer)
        dtl_a = bs4.BeautifulSoup(detail.text,"html.parser")
        links = dtl_a.select("#postlist .pct  .t_fsz  a ")
        is_download = False
        for link in links:
            link_url = link['href']
            if link_url.endswith('.mp4') or link_url.endswith('.mov') or link_url.endswith('.avi'):
                flag = self.download_video(str(dtl_a.select_one("title").text).split('_')[0],link_url)
                is_download = True
                if flag == None or flag == True:
                    self.logger.warning("页面地址= %s,视频地址 =%s,请求code=%d,"%(url,link_url,detail.status_code))
                    time.sleep(10)# 如果下载成功休息10秒,别下载太频繁了
                    print('休息10秒')

        if is_download == False:
            self.logger.error("%s 页面没有找到视频下载,请求code=%d,找到url路径%r"%(url,detail.status_code,links))
        pass


if __name__=="__main__":
    downer = DownloadHuoYing()
    # url = 'http://bbs.huoying666.com/forum-53-1.html'
    url = 'http://bbs.huoying666.com/forum-53%d.html'
    downer.logger.warning("程序开始下载")
    for i in range(-1,-18,-1):
        page_url = url%i
   
        html = requests.get(page_url,headers=referer)
        soup  = bs4.BeautifulSoup(html.text,"html.parser")
        content = soup.select("#waterfall1 > li > div > a")
        downer.logger.warning("页面开始下载视频 page=%s"%page_url)
        # downer.detail_page('http://bbs.huoying666.com/thread-14-1-1.html')
        for link in content:
            detail_url="http://bbs.huoying666.com/%s"%link['href']
            try: 
                downer.detail_page(detail_url)
                print("url:",link['href'])
            except Exception as e:
                downer.logger.error("程序下载出错!!",detail_url,e)
        downer.logger.warning("页面下载视频结束 page=%s"%page_url)
    downer.logger.warning("程序下载结束")