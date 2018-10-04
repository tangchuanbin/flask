#!/usr/bin/python3
#coding = utf-8
# 抓取汽车之家网站
import requests
from bs4 import BeautifulSoup
import weibo_image
from pymongo import MongoClient
import time

client   = MongoClient()
db       = client.test
car_life = db.car_life

user_agent = 'Mozilla/5.0 (Macintosh; )ntel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

header = {
        'User-Agent'                : user_agent
    }
#res = requests.get(url, headers = header)
#print(res.text)

def begin():
    print('开始抓取汽车之家论坛精选')
    # 由于汽车之家可以看到一共有多少页，所以循环的时候写死吧
    begin = 2
    end   = 3
    while begin < end :
        begin = begin + 1
        url = 'https://club.autohome.com.cn/JingXuan/292/3'
        res = requests.get(url, headers = header)
        if res.status_code != 200:
            print('error')
            exit()
        bf = BeautifulSoup(res.text, features="html.parser")
        node_list = bf.find_all('ul', class_ = 'content')[0].find_all('li')
        for one in node_list:
            one_mm_car = {}
            one_mm_car['detail_img'] = []
            one_mm_car['my_url'] = []
            # 取出缩略图
            thumbnail = one.find('img')['data-original']
            thumbnail = 'http:' + thumbnail
            one_mm_car['thumbnail'] = thumbnail
            # 取出图片信息
            info = one.find('a')['title']
            info = info.replace(' ', '')
            one_mm_car['info'] = info
            # 取出detail_url
            detail_url = one.find('a')['href']
            detail_url = 'http:' + detail_url
            # 点击进入详情抓取图片
            print(detail_url)
            detail = requests.get(detail_url, headers = header)
            if detail.status_code != 200:
                print('detail error')
                continue
            detail_node = BeautifulSoup(detail.text, features="html.parser")
            imgs = detail_node.find_all('div', class_='rconten')[0].find_all('img')
            # 取出每一张图片
            count  = 0
            for img in imgs:
                count = count + 1
                img_name = info + '_' + str(count) + '.jpg'
                img_url ='http:' +  img['src']
                if img_url == 'http://x.autoimg.cn/club/lazyload.png':
                    img_url = 'http:' + img['src9']
                if img_url.split('.', len(img_url))[-1] == 'gif':
                    continue
                print(img_url)
                one_mm_car['detail_img'].append(img_url)
                save = requests.get(img_url, headers = header)
                with open('autos/' + img_name, 'wb') as f:
                    f.write(save.content)
                    print('成功保存' + img_name)
                # 微博图床
                weibo_bed = weibo_image.to_weibo('autos/' + img_name)
                if weibo_bed is None:
                    one_mm_car['if_bed'] = 0
                    one_mm_car['my_url'].append('')
                    continue
                else:
                    one_mm_car['if_bed'] = 1
                    one_mm_car['my_url'].append('http://ww2.sinaimg.cn/large/'+ weibo_bed)
                time.sleep(3)

                print('http://ww2.sinaimg.cn/large/' + weibo_bed)
            car_life.insert(one_mm_car)


begin()


    
