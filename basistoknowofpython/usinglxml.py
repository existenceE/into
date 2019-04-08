from lxml import etree
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">2nd item</a></li>
<li class="item-inactive"><a href="link3.html">3rd item</a></li>
<li class="item-1"><a href="link4.html">4th item</a></li>
<li class="item-0"><a href="link5.html">5th item</a>
</li>
</ul>
</div>
'''

html = etree.HTML(text)
result = etree.tostring(html)
#print(result.decode('utf-8'))



h2 = etree.parse('./test.html', etree.HTMLParser())
r2 = etree.tostring(h2)
print(r2.decode('utf-8'))

# 用//开头的XPath规则 选取所有符合要求的节点,*代表匹配所有节点
r3 = html.xpath('//*')
print(r3)

#选取所有li节点
r4 = html.xpath('//li')
print(r4)
print(r4[0])


#选取所有li节点的所有直接a子节点，//为子孙节点
r5 = html.xpath('//li/a')
print(r5)

#父节点获取
r6 = html.xpath('//a[@href="link4.html"]/parent::*/@class')
#r6 = html.xpath('//a[@href="link4.html"]/../@class')
print(r6)

#属性获取
r7 = html.xpath('//li[@class="item-0"]')
print(r7)


#文本获取，使用text()
r8 = html.xpath('//li[@class="item-0"]/text()')
print(r8)

#选取到a节点再获取文本，更整洁
r9 = html.xpath('//li[@class="item-0"]/a/text()')
print(r9)
#第二种方法
r10 = html.xpath('//li[@class="item-0"]//text()')
print(r10)

#属性获取
rA = html.xpath('//li/a/@href')
print(rA)


#属性多值匹配,contains()函数,某节点的某个属性有多个值

text1 = '''
<li class="li li-first", name="item"><a href="link.html">first item</a></li>
<li class="li-se"><a href="link.html">second item</a></li>
'''
html1 = etree.HTML(text1)
#result1 = html1.xpath('//li[@class="li"]/a/text()')
result1 = html1.xpath('//li[contains(@class, "li")]/a/text()')
print(result1)


#多个属性确定一个节点,用and来连接
html2 = etree.HTML(text1)
result2 = html2.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result2)


#li[1]，次序与代码不同
#li[last()], li[position()<3], li[last()-2]


#节点轴选择，获取子 兄弟 父亲 祖先 元素







