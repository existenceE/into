
html = """<!DOCTYPE html>
<html>
    <head lang="en">
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <ul>
            <li class="item-"><a id='i1' href="link.html">first item</a></li>
            <li class="item-0"><a id='i2' href="llink.html">first item</a></li>
            <li class="item-1"><a href="llink2.html">second item<span>vv</span></a></li>
        </ul>
        <div><a href="llink2.html">second item</a></div>
    </body>
</html>
"""




from scrapy.http import HtmlResponse
response = HtmlResponse(url="http://www.baidu.com", body=html, encoding='utf-8')

response.xpath('')

#
# from scrapy.selector import Selector
# hxs = Selector(response)
# hxs.xpath()