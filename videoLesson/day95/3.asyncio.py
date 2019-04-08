# 固定写法
# 支持tcp请求，不支持http请求
# http基于tcp做的，根据协议做改造
#
import asyncio


#
#
# async def task():
#     print('before ....  func1 ...')
#     await asyncio.sleep(5)
#     print('end .... func1 ...')
#
#
# tasks = [task(), task()]
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(*tasks))
# loop.close()

# async def task(host, url='/'):
#     print('start', host, url)
#     reader, writer = await asyncio.open_connection(host, 80)
#
#     request_header_content = """GET %s HTTP/1.0\r\nHost: %s\r\n\r\n""" % (
#     url, host,)
#     request_header_content = bytes(request_header_content, encoding='utf-8')
#
#     writer.write(request_header_content)
#     await writer.drain()
#     text = await reader.read()
#     print('end', host, url, text)
#     print(host, url, text)
#     writer.close()
#
#
# tasks = [
#     task('www.cnblogs.com', '/wupeiqi/'),
#     task('dig.chouti.com', '/pic/show?nid=4073644713430508&lid=10273091')
# ]
#
# loop = asyncio.get_event_loop()
# results = loop.run_until_complete(asyncio.gather(*tasks))
# loop.close()
import aiohttp

@asyncio.coroutine
def task(url):
    print(url)
    response = yield from aiohttp.request('GET', url)
    # data = await response.read()
    # print(url, data)
    print(url, response)
    response.close()


tasks = [task('http://www.baidu.com'), task('http://www.google.com')]

event_loop = asyncio.get_event_loop()
results = event_loop.run_until_complete(asyncio.gather(*tasks))
event_loop.close()









