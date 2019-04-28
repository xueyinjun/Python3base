# coding=<'utf-8'>
#分析Ajax爬取今日头条街拍美图
#当前的URL链接，第一个请求得到的结果渲染出来，它的结果是否包含页面中的相关数据的值，找到它的列表形式，请求是一个GET方法请求URL的参数有找出参数的规律
#分析Ajax请求的逻辑，实现get_page()来加载单个Ajax请求的结果，唯一变化的参数是offset所以我们将它作为参数传递

import requests
from urllib.parse import urlencode
from requests import codes
import os
from hashlib import md5
from multiprocessing.pool import Pool
import re
from pymongo import MongoClient


#用urlencode()方法构造请求的GET参数，然后用requests请求这个链接，如果状态码为200，则调用response的json()方法将结果转换为JSON格式，然后返回
def get_page(offset):
    params = {
        'aid': '24',
        'offset': offset,
        'format': 'json',
        #'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    base_url = 'https://www.toutiao.com/api/search/content/?keyword=%E8%A1%97%E6%8B%8D'
    url = base_url + urlencode(params)
    try:
        resp = requests.get(url)
        print(url)
        if 200 == resp.status_code:
            print(resp.json())
            return resp.json()
    except requests.ConnectionError:
        return None


#实现一个解析方法，提取每条数据字段中的每一张图片链接，将图片链接和图片所属的标题一并返回，
def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                origin_image = re.sub("list", "origin", image.get('url'))
                yield {
                    'image': origin_image,
                    # 'iamge': image.get('url'),
                    'title': title
                }


print('succ')


# 实现保存图片的save_image方法，其中item就是前面get_images()方法返回的一个字典，该方法中，首先根据item的title来创建文件，然后请求这个图片链接，获取图片的二进制数据，以二进制的形式写入数据，图片的名称可以使用其内容的MD5值，这样可以去除重复
def save_image(item):
    img_path = 'img' + os.path.sep + item.get('title')
    print('succ2')
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        resp = requests.get(item.get('image'))
        if resp.status_code == 200:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(resp.content).hexdigest(), file_suffix='jpg')
            if not os.path.exists(file_path):
                print('succ3')
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded image path is %s' % file_path)
                print('succ4')
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image，item %s' % item)


def insert_into_mongodb(item, collection):
    #输入字典要存入的集合
    result = collection.insert_one(item)
    print(result)


#构造一个offset数组，遍历offset，提取图片链接，并将其下载即可，这里定义了起始页数和终止页数，利用了多线程的线程池，调用其map()方法实现多线程下载
def main(offset):
    print('main', offset)
    client = MongoClient('mongodb://localhost:2017')
    db = client.toutiao
    collection = db.jiepai
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START = 0
GROUP_END = 7

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
