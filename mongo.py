#!/usr/bin/python3
#coding=utf-8
# 测试连接mongodb
from pymongo import MongoClient
# 以下为三种建立连接的方式
client = MongoClient()
#client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017/')
# 以下是两种获取数据库的方式
db = client.test
#db = client['python-db']

# 以下是两种获取集合的方式
#collection = db.python_collection
#collection = db['python-collection']
mm = db.mm

# cat" : 1, "thumbnail" : "test", "images_detail" : [ "1.jpg", "2.jpg"  ]"
one_mm = {
        'cat': 1,
        'thumbnail': 'test',
        'images_detail': ['002.jpg', '009.jpg']
}
#mm.insert(one_mm)
res = mm.find_one({'thumbnail' : 'test'})

print(res is  not None)
