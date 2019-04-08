from scrapy.http import HtmlResponse
from scrapy.http import Request


class Md1(object):

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        # crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        print('md1.process_request', request)
        # 请求没交给下载器下载，我们在中间件截获。
        # 下一个Md2的request不进行处理，返回的response就是伪造的。按照md2.response md1.response的顺序返回
        # return HtmlResponse(url="www.xxxx.com", status=200, headers=None, body=b'23dsdasdasdsa')
        # return HtmlResponse(url=request.url, status=200, headers=None, body=b'23dsdasdasdsa')

        # 1.返回Response
        # import requests
        # result = requests.get(request.url)
        # return HtmlResponse(url=request.url, status=200, headers=None,
        #                     body=result.content)

        # 2.返回Request
        # 再返回调度器，一直转圈
        # return Request('https://dig.chouti.com')

        # 3.抛出异常。丢弃请求
        # from scrapy.exceptions import IgnoreRequest
        # raise IgnoreRequest

        # 4.对请求进行加工 加头、加user-agent
        request.headers['user-agent'] = ''



    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        print('md1.process_response', request, response)

        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass


class Md2(object):

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        print('md2.process_request', request)

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        print('md2.process_response', request, response)

        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
