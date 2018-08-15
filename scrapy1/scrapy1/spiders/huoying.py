# -*- coding: utf-8 -*-
from urllib import parse
from bs4 import BeautifulSoup

import scrapy
from scrapy import Selector

from scrapy1.items import VideoItem


class HuoyingSpider(scrapy.Spider):
    name = 'huoying'
    allowed_domains = ['bbs.huoying666.com']

    def start_requests(self):
        print('start_request')
        home_url='http://bbs.huoying666.com/forum-53-3.html'
        yield scrapy.http.Request(url=home_url,callback=self.parse_url)

    def parse_url(self,response):
        print("---------parse_url start ---------")
        try:
            sel =  Selector(response)
            print('response=',response,'\n\n\n')
            print('sel=',sel,'\n\n\n')
            html = BeautifulSoup(response.body,"html.parser");
            content = html.select('#waterfall1 > li > div > a')

            for link in content:
                detail_url="http://bbs.huoying666.com/%s"%link['href']
                try:
                    yield scrapy.http.Request(url=detail_url,callback=self.parse)
                except Exception as e:
                    print("程序下载出错!!",detail_url,e)
        except Exception as e:
            print("出错了",e)
        print("---------parse_url end ---------")
        pass
    def parse(self, response):
        print("---------parse start ---------")
        detail_html = BeautifulSoup(response.body,"html.parser")
        links = detail_html.select('#postlist .pct  .t_fsz  a ')
        for link in links:
            link_url = link['href']
            if link_url.endswith('.mp4') or link_url.endswith('.mov') or link_url.endswith('.avi'):
                file_name = parse.unquote(link_url.split(r'/')[-1]) # parse.uniquote针对文件路径是中午生成文件名没有urldecode解码修复
                title = str(detail_html.select_one("title").text).split('_')[0] # title 最好拿到页面的标题
                local_url = title+'_'+file_name

                item = VideoItem()
                item['name'] = file_name
                item['link_url'] = link_url
                item['local_url'] = local_url
                print('item: ',item)
                yield item
        print("---------parse end ---------")
