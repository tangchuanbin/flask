#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import http.cookiejar as cookielib
# 代表requests的抹一次连接
phi_session = requests.session()
# # 因为原始的session.cookies 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法
phi_session.cookies = cookielib.LWPCookieJar(filename = 'phi_cookie.txt')
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
header     = {
        'User-Agent': user_agent
}
def login(name, password): 
        print('开始登录')
        url = 'https://mall.phicomm.com/passport-post_login.html'
        post_data = {
            'uname'    : name,
            'password' : password
        }
        res = phi_session.post(url, data = post_data, headers = header)
        res.enconding = 'utf-8'
        phi_session.cookies.save()

def if_login():
    print('检测是否登录')
    url = 'https://mall.phicomm.com/index.php/openapi/orders/count'
    res = phi_session.post(url, headers = header)
    if str(res.json()['data']['mem']['account']) == 'None':
        return False
    else:
        return True
def get_order():
    phi_session.cookies.load()
    if if_login() == False:
        print('cookie失效正在重新登录')
        login('15666987950', 'aiyishe05')
    url1 = 'https://mall.phicomm.com/index.php/openapi/orders/count'
    res = phi_session.post(url1, headers = header)
    account = str(res.json()['data']['mem']['account'])

    print('当前登录账号是：' + account)
def do_buy():
    # 斐讯商城member_id : 3040533
    phi_session.cookies.load()
    if if_login() == False:
        print('cookie失效正在重新登录')
        login('15666987950', 'aiyishe05')
    url1 = 'https://mall.phicomm.com/index.php/openapi/orders/count'
    post_data = {
        'cart_md5'   : 'a30d6925424ad25882c35179dd2a4077',
        'ddr_id'     : 377710,
        'dlytype_id' : 1,
        'payapp_id'  : 'alipay',
        'useVcNum'   : 0,
        'useDdwNum'  : 0,
        'vcode'      : '5555'
        
    } 
    res = phi_session.post(url1, data = post_data , headers = header)
get_order()
