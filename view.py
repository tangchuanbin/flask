#!/usr/bin/python3
#coding = utf-8
# 抓取pixabay网站
import requests
from bs4 import BeautifulSoup
import weibo_image
from pymongo import MongoClient
import time
import random

client   = MongoClient()
db       = client.test
view     = db.view


user_agent = 'Mozilla/5.0 (Macintosh; )ntel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

header = {
        'User-Agent'                : user_agent
    }

def begin():
    print('开始抓取pixabay')
    start = 1
    while start < 20:
        url = 'https://pixabay.com/en/photos/?cat=nature' + '&pagi=' + str(start)
        res = requests.get(url , headers = header)
        if res.status_code != 200:
            print('error')
            exit()
        bf = BeautifulSoup(res.text, features="html.parser")
        node_list = bf.find_all('div', class_ = 'item')
        
        for one in node_list:
            one_view = {}
            one_view['page'] = start
            one_view['rand'] = random.randint(1, 100000)
            # 找到跳转的详情
            to_detail_url = one.find_all('a')[0]['href']
            to_detail_url = 'https://pixabay.com' + to_detail_url
            # 找到img缩略图
            thumbnail_img = one.find_all('a')[0].find('img')
            if thumbnail_img['src'] == '/static/img/blank.gif':
                thumbnail = thumbnail_img['data-lazy']
            else :
                thumbnail = thumbnail_img['src']
            # 取得name
            name = one.find_all('a')[0].find('img')['alt']
            name = name.replace(' ', '').replace(',', '')
            # 由于详情的图片地址和缩略图的地址是一样的，区别就在于后面的数字不同
            # 比如缩略图的网址是这样：https://cdn.pixabay.com/photo/2018/09/23/09/43/apple-3697042__340.jpg
            # 那么他的详细图有如下几个
            # 1.__480, 2._960_720, 3._1280
            prefix = thumbnail.split('__', len(thumbnail))
            one_view['detail_img'] = [prefix[0] + '__480', prefix[0] + '_960_720', prefix[0] + '_1280']
            one_view['thumbnail']  = thumbnail
            one_view['name']       = name

            save = requests.get(thumbnail, headers = header)
            if save.status_code != 200:
                print('error')
                continue
            img_name = name + '.jpg'
            with open('views/' + img_name, 'wb') as f:
                f.write(save.content)
                print('成功保存' + name)
            # 微博图床
            weibo_bed = weibo_image.to_weibo('views/' + img_name)
            if weibo_bed is None:
                one_view['if_bed'] = 0
                one_view['my_url'] = ''
                continue
            else:
                one_view['if_bed'] = 1
                one_view['my_url'] = 'http://ww2.sinaimg.cn/large/'+ weibo_bed
                print('http://ww2.sinaimg.cn/large/'+ weibo_bed)
            view.insert(one_view)
            time.sleep(3)
        start = start + 1
begin()
    
