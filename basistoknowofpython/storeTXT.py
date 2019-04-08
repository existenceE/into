#保存知乎上发现页面的热门话题部分，将问题和答案统一保存成文本形式
# 用requests将网页源码获取，用pyquery解析，接下来将提取标题 回答者 回答 保存到文本


import requests
from pyquery import PyQuery as pq


url = "https://www.zhihu.com/explore"
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 \
                 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

html = requests.get(url, headers = headers).text
doc = pq(html)  #让页面更加规整 ，比如添加相应的标签，格式性更加强
#print(doc)
#print(html)
# print(requests.get(url, headers)) #400
#print(requests.get(url, headers = headers)) # <Response [200]>


items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()  #str，首先获取这个类的html文本，重新构造成pq对象 #answer1 = item.find('.content')   #pyquery  #answer2 = item.find('.content').html()   #str
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()

# with open('explore.txt', 'w', encoding='utf-8') as file:
#     file.write('\n'.join([question, author, answer]))
#     file.write('\n' + '=' * 50 + '\n')



















