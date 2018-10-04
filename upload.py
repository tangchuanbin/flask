#!/usr/bin/python3
#coding = utf-8
# 上传图片
import requests
import os
import codecs
url = 'https://sm.ms/api/upload'
#filepath = 'images1/test.jpg'
filepath = 'images1/日系童颜美女小纯子黑色蕾丝半透明学生_3.jpg'
#filepath = 'images1/a.jpg'
#filepath = u'images1/中文.jpg'
#filepath = 'images1/a.jpg'
#filepath = os.path.join(os.getcwd(), 'images1/日系童颜美女小纯子黑色蕾丝半透明学生_1.jpg')
#filepath = os.path.join(os.getcwd(), 'images1/中文.jpg')
#filepath = "images1/test.jpg"
#filepath = filepath.decode('utf8')
#filepath = os.path.normcase(filepath)

#files = open(filepath, 'rb')
#cp_file = open('images1/cp.jpg', 'wb')
#cp_file.write(files.read())
#files = open('images1/cp.jpg', 'rb')
old = os.path.join(os.getcwd(), filepath)
new = os.path.join(os.getcwd(), 'images1/rename.jpg')
os.rename(old, new)
files = open('images1/rename.jpg', 'rb')
post_data = {
        'smfile':files
}
res = requests.post(url , files = post_data)
files.close()
print(res.text)
print(res.json()['data']['url'])
os.remove(new)

