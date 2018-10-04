#!/usr/bin/python3
#coding = utf-8
from pymongo import MongoClient
from bson.objectid import ObjectId
import random

# 获取数据库连接
def get_collection(cate):
    if cate is None:
        cate = 1
    cat_map = {
        1 : 'new_mm1',
        2 : 'new_car_life',
        3 : 'view',
        4 : 'bq'
    }
    client = MongoClient()
    db = client.test #数据库
    #mm = db.mm1 #表
    if cate in cat_map.keys():
        collection = db[cat_map[cate]]
    else:
        collection = db['mm1']
    return collection   
# 查找
def get_list(cate = 1,select = None, condition = None, limit = 0, page = 0, sort_field = '_id', sort_type = -1, rand = 0):
    collection = get_collection(cate)
    if rand == 1:
        count = collection.find().count()
        count = int(count/limit)
        page = random.randint(2, count)
        
    list = []
    skip = limit * (page - 1)
    if sort_field is None:
        results = collection.find(condition, select).limit(limit).skip(skip).sort(sort_field, sort_type)
    else:
        results = collection.find(condition, select).limit(limit).skip(skip).sort(sort_field, sort_type)
    for result in results:
       list.append(result)
    lists = {
        'page' : page,
        'list' : list    
    }
    return lists
# 增加一个元素
def update_colum(cate,id, width, height):
    id = ObjectId(id)
    collection = get_collection(cate)
    if 'width' in (collection.find_one({'_id' : id})).keys():
        print('已有尺寸')
        return 0
        exit()
    #collection.update({'_id' : id}, {'$unset' : {'width': ''}})
    res = collection.update({'_id' : id}, {'$set' : {'width': width, 'height': height}})
    if res['ok'] == 1:
        print(str(id) + '修改尺寸成功')
    else:
        print(str(id) + '修改尺寸失败')

