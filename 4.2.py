# encoding='utf-8'
#3-24
#BeautifulSoup使用
#基本用法 Example1  首先声明变量是一个Html字符串， 把它当做第一个参数传入BeautifulSoup对象，该对象的第二个参数为解析器的类型,完成了初始化
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="sotry"> Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
# <a href="http://example.com/titllie" class="sister" id="link3">Tillie</a>;
#  and they lived at the bottom of a well.</p>
#  <p class="story">...</p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml') # 不标准的HTML字符串BeautifulSoup可以自动更正
# print (soup.prettify()) #用了prettify方法 可以把要解析的字符串以标准的缩进格式输出，
# print(soup.title.string) #输出HTML中title节点的文本内容，选出节点用string属性得到里面的文本

#节点选择器（选择元素,提取信息）

# 选择元素 Example2
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="sotry"> Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
# <a href="http://example.com/titllie" class="sister" id="link3">Tillie</a>;
#  and they lived at the bottom of a well.</p>
#  <p class="story">...</p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.title)
# print(type(soup.title)) #Tag类型:经过选择器选择后，选择结果都是这种Tag类型，Tag类型具有一定的属性
# print(soup.title.string) #string属性
# print(soup.head)
# print(soup.p) #多节点时这种选择方式只会选择到第一个匹配的节点，其他后面的节点都忽略

#提取信息 Example3 （获取名称，获取属性，获取内容）
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="sotry"> Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
# <a href="http://example.com/titllie" class="sister" id="link3">Tillie</a>;
#  and they lived at the bottom of a well.</p>
#  <p class="story">...</p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.title.name) #获取名称，用name属性获取名称
# print(soup.p.attrs)  #获取属性，每个节点可能由多个属性，调用atrrs获取所有属性,返回的结果是字典形式,把选择节点的属性和属性值组合成了一个字典
# print(soup.p.attrs['name']) #从字典中获取某一个值需要用中括号加属性名
# print(soup.p['name']) #简单写法不用写attrs,属性值是唯一的返回结果是单个字符串
# print(soup.p['class'])#一个节点元素可以有多个class所以返回的是列表
# print(soup.p.string) #利用string属性获取节点元素包含的内容，选择返回结果是第一个节点p的文本内容,注意选择方式只会选择第一个匹配到的节点，其他后面的节点都忽略

#嵌套选择:在Tag类型的基础上，再次选择得到的依然还是Tag类型，每次返回的结果都相同，这样就可以做嵌套
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="sotry"> Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
# <a href="http://example.com/titllie" class="sister" id="link3">Tillie</a>;
#  and they lived at the bottom of a well.</p>
#  <p class="story">...</p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)

#关联选择 (子节点和子孙节点，父节点和祖先节点，兄弟节点，提取信息)
#子节点和子孙节点，选取它的直接子节点，可以调用contents属性
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="sotry"> Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span><!--Elsie--></span>
</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
and
<a href="http://example.com/titllie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.p.contents)  #用contents属性选取直接子节点，结果是直接子节点列表，注意:用的是节点选择器，多个节点会选取第一个匹配节点
# print(soup.p.children)  # children直接子节点  返回的结果是生成器类型需要for循环输出相应的内容,enumerate( )迭代方法
# for i, child in enumerate(soup.p.children):
#     print(i, child)
#descendants()属性会递归查询所有子节点,得到所有子孙节点
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.p.descendants)
# for i,child in enumerate(soup.p.descendants):#descendants属性 会递归查询所有子节点，得到所有子孙节点
#     print(i, child)

#父节点和子孙节点

# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="sotry"> Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">
# <span><!--Elsie--></span>
# </a>
# </p>
# <p class="story"></p>
# """
#version1 获取直接父节点
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.a.parent)

#version2 获取所有祖先节点,parents属性，返回结果是生成器类型，这里用列表输出它的索引和内容
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(type(soup.a.parents))
# print(list(enumerate(soup.a.parents)))

#兄弟节点
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="sotry"> Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">
# <span><!--Elsie--></span>
# </a>
#             Hello
# <a href="http://www.example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
# <a href="http://example/title" class="sister" id="lin3">Title></a>
#         and they lived at the bottom of a well
# </p>
# <p class="story"></p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print('Next Sibling', soup.a.next_sibling) #节点的下一个兄弟元素
# print('Prev Sibling', soup.a.previous_sibling) # 节点的上一个兄弟元素
# print('Next Sibling', list(enumerate(soup.a.next_siblings))) #返回所有后面的兄弟节点的生成器
# print('Prev Sibling', list(enumerate(soup.a.previous_siblings))) #返回所有前面的兄弟节点的生成器

