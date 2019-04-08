#下滑微博 出现加载动画 这就是ajax加载的过程 页面没有整个刷新，链接也没有变化但是网页中多出很多新内容
# 发送Ajax请求到网页更新的过程分为3步，发送请求，解析内容，渲染网页



from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
db = client['weibo']
collection = db['weibo']

base_url = 'https://m.weibo.cn/api/container/getIndex?'
#base_url = 'https://m.weibo.cn/u/3978924263?display=0&retcode=6102'
#Request URL: https://m.weibo.cn/api/container/getIndex?display=0&retcode=6102&type=uid&value=3978924263&containerid=1076033978924263&page=4


headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/3978924263',
    #https://m.weibo.cn/u/3978924263?display=0&retcode=6102
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

#获取每次请求的结果
def get_page(page):
    params = {
        'type': 'uid',
        'value': '3978924263',
        'containerid': '1076033978924263',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


#解析方法，从结果中提取想要的信息

def parse_pase(json):
    if json:
        items = json.get('data').get('cards')
        for i in items:
            i = i.get('mblog')
            weibo = {}
            weibo['id'] = i.get('id')
            weibo['text'] = pq(i.get('text')).text()
            weibo['attitudes'] = i.get('attitudes_count')
            weibo['comments'] = i.get('comments_count')
            weibo['reposts'] = i.get('reposts_count')
            yield weibo

def save_to_mongo(result):
    if collection.insert_one(result):
        print('Saved to Mongo')

if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page(page)
        results = parse_pase(json)
        for r in results:
            print(r)
            save_to_mongo(r)















