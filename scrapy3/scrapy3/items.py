# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy3Item(scrapy.Item):
    # define the fields for your item here like:
	# 序号
    serial_number = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
	# 介绍
    introduce = scrapy.Field()
	# 星级
    star = scrapy.Field()
	# 评论数
    evaluate = scrapy.Field()
	# 描述
    describe = scrapy.Field()
    pass