# #提取信息 注意这里的html文本,如果有换行会影响输出结果
# html ="""
# <html>
# <body>
# <p class = "story">
# Once upon a time there were three little sisters;and their names were
# <a href ="http://example.com/elsie" class="sister" id="link1">Bob</a><a href ="http://example.com/lacie" class="sister" id="link2">Lacie</a>
# </p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print("Next Sibling:")  #单个节点可以直接调用属性获取文本和属性
# print(type(soup.a.next_sibling))
# print(soup.a.next_sibling)
# print(soup.a.next_sibling.string)
# print('Parent:') # 返回的结果是多个节点的生成器，则可以转为列表后取出某个元素
# print((type(soup.a.parents)))
# print(list(soup.a.parents)[0])
# print(list(soup.a.parents)[0].attrs['class'])

#方法选择器
#Beautiful Soup还为我们提供了一些查询方法，find_all()和find()等
#方法1 find_all()查询所有符合条件的元素 find_all(name, attrs, recursive, text, **kwargs)
# html = '''
# <div class="panel">
# <div class = "panel-heading">
# <h4>Hello</h4>
# </div>
# <div class="panel-body">
# <ul class="list" id="list-1">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>
# <ul class="list list-small" id="list-2">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# </ul>
# </div>
# </div>
# '''
#(1)name 根据节点名来查询元素,返回的结果是列表类型
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name='ul')[0]))
#嵌套操作 查询出所有的ul再继续查询内部的li节点
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
# 遍历每一个li获取它的文本
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
#     for li in ul.find_all(name='li'):
#         print(li.string)
#(2)根据一些属性来查询  传入attrs参数，参数的类型是字典类型，得到的结果是列表形式
# html = '''
# <div class="panel">
# <div class = "panel-heading">
# <h4>Hello</h4>
# </div>
# <div class="panel-body" name="elements">
# <ul class="list" id="list-1">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>
# <ul class="list list-small" id="list-2">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# </ul>
# </div>
# </div>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(attrs={'id': 'list-1'}))
# print(soup.find_all(attrs={'name': 'elements'}))
#简单方式
#一些常用的属性如id和class等可以不用atrrs来传递，由于class在Python中是一个关键字，所以后面须加一个下划线，返回的结果依旧是列表
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(id='list-1'))
# print(soup.find_all(class_='element'))
#text text参数可用来匹配节点的文本，传入形式可以是字符串，也可以是正则表达式对象
# import re
# html = '''
# <div class="panel">
# <div class="panel-body">
# <a>Hello this is a link</a>
# <a>Hello this is a link, too</a>
# </div>
# </div>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(text=re.compile('link')))
#find()方法，返回的是单个元素，也就是第一个匹配的元素是Tag类型，find_all()返回的是所有匹配元素组成的列表
# html = '''
# <div class="panel">
# <div class = "panel-heading">
# <h4>Hello</h4>
# </div>
# <div class="panel-body" name="elements">
# <ul class="list" id="list-1">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>
# <ul class="list list-small" id="list-2">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# </ul>
# </div>
# </div>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find(name='ul'))
# print(type(soup.find(name='ul')))
# print(soup.find(class_='list'))

#find_parents()和find_parent()返回所有祖先节点，和返回直接父节点
#find_next_siblings()和find_next_sibling() 返回后面所有兄弟的节点，返回后面第一个兄弟节点
#find_previous_siblings()和find_previous_sibling()返回前面所有的兄弟节点，返回前面第一个兄弟节点
#find_all_next()和find_next()返回节点后所有符合条件的节点，返回第一个符合条件的节点
#find_all_previous()和find_previous()返回节点后所有符合条件的节点，后者返回第一个符合条件的节点

#CSS选择器 Beautiful Soup还提供了CSS选择器只需要调用select(),嵌套选择，获取属性，获取文本
# class用 .符号,id用#符号,返回的结果是列表形式
html = '''
<div class="panel">
<div class = "panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body" name="elements">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class=" list-smalistll" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))
# print(soup.select('ul')[0])
#嵌套选择 选择所有ul节点，遍历ul节点选择其li节点
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# for ul in soup.select('ul'):
#     print(ul.select('li'))
#获取属性
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# for ul in soup.select('ul'):
#     print(ul['id'])
#     print(ul.attrs['id'])
#获取文本
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)