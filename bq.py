#!/usr/bin/python3
#coding = utf-8
import requests
import sys

sys.path.append('.')
import http.cookiejar as cookielib
from pymongo import MongoClient
import time
import weibo_image


client   = MongoClient()
db       = client.test
bq       = db.bq


my_session = requests.Session()
my_session.cookies = cookielib.LWPCookieJar(filename = 'bq_cookie.txt')

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
user_agent = 'Mozilla/5.0'
def get_cookie():
   # header = {
   #     'Accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
   #     'Accept-Encoding'           : 'gzip, deflate',
   #     'Accept-Language'           : 'zh-CN,zh;q=0.9',
   #     'Cache-Control'             : 'no-cache',
   #     'Connection'                : 'keep-alive',
   #     'Host'                      : 'image.bee-ji.com',
   #     'Pragma'                    : 'no-cache',
   #     'Upgrade-Insecure-Requests' : 1,
   #     'User-Agent': user_agent,
   #     'Referer': 'http://www.bee-ji.com/'
   # }
   # header = {
   #     'Accept'          : 'application/json',
   #     'Accept-Encoding' : 'gzip, deflate',
   #     'Accept-Language' : 'zh-CN,zh;q=0.9',
   #     'Cache-Control'   : 'no-cache',
   #     'Connection'      : 'keep-alive',
   #     'Content-Type'    : 'application/json',
   #     'Host'            : 'www.bee-ji.com',
   #     'Pragma'          : 'no-cache',
   #     'Referer'         : 'http: //www.bee-ji.com/',
   #     'User-Agent'      : user_agent,
   #     'Upgrade-Insecure-Requests': 1
   # }
    header1 = {
        'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate',
        'Accept-Language' : 'zh-CN,zh;q=0.9',
        'Cache-Control'   : 'no-cache',
        'Connection'      : 'keep-alive',
        'Host'            : 'www.bee-ji.com',
        'Upgrade-Insecure-Requests': 1,
        'Pragma'          : 'no-cache',
        'User-Agent'      : user_agent
    }
    header2 = {
        'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate',
        'Accept-Language' : 'zh-CN,zh;q=0.9',
        'Cache-Control'   : 'no-cache',
        'Connection'      : 'keep-alive',
        'Host'            : 'www.bee-ji.com',
        'Pragma'          : 'no-cache',
        'Upgrade-Insecure-Requests': 1,
        'User-Agent'      : user_agent,
        'Cookie' : 'Hm_lvt_65e796f34b9ee7170192209a91520a9a=1538198207; Hm_lpvt_65e796f34b9ee7170192209a91520a9a=1538198207'
    }
    #cookie ={'cookie': 'Hm_lvt_65e796f34b9ee7170192209a91520a9a=1538145350; Hm_lpvt_65e796f34b9ee7170192209a91520a9a=1538145411'}
    cookie = {'cookie' : 'Hm_lvt_65e796f34b9ee7170192209a91520a9a=1538149473; Hm_lpvt_65e796f34b9ee7170192209a91520a9a=1538149473'}
    cookie = {'cookie' : 'Hm_lvt_65e796f34b9ee7170192209a91520a9a=1538149473,1538151121; Hm_lpvt_65e796f34b9ee7170192209a91520a9a=1538151121'}
    cookie = {'cookie' : 'Hm_lvt_65e796f34b9ee7170192209a91520a9a=1538132611; ___rl__test__cookies=1538132844767; OUTFOX_SEARCH_USER_ID_NCOO=2048559860.108473; Hm_lpvt_65e796f34b9ee7170192209a91520a9a=1538196085'}
    cookie = {'cookie' : 'Hm_lvt_65e796f34b9ee7170192209a91520a9a=1538198207; Hm_lpvt_65e796f34b9ee7170192209a91520a9a=1538198207'}
    url = 'http://www.bee-ji.com/'
    #res = my_session.get(url, headers = header1)
   # res = requests.get(url, headers = header1)
   # print(res.cookies.get_dict())
   # exit()
   # my_session.cookies.save()
   # print(res.status_code)
   # my_session.cookies.load()
    url = 'http://www.bee-ji.com/data/search/json'
    res = requests.get(url, headers = header2)
    print(res.status_code)
    print(res.text)
   # while begin < end:
   #     url = 'http://image.bee-ji.com/' + begin
   # with open('bq.jpg', 'wb') as f:
   #     f.write(res.content)
    
#get_cookie()
def get():
   # header2 = {
   #     'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
   #     'Accept-Encoding' : 'gzip, deflate',
   #     'Accept-Language' : 'zh-CN,zh;q=0.9',
   #     'Cache-Control'   : 'no-cache',
   #     'Connection'      : 'keep-alive',
   #     'Host'            : 'www.bee-ji.com',
   #     'Pragma'          : 'no-cache',
   #     'Upgrade-Insecure-Requests': 1,
   # }
    header2 = {
        'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate',
        'Accept-Language' : 'zh-CN,zh;q=0.9',
        'Cache-Control'   : 'no-cache',
        'Connection'      : 'keep-alive',
        'Host'            : 'www.bee-ji.com',
        'Pragma'          : 'no-cache',
        'Upgrade-Insecure-Requests': 1,
        'User-Agent'      : user_agent,
        'Cookie' : 'Hm_lvt_65e796f34b9ee7170192209a91520a9a=1538198207; Hm_lpvt_65e796f34b9ee7170192209a91520a9a=1538198207'
    }
    begin = 1
    end = 5000
    while begin < end:
        begin = begin + 1
        url = 'http://www.bee-ji.com/data/search/json'
        res = requests.get(url, headers = header2)
        for one in res.json():
            one_bq = {}
            condition = {}
            condition['bq_id'] = one['id']
            if bq.find_one(condition) is not None:
                print(str(one['id']) + '已经存在')
                continue
            print(one['desc'])
            one_bq['bq_id'] = one['id']
            one_bq['width'] = one['width']
            one_bq['height'] = one['height']
            one_bq['desc'] = one['desc']
            
            header1 = {
                'Accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding'           : 'gzip, deflate',
                'Accept-Language'           : 'zh-CN,zh;q=0.9',
                'Cache-Control'             : 'no-cache',
                'Connection'                : 'keep-alive',
                'Host'                      : 'image.bee-ji.com',
                'Pragma'                    : 'no-cache',
                'Upgrade-Insecure-Requests' : 1,
                'User-Agent'                : user_agent,
                'Referer'                   : 'http: //www.bee-ji.com/'
            }
            url = 'http://image.bee-ji.com/' + str(one['id'])
            one_image = requests.get(url, headers = header1)
            if one_image.status_code != 200:
                continue
            image_name = one['desc']
            image_name = image_name.replace(' ', '').replace('-', '').replace('?', '').replace('!', '')
            image_name = 'bqs/' + image_name + '.jpg'
            try:
                with open(image_name, 'wb') as f:
                    f.write(one_image.content)
                    print('成功保存' + image_name)
            except OSError:
                continue

            # 微博图床
            weibo_bed = weibo_image.to_weibo(image_name)
            if weibo_bed is None:
                one_bq['if_bed'] = 0
                one_bq['my_url'] = ''
                continue
            else:
                one_bq['if_bed'] = 1
                one_bq['my_url'] = 'http://ww2.sinaimg.cn/large/'+ weibo_bed
            bq.insert(one_bq) 
            print('http://ww2.sinaimg.cn/large/'+ weibo_bed)
            time.sleep(3)
        
get()









