#!/usr/bin/python3
#coding = utf-8
import db
import requests
import io
from PIL import Image

def size(cate, page):
    if cate is None:
        cate = 1
    if page is None:
        page = 1
    mms = []
    condition = {}
    select = {'name': 1, 'thumbnail': 1, 'my_url': 1, '_id': 1}
    sort_field = 'rand'
    sort_type  = -1
    mms = db.get_list(cate, select, condition, 2000, page, sort_field, sort_type)
    for mm in mms:
        #print(mm['_id'])
        if 'my_url' not in mm.keys():
            continue
        try: 
            res = requests.get(mm['my_url'])
            if res.status_code != 200:
                continue
            tmpIm = io.BytesIO(res.content)
            im = Image.open(tmpIm)
            width = im.size[0]
            height = im.size[1]
            if width < 100 or height < 200:
                continue
            db.update_colum(cate, mm['_id'], width, height)
        except KeyError:
            print(1)
            continue
        except requests.exceptions.MissingSchema:
            print(2)
            continue

size(3, 1)
