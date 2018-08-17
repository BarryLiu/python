# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JokejiItem(scrapy.Item):
    """笑话集数据item"""
    #标题
    title = scrapy.Field()
    #内容
    content = scrapy.Field()
    #发布时间
    publish_date = scrapy.Field()
    #浏览次数
    browse = scrapy.Field()
    #赞数量
    favour = scrapy.Field()
    #类型
    type = scrapy.Field()
    pass
