import redis

from scrapy.dupefilters import BaseDupeFilter
from scrapy.utils.request import request_fingerprint

from scrapy_redis import defaults
from scrapy_redis.connection import get_redis_from_settings

from scrapy_redis.dupefilter import RFPDupeFilter


class DupeFulter(BaseDupeFilter):

    def __init__(self):
        # self.visited_url = set()
        self.conn = redis.Redis(host='127.0.0.1', port=6379, password="")

    def request_seen(self, request):
        fd = request_fingerprint(request)
        result = self.conn.sadd("visited_urls", fd)
        if result == 1:
            return False
        return True

        # if request.url in self.visited_url:
        #     return True
        # self.visited_url.add(request.url)
        # return False


class RedisDupeFilter(RFPDupeFilter):
    @classmethod
    def from_settings(cls, settings):
        """Returns an instance from given settings.

        This uses by default the key ``dupefilter:<timestamp>``. When using the
        ``scrapy_redis.scheduler.Scheduler`` class, this method is not used as
        it needs to pass the spider name in the key.

        Parameters
        ----------
        settings : scrapy.settings.Settings

        Returns
        -------
        RFPDupeFilter
            A RFPDupeFilter instance.


        """
        server = get_redis_from_settings(settings)
        # XXX: This creates one-time key. needed to support to use this
        # class as standalone dupefilter with scrapy's default scheduler
        # if scrapy passes spider on open() method this wouldn't be needed
        # TODO: Use SCRAPY_JOB env as default and fallback to timestamp.
        key = defaults.DUPEFILTER_KEY % {'timestamp': "xiaodongbei"}
        debug = settings.getbool('DUPEFILTER_DEBUG')
        return cls(server, key=key, debug=debug)
