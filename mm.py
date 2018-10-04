# 抓取www.nvshens.com网站图片
# 从https://www.nvshens.com/gallery/yazhou/ 这个亚洲分类开始抓取,首先抓取这个页面的头图和页数和每一个头像的详情页面
# 开始
from bs4 import BeautifulSoup
import requests
import os
from pymongo import MongoClient

client = MongoClient()
db = client.test
mm = db.mm

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
    # 定义列表
    url = 'https://www.nvshens.com/gallery/jiemeihua/'
    next_home_page_url = 'https://www.nvshens.com/gallery/jiemeihua/2.html'
    while ('https://www.nvshens.com/gallery/jiemiehua' != next_home_page_url):
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
            # 先拿出这一页的图片
            images = bf.select('#hgallery > img')
            for image in images:
                one_mm['images_detail'].append(image['src'])
                # save到文件
                save = requests.get(image['src'])
                image_name = ((image['alt'].replace(' ', '')).replace('\\', '')).replace('/', '')
                with open('images/' + image_name  + ".jpg", 'wb') as f:
                    f.write(save.content)
                    print('成功保存' + image_name)
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
                    save = requests.get(next_detail_image['src'])
                    image_name = ((next_detail_image['alt'].replace(' ', '')).replace('\\', '')).replace('/', '')
                    with open('images/' + image_name + ".jpg", 'wb') as f:
                        f.write(save.content)
                        print('成功保存' + image_name)
                # 进入下一页
                pages     = next_bf.find_all(id  = 'pages')
                next_page = next_bf.select('#pages > a')
            mm_list.append(one_mm)
 #       return mm_list

        mm.insert_many(mm_list)
    
mms = begin()
#mm.insert_many(mms)

