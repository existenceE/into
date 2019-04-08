# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://chouti.com/']

    def parse(self, response):
        print(response)
        page_list = response.xpath('//div[@id="dig_lcpage"]//a/@href').extract()
        for page in page_list:
            page = "https://dig.chouti.com" + page
            yield Request(url=page, callback=self.parse)
