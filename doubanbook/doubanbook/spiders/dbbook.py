# -*- coding: utf-8 -*-
import scrapy
import re
#from items import DoubanbookItem
from doubanbook.items import DoubanbookItem
class DbbookSpider(scrapy.Spider):
    name = "dbbook"
    #allowed_domains = ["https://www.douban.com/doulist/1264675/"]
    start_urls = ['https://www.douban.com/doulist/1264675/']

    def parse(self, response):
        #print(str(response.body,encoding="utf8"))
        item= DoubanbookItem()
        selector=scrapy.Selector(response)
        books=selector.xpath('//div[@class="bd doulist-subject"]')
        for x in books:
            title = x.xpath('div[@class="title"]/a/text()').extract()[0]
            rate = x.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()').extract()[0]
            author = re.search('<div class="abstract">(.*?)<br', x.extract(), re.S).group(1)
            title = title.replace(' ', '').replace('\n', '')
            author = author.replace(' ', '').replace('\n', '')
            item["title"] = title
            item["rate"] = rate
            item["author"] = author

            # print('标题:' + title)
            # print('评分:' + rate)
            # print(author)
            # print('-----------------------------------------')
            yield item
            nextpage=selector.xpath('//span[@class="next"]/link/@href').extract()
            if nextpage:
                next=nextpage[0]
                print(next)
                yield scrapy.http.Request(next, callback=self.parse)