from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, urljoin, urlencode
from urllib.parse import parse_qs, parse_qsl


result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data)) #长度为6，区分于urlunsplit长度为5

result2 = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result2)

data2 = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data2))

#实现链接的解析、拼合与生成
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))

#构造GET请求参数
params = {
    'name': 'germey',
    'age': 22
}
base_url = 'http://www.baidu.com?' #此处有问号
url = base_url + urlencode(params)
print(url)

#反序列化，将一串GET请求参数转回字典
query = 'name=germey&age=22'
print(parse_qs(query))

#将参数转化为元组组成的列表
query = 'name=germey&age=22'
print(parse_qsl(query))

#将内容转化为URL编码格式
from urllib.parse import quote, unquote
keyword = 'wallpaper 壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)

url2 = 'https://www.baidu.com/s?wd=wallpaper%20%E5%A3%81%E7%BA%B8'
print(unquote(url2))











