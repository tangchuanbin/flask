#!/usr/bin/python3
#coding = utf-8
from flask import Flask, jsonify, request
import db
import re
import sys
import hashlib
import xml.etree.ElementTree as ET
sys.path.append('wx_helper')
import msg as wx
app = Flask(__name__)

@app.route('/api/list/<int:cate>/<int:page>/<int:rand>')
def list(cate, page, rand):
    condition = {}
    key_word = request.values.get('key_word', 0)
    print(key_word)
    if key_word != 0 and cate == 4:
        print('enter condition.....')
        rgx = re.compile('.*' + key_word + '.*', re.IGNORECASE)
        condition = {"desc" :  rgx}
        print(condition)
    # 获取客户端IP
    #user_ip = request.remote_addr
    if cate is None:
        cate = 1
    if page is None:
        page = 1
    if rand is None:
        rand = 0
    mms = []
    select = {'name': 1, 'thumbnail': 1, 'my_url': 1, '_id': 0, 'width': 1, 'height': 1}
    sort_field = 'rand'
    sort_type  = -1
    if page == 1:
        limit = 20
    else:
        limit = 10
    if rand == 1:
        limit = 20
    mms = db.get_list(cate, select, condition, limit, page, sort_field, sort_type, rand)
    return jsonify(mms)

@app.route('/api/res', methods = ['GET', 'POST'])
def res():
    #以下代码通过token验证后注释即可
    #token = 'home'
    #timestamp = request.values.get('timestamp', 0)
    #nonce     = request.values.get('nonce', 0)
    #signature = request.values.get('signature', 0)
    #echostr   = request.values.get('echostr', 0)
    #
    #list = [token, timestamp, nonce]
    #list.sort()
    #list = ''. join(list)
    ###这里必须给他encode一把要不报错list.encode('utf8')
    #hashcode = hashlib.sha1(list.encode('utf8')).hexdigest()
    #if hashcode == signature:
    #    print(request.values)
    #    return echostr
    #else:
    #    return ""
    #exit()
    print(request.get_data().decode('utf-8'))
    xml_str = request.get_data()
    if len(xml_str) == 0:
        return ''
    xml_data     = ET.fromstring(xml_str)
    ToUserName   = xml_data.find('ToUserName').text
    FromUserName = xml_data.find('FromUserName').text
    CreateTime   = xml_data.find('CreateTime').text
    MsgType      = xml_data.find('MsgType').text
    #MsgId        = xml_data.find('MsgId').text
    if MsgType == 'event':
        Event        = xml_data.find('Event').text
        if Event == 'subscribe':
            text = "终于等到你，关注全网最新最全的斗图神器\r\n" + '你可以试着发送你想要搜素的关键词，我们公众号会随机给你推送十个图片链接，点击链接查看即可\r\n例如发送 熊本熊'
            data = {'ToUserName': FromUserName, 'FromUserName' : ToUserName, 'Content': text}
            res = wx.text_send(data)
            print(res)
            return res
            exit()
    else:
        Content      = xml_data.find('Content').text
        # 开始查询
        condition = {}
        key_word = Content
        cate = 4
        page = 1
        rand = 0
        if key_word != 0 and cate == 4:
            rgx = re.compile('.*' + key_word + '.*', re.IGNORECASE)
            condition = {"desc" :  rgx}
        lists = []
        select = {'name': 1, 'thumbnail': 1, 'my_url': 1, '_id': 0, 'width': 1, 'height': 1}
        sort_field = 'rand'
        sort_type  = -1
        if page == 1:
            limit = 10
        else:
            limit = 10
        if rand == 1:
            limit = 20
        lists = db.get_list(cate, select, condition, limit, page, sort_field, sort_type, rand)
        if len(lists['list']) == 0:
            text = '暂无该关键词的表情包,请重新换一个词。'
        else:
            text = "因为微信限制，个人公众号提供的上传图片空间有限，您可以点击如下链接选择需要的图片:\r\n"
            i = 0
            for one_list in lists['list']:
                i = i + 1
                text = text + str(i) + ':' + one_list['my_url'] + '\r\n'

        data = {'ToUserName': FromUserName, 'FromUserName' : ToUserName, 'Content': text}
        
        if MsgType  == 'text':
            res = wx.text_send(data)
            print(res)
            return res
        return ''
