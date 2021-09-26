import scrapy
from scrapy3.items import Scrapy3Item

class Douban250Spider(scrapy.Spider):
    name = 'douban250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
      print('--join--')
      mv_list = response.xpath("/html[@class='ua-windows ua-webkit']/body/div[@id='wrapper']/div[@id='content']/div[@class='grid-16-8 clearfix']/div[@class='article']/ol[@class='grid_view']/li");
      print('mv_list:',len(mv_list));
      for mv in mv_list:
        item = Scrapy3Item()
        item['serial_number'] = mv.xpath(".//div[@class='item']/div[@class='pic']/em/text()").extract_first();
        item['movie_name'] = mv.xpath(".//div[@class='item']/div[@class='info']/div[@class='hd']/a/span[@class='title'][1]/text()").extract_first();
        item['star'] = mv.xpath(".//div[@class='item']/div[@class='info']/div[@class='bd']/div/span[@class='rating_num']/text()").extract_first();
        item['evaluate'] = mv.xpath(".//div[@class='item']/div[@class='info']/div[@class='bd']/div/span[2]/text()").extract_first();
        item['describe'] = mv.xpath(".//div[@class='item']/div[@class='info']/div[@class='hd']/a/span[@class='title'][1]/text()").extract_first();
        content = mv.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract_first()
        for i_content in content:
          content_s = "".join(i_content.split())
          item['introduce'] = content_s
        yield item
      next_link = response.xpath("//span[@class='next']/link/@href").extract()
      if next_link:
        next = next_link[0]
        yield scrapy.Request('https://movie.douban.com/top250/'+next,callback=self.parse)
      pass
