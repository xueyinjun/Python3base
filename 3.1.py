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
 