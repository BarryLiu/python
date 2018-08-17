# -*- coding: utf-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup

from scrapy2.items import JokejiItem

Picreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://www.jokeji.cn'
}
home_url = 'http://www.jokeji.cn'

class JokejiSpider(scrapy.Spider):
    name = 'jokeji'
    allowed_domains = ['www.jokeji.cn']

    #start_urls = ['http://www.jokeji.cn/']
    def start_requests(self):
        url='http://www.jokeji.cn/list23_1.htm'
        list_page = requests.get(url=url,headers=Picreferer)
        bs_page = BeautifulSoup(list_page.content,'html.parser')
        items = bs_page.select('.list_title li ')
        for item in items:
            link = home_url+item.select_one('a ')['href']
            browse = item.select_one('i')
            try:
                yield scrapy.http.request(url=link,callback=self.parse)
            except Exception as e:
                print("程序下载出错!!",link,browse,e)
        pass


    def parse(self, response):

        detail = BeautifulSoup(response.body,'html.parser')
        content = detail.select('.left_up ul')
        title = detail.select_one('title').get_text

        item = JokejiItem()
        item.title = title
        yield item
        pass
