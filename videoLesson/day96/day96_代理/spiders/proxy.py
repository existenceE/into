import base64
from six.moves.urllib.parse import unquote, urlunparse
try:
    from urllib2 import _parse_proxy
except ImportError:
    from urllib.request import _parse_proxy
from scrapy.utils.python import to_bytes
import random
class mxnProxyMiddleware(object):
    def _basic_auth_header(self, username, password):
        user_pass = to_bytes(
            '%s:%s' % (unquote(username), unquote(password)),
            encoding='latin-1')
        return base64.b64encode(user_pass)

    def process_request(self, request, spider):
        PROXIES=[
            {'ip_port': '111.11.228.75:80', 'user_pass': ''},
            {'ip_port': '111.11.228.75:80', 'user_pass': ''},
            {'ip_port': '111.11.228.75:80', 'user_pass': ''},
            {'ip_port': '111.11.228.75:80', 'user_pass': ''},
            {'ip_port': '111.11.228.75:80', 'user_pass': ''},
        ]
        url = random.choice(PROXIES)


        #url = "http://root:woshiniba@192.168.11.11:9999/"
        orig_type=""

        # from httpproxy._get_proxy
        proxy_type, user, password, hostport = _parse_proxy(url)
        proxy_url = urlunparse((proxy_type or orig_type, hostport, '', '', '', ''))

        if user:
            creds = self._basic_auth_header(user, password)
        else:
            creds = None

        request.meta['proxy'] = proxy_url
        if creds:
            request.headers['Proxy-Authorization'] = b'Basic ' + creds

class mdnProxyMiddleware(object):
        def process_request(self, request, spider):
            PROXIES = [
                {'ip_port': '111.11.228.75:80', 'user_pass': ''},
                {'ip_port': '120.198.243.22:80', 'user_pass': ''},
                {'ip_port': '111.8.60.9:8123', 'user_pass': ''},
                {'ip_port': '101.71.27.120:80', 'user_pass': ''},
                {'ip_port': '122.96.59.104:80', 'user_pass': ''},
                {'ip_port': '122.224.249.122:8088', 'user_pass': ''},
            ]
            proxy = random.choice(PROXIES)
            if proxy['user_pass'] is not None:
                request.meta['proxy'] = to_bytes("http://%s" % proxy['ip_port'])
                encoded_user_pass = base64.b64encode(
                    to_bytes(proxy['user_pass']))
                request.headers['Proxy-Authorization'] = to_bytes(
                    'Basic ' + encoded_user_pass)
                # print
                # "**************ProxyMiddleware have pass************" + proxy[
                #     'ip_port']
            else:
                # print
                # "**************ProxyMiddleware no pass************" + proxy[
                #     'ip_port']
                request.meta['proxy'] = to_bytes("http://%s" % proxy['ip_port'])

    # DOWNLOADER_MIDDLEWARES = {
    #     'step8_king.middlewares.ProxyMiddleware': 500,
    # }
