# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from ..items import ChoutiItem
from scrapy.http.cookies import CookieJar

from scrapy.http import HtmlResponse


# 去response里把cookie解析出来


# 实现功能
# 1、将标题和连接写入news.log中
# 2、递归反复爬取页面

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://www.baidu.com/']
    cookie_dict = {}

    def parse(self, response):

        """
        第一次访问抽屉返回的内容:response
        :param response:
        :return:
        """
        print(response)