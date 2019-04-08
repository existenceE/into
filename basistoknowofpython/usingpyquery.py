
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

from pyquery import PyQuery as pq
doc = pq(html)  #传入html文本来初始化一个pyquery对象
# print(doc('li'))
#
#
#
# doc = pq(url="https://www.douban.com")
# print(doc('title'))
#
# #等同于
# import requests
# doc = pq(requests.get('https://cuiqingcai.com').text)
# print(doc('title'))


print(doc('#container .list li'))
print(type(doc('#container .list li')))

#find()的范围是节点的所有子孙节点，如果只想找子节点，可以用children()
items = doc('.list')
lis = items.find('li')
print(lis)

lis = items.children()
print(type(lis))
print(lis)

#筛选子节点中符合条件的节点
lis = items.children('.active')
print(lis)

items = doc('.list')
container = items.parent()
print(type(container))
print(container)

#parents 祖先 siblings() 兄弟
#遍历

lis = doc("li").items()
print(type(lis))
for li in lis:
    print(li, type(li))

#获取信息，分别为获取属性 获取文本
a = doc('.item-0.active a')
print(a, type(a))
#如果a包含多个结果，只会得到第一个
print(a.attr('href'))
print(a.attr.href)

a = doc('a')
for item in a.items():
    print(item.attr('href'))


#a.text()来获取文本，此时会忽略节点内部包含的所有html，只返回纯文字内容
#a.html()返回结果是li节点内的所有html文本
#如果是多个结果，html()返回的是第一个内部的html文本，而text()则是返回所有li节点内的纯文本 中间用一个空格
#分隔开，即返回结果是一个字符串

#节点操作，动态改变节点的class属性 li.addClass('active')  li.removeClass('active')
#attr\text\html
#attr至少一个，text html可以没有参数
li = doc('.item-0.active')
print(li)
li.attr('name', 'link')
print(li)
li.text('changed item')
print(li)
li.html('<span>changed item</span>')
print(li)



print("(((((((((((((((((((((((((((")
html = '''
<div class="wrap">
Hello, World
<p> This is a paragraph. </p>
</div>

'''
doc = pq(html)
wrap = doc('.wrap')
print(wrap)
print(wrap.text())

wrap.find('p').remove()

print(wrap.text())


#伪类选择器

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:contains(second)')
print(li)







