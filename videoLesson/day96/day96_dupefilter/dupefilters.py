


from scrapy.dupefilters import BaseDupeFilter
from scrapy.utils.request import request_fingerprint
from scrapy.http import Request



# url1 = "http://www.baidu.com?k1=123&k2=456"
# url2 = "http://www.baidu.com?k2=456&k1=123"
#
# req1 = Request(url=url1)
# req2 = Request(url=url2)
#
# fd1 = request_fingerprint(request=req1)
# fd2 = request_fingerprint(request=req2)


class mxnDupeFulter(BaseDupeFilter):

    def __init__(self):
        self.visited_url = set()


    @classmethod
    def from_settings(cls, settings):
        return cls()

    def request_seen(self, request):
        fd = request_fingerprint(request=request)
        if fd in self.visited_url:
            return True
        self.visited_url.add(fd)

    def open(self):  # can return deferred
        print("dupe开始")
        pass

    def close(self, reason):  # can return a deferred
        print("dupe结束")
        pass

    def log(self, request, spider):  # log that a request has been filtered
        print("日志")
        pass













