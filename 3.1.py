#coding=utf-8
#当使用urllib.urlopen打开一个 https 链接时，会验证一次 SSL 证书。

#1 使用ssl创建未经验证的上下文，在urlopen中传入上下文参数

# import ssl
# import urllib
# context=ssl._create_unverified_context()
# print(urllib.urlopen('htttps://www.12306.cn/mormhweb/',context=context).read())

#2全局取消证书验证
# import ssl
# import urllib
# ssl._create_default_https_context=ssl._create_unverified_context
# print(urllib.urlopen('https://www.12306.cn/mormhweb').read())

#注意在全局请求文件导入import ssl
# import ssl
# ssl._create_default_https_context=ssl._create_unverified_context

# import ssl
# import urllib.request
# context=ssl._create_unverified_context()
# response = urllib.request.urlopen('https://www.python.org',context=context)
# print(response.read().decode('utf-8'))

#type()
# import ssl
# import urllib.request
# ssl._create_default_https_context=ssl._create_unverified_context
# response=urllib.request.urlopen('https://www.pyton.org')
# print(type(response))

#把response看成一个变量,调用response这个变量的其他方法
# import ssl
# import urllib.request
# ssl._create_default_https_context=ssl._create_unverified_context
# response=urllib.request.urlopen('https://www.python.org')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

#data参数
#其中转字节流采用了bytes()方法,该方法的第一个参数需要是str(字符串)类型
# 需要用urllib.parse模块里的urlcode()方法来将参数字典转换成字符串，第二个参数指定编码格式，这里指为utf-8

# import urllib.parse
# import urllib.request

# data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
# response=urllib.request.urlopen('http://httpbin.org/post',data)
# print(response.read())

#timeout 参数

# import urllib.request
# response=urllib.request.urlopen('http://httpbin.org/get',timeout=1)
# print(resposne.read())

#通过timeout设置这个超时间来控制一个网页如果长时间未响应，就跳过它的抓取
# import socket
# import urllib.error
# import urllib.request

# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')

#Request
#我们依然是用urlopen()方法来发送这个请求，只不过这次该方法的参数不再是URL，而是一个Request类型的对象
#通过构造这个数据结构，一方面我们可以将请求独立成一个对象，另一方面可更加丰富和灵活的配置参数
# import urllib.request
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

#传入多个参数构造
# from urllib import request,parse
# url='http://httpbin.org/post'
# headers={
#     'User-Agent':'AppleWebKit/537.36 (KHTML, like Gecko)',
#     'Host':'httpbin.org'
# }
# dict={
#     'name':'Germey'
# }
# data=bytes(parse.urlencode(dict),encoding='utf8')
# req=request.Request(url=url,data=data,headers=headers,method='POST')
# response=request.urlopen(req)
# print(response.read().decode('utf-8'))

#add_header()方法
# from urllib import request,parse
# url='http://httpbin.org/post'

# dict={
#     'name':'Germey'
# }
# data=bytes(parse.urlencode(dict),encoding='utf-8')
# req=request.Request(url=url,data=data,method='POST')
# req.add_header( 'User-Agent','AppleWebKit/537.36 (KHTML, like Gecko)')
# response=request.urlopen(req)
# print(response.read().decode('utf-8'))

#高级方法 Handler OpennerDirector

# 这里首先实例化HTTPBasicAuthHandler对象，其参数是HTTPPasswordMgrWithDefaultRealm对象
#利用add_passwor()添加进去用户名和密码，这样就建立一个处理验证的Handler
#利用Hanlder 并使用build_opener()方法构建一个Opener,这个Opener在发送时就相当于验证成功，
# 利用Opener的open()方法打开链接，就可以完成验证，这里获到的结果就是验证后的页面源码内容，

# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# username = 'username'
# password = 'password'
# url = 'https://passport.bilibili.com/login'

# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)

# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
# except URLError as e:
#     print(e.reason)

#代理
# from urllib.error import URLError
# from urllib.request import ProxyHandler,build_opener
# import ssl

# ssl._create_default_https_context=ssl._create_unverified_context

# proxy_handler=ProxyHandler(
#     {
#         'http':'http://121.61.2.246:9999',
#         'https':'https://121.61.2.246:9999'
#     }
# )
# opener=build_opener(proxy_handler)
# try:
#     response=opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

#Cookies
#怎样将网站的Cookies获取下来
# import http.cookiejar,urllib.request

# cookie=http.cookiejar.CookieJar()
# handler=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(handler)
# reponse=opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+"="+item.value)

#Cookies 以文本形式保存
# import http.cookiejar, urllib.request
# filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

#改为LWP格式
# import http.cookiejar, urllib.request
# filename = 'cookies1.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# hanlder = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(hanlder)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# 读取Cookies1并利用
# import http.cookiejar, urllib.request
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookies1.txt', ignore_discard=True, ignore_expires=True)
# hanlder = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(hanlder)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))

#处理异常
#URLError  它有一个属性reason 即返回错误的原因
# import ssl
# from urllib import request, error
# ssl._create_default_https_context = ssl._create_unverified_context
# try:
#     response = request.urlopen('https://cuiqingcai.com/index.htm')
# except error.URLError as e:
#     print(e.reason)

