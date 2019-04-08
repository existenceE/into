#它是一个工具箱
#自动将输入文档转化为unicode编码，输出文档转换为UTF-8编码.不需要考虑编码方式
#解析时依赖解析器，其中lxml速度快容错能力强
from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.p.string)

#string或者get_text()一样效果
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup1 = BeautifulSoup(html, 'lxml') #这一步就自动更正格式了
print(soup1.prettify())
print(soup1.title.string)
#选择元素
print(soup1.title)
print(type(soup1.title))
print(soup1.title.string)
print(soup1.head)
print(soup1.p)

#提取信息
print(soup1.title.name)
print(soup1.p.attrs) #返回字典形式
print(soup1.p.attrs['name'])
#或者
print(soup1.p['name'])  #属性值唯一，返回单个字符串
print(soup1.p['class']) #一个元素可能有多个class 返回列表


#获取内容
print(soup1.p.string) #选择到的p节点是第一个p节点，获取的文本也是第一个p节点里的文本

#嵌套选择
print(soup1.head.title)
print(type(soup1.head.title))
print(soup1.head.title.string)


#关联选择


h2 = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a><a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup2 = BeautifulSoup(h2, 'lxml')

print("#########################®")

print(soup2.p.contents)   #列表形式，每个元素都是直接，【直接】子节点
print(soup2.p.children)   #生成器类型，用for循环输出相应的内功
for i,child in enumerate(soup2.p.children):
    print(i, child)

print(soup2.p.descendants)  #递归查询所有节点，得到所有的子孙节点
for i,c in enumerate(soup2.p.descendants):
    print(i, c)


print(soup2.a.parent)  #直接 【直接】父节点
print("*****************************************")
print(soup2.a.parents)   #所有祖先节点
print(type(soup2.a.parents))
print(list(enumerate(soup2.a.parents)))


print("Next Sibling: ", soup2.a.next_sibling)
print("Prev Sibling: ", soup2.a.previous_sibling)
#加s 生成器
print("Next Sibling", list(enumerate(soup2.a.next_siblings)))
print("Prev Sibling", list(enumerate(soup2.a.previous_siblings)))




print("Next Sibling:")
print(type(soup2.a.next_sibling))
print(soup2.a.next_sibling)
print(soup2.a.next_sibling.string)
print("Parent:")
print(type(soup2.a.parents))
print(list(soup2.a.parents)[0])
print(list(soup2.a.parents)[0].attrs['class'])  # list



#方法选择器
print(soup2.find_all(name='a'))
print(type(soup2.find_all(name='a')[0]))


h3='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(h3, 'lxml')
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]))

for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))

print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))

print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))  #class在Python理是关键字，所以需要加下划线

print(soup.find_all(text=re.compile('o')))


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#find值返回单个元素，第一个匹配的元素
print(soup.find(name='ul'))
print(type(soup.find(name='ul')))
print(soup.find(class_='list'))

#CSS选择器

print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))


#嵌套选择
for ul in soup.select('ul'):
    print(ul.select('li'))






