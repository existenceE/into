# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

"""
源码内容
    1、判断当前类中是否有from_crawler
    有 obj = Day96Pipeline.from_crawler(...)
    否： obj = Day96Pipeline()
    2、obj.open_spider()
    3、obj.process_item()obj.process_item()obj.process_item()obj.process_item()obj.process_item()
    4、obj.close_spider()
"""

class FilePipeline(object):

    #规范
    #最先执行
    def __init__(self, path):
        self.f = None
        self.path = path
        print("File.init")


     #最最最先执行
    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化的时候，用于创建pipeline对象
        不实例化就可以调用。类方法。当前类名。
        :param crawler:
        :return:
        """
        print("File.from_crawler")
        path = crawler.settings.get("HREF_FILE_PATH")  #去所有的配置文件（内置、自己写的）里找这个
        return cls(path)

    #2
    def open_spider(self, spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        print("File.open_spider")

        print("爬虫开始啦！")
        self.f = open(self.path, "a+")
     #34567
    def process_item(self, item, spider):
        #item就是yield里面传入的对象，spider就是当前的爬虫对象ChoutiSpider
        # print(spider, item)
        # if spider.name == 'chouti'
        print("File.process_item")
        print("File:", item)

        tpl = "%s\n%s\n\n" %(item['title'], item['href'])
        # print(tpl)
        self.f.write(tpl)
        return item
        # raise DropItem()
        # f = open('news.json', 'a+')
        # f.write(tpl)
        # f.close()
    #1000000
    def close_spider(self, spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        print("File.close_spider")

        print("爬虫结束辣！！！")
        self.f.close()

class DBPipeline(object):

    #规范
    #最先执行
    def __init__(self, path):
        self.f = None
        self.path = path
        print("DB.init")


     #最最最先执行
    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化的时候，用于创建pipeline对象
        不实例化就可以调用。类方法。当前类名。
        :param crawler:
        :return:
        """
        print("DB.from_crawler")
        path = crawler.settings.get("HREF_FILE_PATH")  #去所有的配置文件（内置、自己写的）里找这个
        return cls(path)

    #2
    def open_spider(self, spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        print("DB.open_spider")

        print("爬虫开始啦！")
        self.f = open(self.path, "a+")
     #34567
    def process_item(self, item, spider):
        #item就是yield里面传入的对象，spider就是当前的爬虫对象ChoutiSpider
        # print(spider, item)
        # if spider.name == 'chouti'
        print("DB.process_item")
        print("DB:", item)


        tpl = "%s\n%s\n\n" %(item['title'], item['href'])
        # print(tpl)
        self.f.write(tpl)
        #return item
        # f = open('news.json', 'a+')
        # f.write(tpl)
        # f.close()
    #1000000
    def close_spider(self, spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        print("DB.close_spider")

        print("爬虫结束辣！！！")
        self.f.close()