#!/usr/bin/python3
#coding = utf-8

# 抓取www.nvshens.com网站图片
# 从https://www.nvshens.com/gallery/yazhou/ 这个亚洲分类开始抓取,首先抓取这个页面的头图和页数和每一个头像的详情页面
# 开始
from bs4 import BeautifulSoup
import requests
import os
import time
import weibo_image
from pymongo import MongoClient

client = MongoClient()
db = client.test
mm = db.mm1

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
header = {
        'User-Agent'                : user_agent,
        'Host'                      : 'www.nvshens.com',
        'Upgrade-Insecure-Requests' : 1
}
prox = { 
        'http' : 'http://218.22.7.62:53281',
    }   
def begin():
    print('开始爬取数据')
    # 图床上传URL
    bed_url = 'https://sm.ms/api/upload'
    # 定义列表
    url = 'https://www.nvshens.com/gallery/luoli/3.html'
    next_home_page_url = 'https://www.nvshens.com/gallery/luoli/4.html'
    while ('https://www.nvshens.com/gallery/luoli' != next_home_page_url):
        mm_list = []
        res = requests.get(url, headers = header, proxies = prox, verify = False, timeout = 2000)
        res.encoding = 'utf-8'
        bf = BeautifulSoup(res.text)
        mm_avatars = bf.find_all('a', class_ = 'galleryli_link')
        # 分页信息
        home_next_page     = bf.find_all('div', class_ = 'pagesYY')
        next_home_page_url = 'https://www.nvshens.com' + home_next_page[0].find_all('a')[-1]['href']
        url = next_home_page_url
        print(next_home_page_url)
        for mm_avatar in mm_avatars:
            cur_home_page      = home_next_page[0].find_all('a', class_ = 'cur')[0].contents[-1]
            one_mm = {}
            one_mm['curpage'] = cur_home_page
            # 找到所有的缩略图点击进入详情的链接
            to_detail_url = 'https://www.nvshens.com'+ mm_avatar['href']
            print(to_detail_url)
            # 取出缩略图
            thumbnail = mm_avatar.select('img')[0]['data-original']
            # 点击链接进入详情
            res = requests.get(to_detail_url, headers = header)
            res.encoding = 'utf-8'
            bf = BeautifulSoup(res.text)
            #print(bf.title)
            name = bf.title.contents[0]
            # 保存name
            one_mm['name'] = name
            print('开始保存' + name + '的图片')
            # 保存缩略图
            one_mm['thumbnail'] = thumbnail
            one_mm['images_detail'] = []
            one_mm['my_url'] = []
            # 先拿出这一页的图片
            images = bf.select('#hgallery > img')
            for image in images:
                one_mm['images_detail'].append(image['src'])
                # save到文件
                request_image_header = {
                        'Referer': to_detail_url ,
                }
                save = requests.get(image['src'], headers = request_image_header,timeout = 2000)
                image_name = ((image['alt'].replace(' ', '')).replace('\\', '')).replace('/', '')
                with open('images1/' + image_name  + ".jpg", 'wb') as f:
                    f.write(save.content)
                    print('成功保存' + image_name)
                # 因为sm.ms上传中文名出错所以重命名
                old = os.path.join(os.getcwd(), 'images1/' + image_name + ".jpg")
                new = os.path.join(os.getcwd(), 'images1/' + 'rename.jpg')
                os.rename(old, new)
                # 上传到图床
                #smfile = open(new, 'rb')
                #sm_post_data = {
                #        'smfile' : smfile
                #        }
                #to_bed = requests.post(bed_url, files = sm_post_data) 
                #print(to_bed.text) 
                #if to_bed.json()['code'] == 'success':
                #    one_mm['my_url'].append(to_bed.json()['data']['url'])
                #    one_mm['if_true'] = 1
                #    print('成功保存到图床' + to_bed.json()['data']['url'])
                #else:
                #    one_mm['my_url'].append('')
                #    one_mm['if_true'] = 0
                #    if to_bed.json()['msg'].find('Upload file count limit') == 0 :
                #        time.sleep(3600)
                #smfile.close()
                #os.rename(new, old)
                #time.sleep(3)
                # 微博图床
                weibo_bed = weibo_image.to_weibo(new)
                if weibo_bed is None:
                    one_mm['if_bed'] = 0
                    one_mm['my_url'].append('')
                    continue
                else:
                    one_mm['if_bed'] = 1
                    one_mm['my_url'].append('http://ww2.sinaimg.cn/large/'+ weibo_bed)
                print('http://ww2.sinaimg.cn/large/' + weibo_bed)
                os.rename(new, old)
                time.sleep(2)
            # 进入下一页
            pages = bf.find_all(id ='pages')
            #next_page = BeautifulSoup(str(pages[0])).find_all('a')
            next_page = bf.select('#pages > a')
            print(mm_avatar['href'])
            while (next_page[-1]['href'] + '/' != mm_avatar['href']):
                next_detail = 'https://www.nvshens.com' + next_page[-1]['href']
                next_res = requests.get(next_detail, headers = header)
                next_res.encoding = 'utf-8'
                next_bf = BeautifulSoup(next_res.text)
                next_detail_images = next_bf.select('#hgallery > img')
                for next_detail_image in next_detail_images:
                    # 保存到列表
                    one_mm['images_detail'].append(next_detail_image['src'])
                    # save到文件
                    print(next_detail)
                    request_image_header = {
                        'Referer': next_detail,
                    }
                    save = requests.get(next_detail_image['src'], headers = request_image_header)
                    image_name = ((next_detail_image['alt'].replace(' ', '')).replace('\\', '')).replace('/', '')
                    with open('images1/' + image_name + ".jpg", 'wb') as f:
                        f.write(save.content)
                        print('成功保存' + image_name)
                    # 因为sm.ms上传中文名出错所以重命名
                    old = os.path.join(os.getcwd(), 'images1/' + image_name + ".jpg")
                    new = os.path.join(os.getcwd(), 'images1/' + 'rename.jpg')
                    os.rename(old, new)
                    # 上传到图床
                    #smfile = open(new, 'rb')
                    #sm_post_data = {
                    #        'smfile' : smfile
                    #        }
                    #to_bed = requests.post(bed_url, files = sm_post_data) 
                    #print(to_bed.text)
                    #if to_bed.json()['code'] == 'success':
                    #    one_mm['my_url'].append(to_bed.json()['data']['url'])
                    #    one_mm['if_true'] = 1
                    #    print('成功保存到图床' + to_bed.json()['data']['url'])
                    #else:
                    #    one_mm['if_true'] = 0
                    #    one_mm['my_url'].append('')
                    #    if to_bed.json()['msg'].find('Upload file count limit') == 0 :
                    #         time.sleep(3600)
                    #smfile.close()
                    #os.rename(new, old)
                    #time.sleep(3)
                    # 微博图床
                    weibo_bed = weibo_image.to_weibo(new)
                    if weibo_bed is None:
                        one_mm['if_bed'] = 0
                        one_mm['my_url'].append('')
                        continue
                    else:
                        one_mm['if_bed'] = 1
                        one_mm['my_url'].append('http://ww2.sinaimg.cn/large/'+ weibo_bed)
                    print('http://ww2.sinaimg.cn/large/' + weibo_bed)
                    os.rename(new, old)
                    time.sleep(3)
                # 进入下一页
                pages     = next_bf.find_all(id  = 'pages')
                next_page = next_bf.select('#pages > a')
            mm_list.append(one_mm)
            mm.insert(one_mm)
        #mm.insert_many(mm_list)
    
mms = begin()
