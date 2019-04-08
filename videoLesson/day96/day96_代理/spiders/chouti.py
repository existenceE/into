# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from ..items import ChoutiItem
from scrapy.http.cookies import CookieJar


# 去response里把cookie解析出来


# 实现功能
# 1、将标题和连接写入news.log中
# 2、递归反复爬取页面

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://dig.chouti.com/']
    cookie_dict = {}


    def start_requests(self):
        #方式一
        # import os
        # os.environ['HTTPS_PROXY']= "http://root:woshiniba@192.168.11.11:9999/"
        # os.environ['HTTP_PROXY'] = "192.168.11.11",
        #方式二
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)
            # yield Request(url=url, callback=self.parse, meta={'proxy': "http://root:woshiniba@192.168.11.11:9999/"})
            #没有meta depth为空

    def parse(self, response):

        """
        第一次访问抽屉返回的内容:response
        :param response:
        :return:
        """
        from scrapy.http import Response
        #response.request其实就是上面start_requests里的返回结果
        #response.meta -》 response.request.meta
        from scrapy.spidermiddlewares.depth import DepthMiddleware
        print(response.meta.get('depth'))
        page_list = response.xpath('//div[@id="dig_lcpage"]//a/@href').extract()
        for page in page_list:
            page = "https://dig.chouti.com" + page
            yield Request(url=page, callback=self.parse, dont_filter=False, )