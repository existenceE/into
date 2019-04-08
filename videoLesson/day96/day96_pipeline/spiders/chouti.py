# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from ..items import ChoutiItem

# 实现功能
# 1、将标题和连接写入news.log中
# 2、递归反复爬取页面

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://dig.chouti.com/']

    def parse(self, response):
        item_list = response.xpath('//div[@id="content-list"]/div[@class="item"]')
        # f = open("news.log", mode="a+")
        for item in item_list:
            text = item.xpath('.//a/text()').extract_first().strip()
            href = item.xpath('.//a/@href').extract_first()
            # print(type(href), type(text.strip()))
            # print(href, text.strip())
            yield ChoutiItem(title=text, href=href) #立即去执行pipelines力的process_item方法
        #     f.write(href+'\n'+text.strip())
        # f.close()

        page_list = response.xpath('//div[@id="dig_lcpage"]/a/@href').extract()
        for page in page_list:
            page = "https://dig.chouti.com" + page
            yield Request(url=page, callback=self.parse)
