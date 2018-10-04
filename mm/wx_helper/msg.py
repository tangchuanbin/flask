#!/usr/bin/python3
#coding = utf-8
import xml.etree.ElementTree as ET
import time

def text_send(d):
    data = dict()
    data['ToUserName']   = d['ToUserName']
    data['FromUserName'] = d['FromUserName']
    data['CreateTime']   = int(time.time())
    data['text']         = 'text'
    data['Content']      = d['Content']
    XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
	<Content><![CDATA[{Content}]]></Content>
        </xml>
        """
    return XmlForm.format(**data)

    
