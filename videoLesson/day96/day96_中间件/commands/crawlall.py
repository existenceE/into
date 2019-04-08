from scrapy.commands import ScrapyCommand




class Command(ScrapyCommand):

    requires_project = True

    def syntax(self):
        return '[options]'


    def short_desc(self):
        return "Runs all of the spiders"

    #只要一执行crawlall就会执行run方法
    def run(self, args, opts):
        #找到所有的爬虫
        spider_list = self.crawler_process.spiders.list()
        print(spider_list)
        #循环这几个爬虫 添加两个爬虫的任务
        for name in spider_list:
            self.crawler_process.crawl(name, **opts.__dict__)
        #开始爬
        self.crawler_process.start()
