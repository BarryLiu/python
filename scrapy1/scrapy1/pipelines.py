# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os

import requests

class Scrapy1Pipeline(object):
    def process_item(self, item, spider):
        return item


class TencentJsonPipeline(object):

    def __init__(self):
        self.name = 'tencent'
        self.file = open('tencent.json', 'wb')

    def process_item(self, item, spider):
        if spider.name != self.name:
            return item
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        print("item=",item)
        print("content=",content,type(content))
        self.file.write(content)
        return item

    def close_spider(self, spider):
        self.file.close()


class HuoyingVideoPipeline(object):

    def __init__(self):
        self.name='huoying'
        self.path ='files/yinghuochong'
        self.referer= {
            'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
            'Referer':'http://bbs.huoying666.com'
        }
        self.init_fileroot()
    def init_fileroot(self):
        """创建存储文件目录"""
        if os.path.exists(self.path) == False:
            print('目录不存在')
            os.makedirs(self.path)
    def process_item(self, item, spider):
        if spider.name != self.name or item == None:
            return item
        local_url = item['local_url']
        link_url = item['link_url']
        print("进入下载通道: item=",item)
        if os.path.exists(local_url):
            print("该请求路径的文件存在,不重新下载.vid_url=【%s】,file_local_url=【%s】"%(link_url,local_url))
            return item
        # file = requests.get(link_url,headers= self.referer)
        # with open(self.path+'/'+local_url, "wb") as code:
        #     code.write(file.content)
        print('---------下载成功!!!------\n\n\n\n')
        return item

    def open_spider(self,spider):
        print("打开爬虫了")

    def close_spider(self,spider):
        print("关闭爬虫")