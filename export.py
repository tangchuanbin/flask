#!/usr/bin/python3
#coding=utf-8
from pymongo import MongoClient
import random
client       = MongoClient()
db           = client.test
#这是汽车的
car_life     = db.car_life
new_car_life = db.new_car_life

#这是mm的
#car_life     = db.mm1
#new_car_life = db.new_mm1

list1        = car_life.find()

for list in list1:
    for url in list['my_url']:
        rand = random.randint(1, 100000)
        # 这是汽车的
        one_img = {
            'name'      : list['info'],
            'my_url'    : url,
            'rand'      : rand,
            'thumbnail' : list['thumbnail']
        }
        # 这是mm的
        #one_img = {
        #    'name' : list['name'],
        #    'my_url'  : url,
        #    'rand' : rand,
        #    'thumbnail' : list['thumbnail']
        #}
        new_car_life.insert(one_img) 

print('success')