#HTTPError  先捕获子类的错误，再去捕获父类的错误
# from urllib import request,error
# import ssl
# ssl._create_default_https_context=ssl._create_unverified_context
# try:
#  response=request.urlopen('https://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers)
#更好的写法
# from urllib import request,error
# import ssl
# ssl._create_default_https_context=ssl._create_unverified_context
# try:
#     response=request.urlopen('https://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.reason)
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')

#有时候，reason属性返回的不一定是字符串，可能是一个对象
# import socket
# import urllib.request
# import urllib.error
# import ssl
# ssl._create_default_https_context=ssl._create_unverified_context
# try:
#  response=urllib.request.urlopen('https://www.baidu.com',timeout=0.01)
# except urllib.error.URLError as e:
#     print(type(e.reason))
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')

#解析链接
#urlparse()
#可以实现URL的识别和分段
# from urllib.parse import urlparse
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)

#scheme 参数
# import ssl
# from urllib.parse import urlparse
# ssl._create_default_https_context = ssl._create_unverified_context
# result = urlparse('www.baidu.com/index.html;user?id=5#comment', 'https')
# print(result)

#allow_fragments   fragment部分为空
# from urllib.parse import urlparse
# result = urlparse(
#     'http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
# print(result)

#返回结果ParseResult 实际上是一个元组，我们可以用索引顺序来获取，也可以用属性名获取，

# from urllib.parse import urlparse
# result=urlparse('http://www.baidu.com/index.html#comment',allow_fragments=False)
# print(result.scheme,result[0],result.netloc,result[1])

#urlunparse() 可迭代对象 长度必须是6 参数data用了列表类型，可以用元组或者特定的数据结构
# from  urllib.parse import urlunparse
# data=['http','www.baidu.com','index.html','user','a=6','comment']
# print(urlunparse(data))

#urlspit() 和urlparse()方法类似，只不过不再单独解析params这部分，params会合并到path中
# from urllib.parse import urlsplit

# result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
# print(result)

#SplitResult结果是一个元组类型，可以用属性获取，索引获取
# from urllib.parse import urlsplit
# result = urlsplit('http://www.baidu.com/index.html;user?id=5#commment')
# print(result.scheme, result[0])

#urlunsplit() 和urlunpaser()类似，它也是将各个部分组合成完整链接的方法，传入的参数是一个可迭代的对象，例如列表，元组等

# from urllib.parse import urlunsplit
# data=['http','www.baidu.com','index.html','a=6','comment']
# print(urlunsplit(data))

#urljion() base_url作为第一个链接，将新的链接作为第二个参数
# from urllib.parse import urljoin
# print(urljoin('http://www.baidu.com','FAQ.html'))
# print(urljoin('http://www.baidu.com','https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html?question=2'))
# print(urljoin('http://www.baidu.com/wd=abc','https://cuiqingcai.com/index.php'))
# print(urljoin('www.baidu.com','?category=2#comment'))
# print(urljoin('www.baidu.com#comment','?category=2'))

#urlencode()构造GET请求参数 将字典参数序列化为URL的参数
# from urllib.parse import urlencode
# params = {'name': 'germey', 'age': 22}
# base_url = 'http://www.baidu.com'
# url = base_url + urlencode(params)
# print(url)

#parse_qs() 反序列化 把str类型转化为字典类型
# from urllib.parse import parse_qs
# query = 'name=germey&age=22'
# print(parse_qs(query))

#parse_qsl()用于将str类型的GET参数转化为元组组成的列表 第一个内容是参数名，第二个内容是参数值
# from urllib.parse import parse_qsl
# query = 'name=germey&age=22'
# print(parse_qsl(query))

#quote() 这个方法可以将内容转化为URL编码格式
# from urllib.parse import quote

# keyword = '壁纸'
# url = 'https://www.baidu.com/s?wd=' + quote(keyword)
# print(url)

#unquote()将URL编码的格式转化为内容
# from urllib.parse import unquote
# url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
# print(unquote(url))

#robotparser类 RobotFileParser(url='') 创建了RobotFileParser对象，然后通过set_url()方法设置robots.txt的链接 用can_fetch判断
# from urllib.robotparser import RobotFileParser
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# rp = RobotFileParser()
# rp.set_url('http://www.jianshu.com/robots.txt')
# rp.read()
# print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
# print(
#     rp.can_fetch('*',
#                  'http://www.jianshu.com/search?q=python&type=collections'))

#使用parse()方法执行读取和分析
#urlopen 打开请求会发生403错误 网站服务器会检查User-Agent 用urllib.request.Request 构造完整的请求头
# from urllib.robotparser import RobotFileParser
# from urllib.request import urlopen, Request
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# headers = {
#     'User-Agent':
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
# }
# req = Request('https://www.jianshu.com/robots.txt', headers=headers)
# rp = RobotFileParser()
# rp.parse(urlopen(req).read().decode('utf-8').split('\n'))
# print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
# print(
#     rp.can_fetch('*',
#                  'http://www.jianshu.com/search?q=python&page=collection'))

