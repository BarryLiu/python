
import requests
from bs4 import BeautifulSoup
import you_get
import argparse

"""
    you-get 库搭配request+bs4爬取youtube上面的一个人的所有视频
    (没写完,不想写啦)
"""


class YoutobeDownload:
    def __init__(self):
        self.start_url = 'https://www.youtube.com/channel/UCdwAosJ8p9jsuZ5D9zRjEHQ'




if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help=('要爬取的人的url.eg:https://www.youtube.com/channel/UCdwAosJ8p9jsuZ5D9zRjEHQ'),default='https://www.youtube.com/channel/UCdwAosJ8p9jsuZ5D9zRjEHQ')
    args = parser.parse_args()
    url = args.url
    # filename= args.filename
    print('开始下载',url)
    try:
        downloader = YoutobeDownload()

    except Exception as e:
        print('下载出错',e)

