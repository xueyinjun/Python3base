#encondig=utf-8
# XPath 它是一门在XML文档中查找信息的语言

#常用规则
# / 从当前节点选取直接子节点
# 双斜杠 从当前节点选取子孙节点
# . 选取当前节点
# .. 选取当前节点的父节点
# @ 选取属性

#Example 1 lxml 模块的使用
# from lxml import etree
# text = '''
# <div>
# <Ul>
# <li class="item-O"><a href=”linkl.html”>first item</a><lli>
# <li class=”item-1”><a href=”link2.html”>second item</a><lli>
# <li class=”item-inactive”><a href="link3.html”>third item</a></h>
# <li class=” item-1”><a href="link4.html'’>fourth <li class=”item-口”><a hre于=”links . html”>fi干th </ul>
# </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))

#version2 调用文本文件进行解析
#添加完整路径
# from lxml import etree

# html = etree.parse('/Users/VON/WorkSpace/Python3cui/text.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))

# # #// *sx选取所有节点,结果是列表模式
# from lxml import etree
# html = etree.parse('/Users/VON/WorkSpace/Python3cui/text.html',etree.HTMLParser())
# result =html.xpath('//*')
# print(result)

# 所有的li节点，提取的结果是列表形式
# from lxml import etree
# html =  etree.parse('/Users/VON/WorkSpace/Python3cui/text.html', etree.HTMLParser())
# result = html.xpath('//li')
# print (result)
# print(result[0])

#子节点 version1 通过/和双斜杠可查找元素的子节点或子孙节点, version2 斜杠子节点，双斜杠，所有子孙节点,结果相同,/用于获取直接子节点，//用于获取子孙节点
# version1
# from lxml import etree

# html = etree.parse('/Users/VON/WorkSpace/Python3cui/text.html',etree.HTMLParser())
# result = html.xpath('//li/a')
# print(result)

#version2
# from lxml import etree

# html = etree.parse('/Users/VON/WorkSpace/Python3cui/text.html',
#                    etree.HTMLParser())
# result = html.xpath('//ul//a')
# print(result)

#父节点 version1用..实现， version2可以通过parent::*来获取父节点
#version1
# from lxml import etree

# html = etree.parse('/Users/VON/WorkSpace/Python3cui/text.html',
#                    etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/../@class')
# print(result)
#version2
# from lxml import etree

# html = etree.parse('/Users/VON/WorkSpace/Python3cui/text.html',
#                    etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# print(result)

#属性匹配 用符号@进行属性过滤
# from lxml import etree
# html = etree.parse('/Users/VON/WorkSpace/Python3cui/text.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]')
# print(result)

#文本获取 version1 获取li节点中的文本  version2 选取a节点获取文本,version3使用//
#version1
# from lxml import etree
# html = etree.parse('/Users/VON/WorkSpace/Python3cui/text.html',
#                    etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/text()')
# print(result)
#text() 前面的/含义是选取直接子节点，获取到换行符

#version2
# from lxml import etree
# html = etree.parse('/Users/VON/WorkSpace/Python3cui/text.html',
#                    etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/a/text()')
# print(result)

#version3  这里选取所有子孙节点的文本，// +text()方式可以保证获取到最全面的文本信息，可能会夹杂换行符等特殊字符，如果想获取特定的字符，定位到特定的子孙节点，然后用text()获取其中的内容
# from lxml import etree
# html = etree.parse('/Users/VON/WorkSpace/Python3cui/text.html',
#                    etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]//text()')
# print(result)

#属性获取  属性的获取和属性的匹配不同，属性的匹配会用到中括号加属性名和值来限定某个属性[]获取不会
# from lxml import etree
# html = etree.parse('/Users/VON/WorkSpace/Python3cui/text.html',
#                    etree.HTMLParser())
# result = html.xpath('//li/a/@href')
# print(result)

#属性多值匹配 contains()函数方法，第一个参数传入属性名称，第二个参数传入属性值，某个节点的某个属性有多个值时经常用到
#contains()函数方法
# from lxml import etree
# text = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class, "li")]/a/text()')
# print(result)

#多属性匹配 多个属性确认一个节点这时需要匹配多个属性，用运算符and来连接
# from lxml import etree
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
# print(result)

# 按序选择  可以用索引注意[]里面数字起始是1,last()函数方法是最后一位数，position()函数方法是位置
# from lxml import etree
# text = '''
# <div><ul>
# <li class="item-0"><a href="link1.html">first.html</a></li>
# <li class="item-1"><a href="link2.html"><first.html></a></li>
# <li class="item-inactive"><a href="link3.html">third item</a></li>
# <li class="item-1"><a href="link4-html">fourth item</a></li>
# <li class="item-0"><a href="link5-html">fifth item</a></li>
# </ul></div>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[1]/a/text()')
# print(result)
# result = html.xpath('//li[last()]/a/text()')
# print(result)
# result = html.xpath('//li[position()<3]/a/text()')
# print(result)
# result = html.xpath('//li[last()-2]/a/text()')
# print(result)

#节点轴选择  
# ancestor轴，可以获取所有祖先节点，后面需要跟两个冒号::然后是节点选择器
# attribute轴，可以获取所有属性值跟两个冒号::，后面跟的选择器是*
# child轴，可以获取所有直接子节点，跟两个冒号:
# descendant轴 后面跟两个冒号::获取所有子孙节点
# following轴，后面跟着两个冒号:: 获取当前节点之后的所有节点
# following-sibling轴 可以获取当前节点之后的所有同级节点
# from lxml import etree
# text = '''
# <div><ul>
# <li class="item-0"><a href="link1.html">first.html</a></li>
# <li class="item-1"><a href="link2.html"><first.html></a></li>
# <li class="item-inactive"><a href="link3.html">third item</a></li>
# <li class="item-1"><a href="link4-html">fourth item</a></li>
# <li class="item-0"><a href="link5-html">fifth item</a></li>
# </ul></div>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[1]/ancestor::*')
# print(result)
# result = html.xpath('//li[1]/ancestor::div')
# print(result)
# result = html.xpath('//li[1]/attribute::*')
# print(result)
# result = html.xpath('//li[1]/child::a[@href="link1.html"]')
# print(result)
# result = html.xpath('//li[1]/descendant::sapn')
# print(result)
# result = html.xpath('//li[1]/following::*[2]')
# print(result)
# result = html.xpath('//li[1]/following-sibling::*')
# print(result)