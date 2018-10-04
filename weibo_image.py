#!/usr/bin/python3
#coding = utf-8
import requests
import base64
import re
import json


url = 'http://picupload.service.weibo.com/interface/pic_upload.php?mime=image%2Fjpeg&data=base64&url=0&markpos=1&logo=&nick=0&marks=1&app=miniblog'

cookie = {'cookies_are': 'SINAGLOBAL=8229730011315.093.1532845871069; _s_tentry=-; Apache=5630594756871.703.1537537719018; ULV=1537537719470:3:2:1:5630594756871.703.1537537719018:1537019561032; login_sid_t=dd258a5fa0aa71eb8ce558b78b7b1d11; cross_origin_proto=SSL; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhRzVZvOz_cVFBIO6.NEy0w5JpX5K2hUgL.Foz4S0nESo-pSo-2dJLoIpjLxKnLB-qL1hBLxKML1KBLBo-LxKnLBKML1hqt; ALF=1569229062; SSOLoginState=1537693063; SCF=AlDqAPifcJ7RLq4ulmNhwsy4sl2Vc8z50_zJWTfUErKNwmnHxK_h3zj8V93qpSKruyxHnQ4rSe64o2_mMtRXGSM.; SUB=_2A252oyXVDeRhGeRH7FoT9ivNzTmIHXVV2RAdrDV8PUNbmtANLW7YkW9NTYVFMXR7FGYyIklm9sQ_1SRC4wPttoI4; SUHB=0ft52FR07GDXMz; un=lltangchuanbin@live.com; wvr=6'}

cookie = {'cookies_are' : 'SINAGLOBAL=8229730011315.093.1532845871069; _s_tentry=-; Apache=5630594756871.703.1537537719018; ULV=1537537719470:3:2:1:5630594756871.703.1537537719018:1537019561032; login_sid_t=dd258a5fa0aa71eb8ce558b78b7b1d11; cross_origin_proto=SSL; UOR=,,login.sina.com.cn; SSOLoginState=1537693063; un=lltangchuanbin@live.com; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhRzVZvOz_cVFBIO6.NEy0w5JpX5KMhUgL.Foz4S0nESo-pSo-2dJLoIpjLxKnLB-qL1hBLxKML1KBLBo-LxKnLBKML1hqt; ALF=1569318158; SCF=AlDqAPifcJ7RLq4ulmNhwsy4sl2Vc8z50_zJWTfUErKNfAeCl-7VX-JINhAb-M4EagA-a_8DFJYHChHjIw2WE0k.; SUB=_2A252rMHfDeRhGeRH7FoT9ivNzTmIHXVV27QXrDV8PUNbmtAKLVHakW9NTYVFMRVRkDQsiswo36LF-R-Wa7OmZYa1; SUHB=0cS3BNgEOoU8I_'}
cookie = {'cookies_are': 'SINAGLOBAL=5418409871869.738.1491569259907; UM_distinctid=1628b16cdc71ce-0fb3b5a6c0b72f-50683974-100200-1628b16cdc81d1; _s_tentry=-; Apache=8515559757874.313.1537241976670; ULV=1537241977091:16:1:1:8515559757874.313.1537241976670:1532952273284; UOR=www.ikang.com,widget.weibo.com,www.dewen.net.cn; login_sid_t=670de8df03236e13c6db40e34e5ccb29; cross_origin_proto=SSL; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhRzVZvOz_cVFBIO6.NEy0w5JpX5K2hUgL.Foz4S0nESo-pSo-2dJLoIpjLxKnLB-qL1hBLxKML1KBLBo-LxKnLBKML1hqt; ALF=1569738645; SSOLoginState=1538202647; SCF=AsahgCOSIfl7onJKoCdD6-p4Cf2oPxhP1MqbdDepufUQTEuFwHkWpYq4sQSfKKXkVoBeYfpO7Z9fc0VTfj1crIM.; SUB=_2A252q2xHDeRhGeRH7FoT9ivNzTmIHXVVwdqPrDV8PUNbmtBeLWmikW9NTYVFMSkBZjyqCrxLA0Enf3ScBnLSB_4Z; SUHB=0ElKTl8zSnzXC6; un=lltangchuanbin@live.com; wvr=6'}
cookie = {'cookies_are' : 'SINAGLOBAL=8229730011315.093.1532845871069; un=lltangchuanbin@live.com; UOR=,,www.baidu.com; login_sid_t=9c2518882c39885b8a75ac3c891ad96e; cross_origin_proto=SSL; _s_tentry=-; Apache=8741998841440.375.1538306601237; ULV=1538306601245:5:4:1:8741998841440.375.1538306601237:1537970079352; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhRzVZvOz_cVFBIO6.NEy0w5JpX5K2hUgL.Foz4S0nESo-pSo-2dJLoIpjLxKnLB-qL1hBLxKML1KBLBo-LxKnLBKML1hqt; ALF=1569842621; SSOLoginState=1538306627; SCF=AlDqAPifcJ7RLq4ulmNhwsy4sl2Vc8z50_zJWTfUErKN_iyZIt0AQhZip9g5MPnQqnw-McBxPruR__huTEJ4Rr8.; SUB=_2A252tMITDeRhGeRH7FoT9ivNzTmIHXVVw7TbrDV8PUNbmtANLRDSkW9NTYVFMYhsaNXFD_U7jQb6GEchCAb2R7eK; SUHB=0cS3BNgEOoW4us; wvr=6'}
cookie = {'cookies_are' : 'SINAGLOBAL=8229730011315.093.1532845871069; un=lltangchuanbin@live.com; UOR=,,www.baidu.com; login_sid_t=9c2518882c39885b8a75ac3c891ad96e; cross_origin_proto=SSL; _s_tentry=-; Apache=8741998841440.375.1538306601237; ULV=1538306601245:5:4:1:8741998841440.375.1538306601237:1537970079352; SSOLoginState=1538306627; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhRzVZvOz_cVFBIO6.NEy0w5JpX5K2hUgL.Foz4S0nESo-pSo-2dJLoIpjLxKnLB-qL1hBLxKML1KBLBo-LxKnLBKML1hqt; ALF=1569984989; SCF=AlDqAPifcJ7RLq4ulmNhwsy4sl2Vc8z50_zJWTfUErKNUovUawFJ7eLqd19XAtTTMdxgmKaB8QrYs21BgmpTpq4.; SUB=_2A252tq4ODeRhGeRH7FoT9ivNzTmIHXVVxZjGrDV8PUNbmtAKLXbWkW9NTYVFMW7hkc4KzZv7BUEKqdvHrd2V_aYB; SUHB=0S7Si96WB1MY-R'}
cookie = {'cookies_are' : 'SINAGLOBAL=8229730011315.093.1532845871069; un=lltangchuanbin@live.com; login_sid_t=9c2518882c39885b8a75ac3c891ad96e; cross_origin_proto=SSL; _s_tentry=-; Apache=8741998841440.375.1538306601237; ULV=1538306601245:5:4:1:8741998841440.375.1538306601237:1537970079352; SSOLoginState=1538306627; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhRzVZvOz_cVFBIO6.NEy0w5JpX5KMhUgL.Foz4S0nESo-pSo-2dJLoIpjLxKnLB-qL1hBLxKML1KBLBo-LxKnLBKML1hqt; ALF=1570071714; SCF=AlDqAPifcJ7RLq4ulmNhwsy4sl2Vc8z50_zJWTfUErKNpl_5uAKTkI3xhPwNpRQ0AVxN6fH_llq55R70CVXtuzw.; SUB=_2A252sEF1DeRhGeRH7FoT9ivNzTmIHXVVxDW9rDV8PUNbmtAKLUntkW9NTYVFMVuZlUaMMnMPyfBBnMErgqU2rtqy; SUHB=0S7Si96WB1M-Px; UOR=,,login.sina.com.cn'}
cookie = {'cookies_are' : 'SINAGLOBAL=8229730011315.093.1532845871069; un=lltangchuanbin@live.com; login_sid_t=9c2518882c39885b8a75ac3c891ad96e; cross_origin_proto=SSL; _s_tentry=-; Apache=8741998841440.375.1538306601237; ULV=1538306601245:5:4:1:8741998841440.375.1538306601237:1537970079352; SSOLoginState=1538306627; wvr=6; UOR=,,login.sina.com.cn; SCF=AlDqAPifcJ7RLq4ulmNhwsy4sl2Vc8z50_zJWTfUErKNBUdY25QrquoYEvOs5xN9YKmWORjVohH4qU5ZkLBhAlE.; SUB=_2A252sfM2DeRhGeRH7FoT9ivNzTmIHXVVx2P-rDV8PUJbmtAKLUzCkW9NTYVFMWsbmYPJGkDkULQ1PCvVjmwQB8BW; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhRzVZvOz_cVFBIO6.NEy0w5JpX5K-hUgL.Foz4S0nESo-pSo-2dJLoIpjLxKnLB-qL1hBLxKML1KBLBo-LxKnLBKML1hqt; SUHB=0YhBguEwIsZLkV; ALF=1570158305'}
#filepath = 'images1/rename.jpg'
#with open(filepath, 'rb') as f:
#    base64_data = base64.b64encode(f.read())
#
#post_data  = {
#        'b64_data' : base64_data
#    }
#res = requests.post(url, data = post_data, cookies = cookie)
#print(res.text)
# result
#{"code":"A00006","data":{"count":1,"data":"eyJ1aWQiOjI5NzgyNjUxNjUsImFwcCI6Im1pbmlibG9nIiwiY291bnQiOjEsInRpbWUiOjE1Mzc2OTc2ODEuMTM2LCJwaWNzIjp7InBpY18xIjp7IndpZHRoIjoxMDAwLCJzaXplIjoxMTM2NjEsInJldCI6MSwiaGVpZ2h0IjoxNTAwLCJuYW1lIjoicGljXzEiLCJwaWQiOiJiMTg0Yjg0ZGx5MWZ2am4yYzRsdHZqMjByczE1bzB2aiJ9fX0=","pics":{"pic_1":{"width":1000,"size":113661,"ret":1,"height":1500,"name":"pic_1","pid":"b184b84dly1fvjn2c4ltvj20rs15o0vj"}}}}

def to_weibo(filepath):
    with open(filepath, 'rb') as f:
        base64_data = base64.b64encode(f.read())
    post_data  = {
        'b64_data' : base64_data
    }
    try:
        res = requests.post(url, data = post_data, cookies = cookie)
        f.close()
        if res.status_code == 200:
            index = res.text.find('{')
            sub   = res.text[index:]
            result = json.loads(sub) 
            val = result['data']['pics']['pic_1']['pid']
        else :
            val = None
    except IOError:
        print(0)
        val = None
    except SyntaxError:
        print(1)
        val = None
    except IndexError:
        print(2)
        val = None
    except ValueError as e:
        print(3)
        val = None
    except KeyError:
        print(4)
        val = None
    return val; 


def test():
    test = '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><script type="text/javascript">document.domain="sina.com.cn";</script>{"code":"A00006","data":{"count":1,"data":"eyJ1aWQiOjI5NzgyNjUxNjUsImFwcCI6Im1pbmlibG9nIiwiY291bnQiOjEsInRpbWUiOjE1Mzc2OTg2MDguMDYyLCJwaWNzIjp7InBpY18xIjp7IndpZHRoIjoxMDAwLCJzaXplIjoxMTM2NjEsInJldCI6MSwiaGVpZ2h0IjoxNTAwLCJuYW1lIjoicGljXzEiLCJwaWQiOiJiMTg0Yjg0ZGx5MWZ2am5pZXNkeGZqMjByczE1bzB2aiJ9fX0=","pics":{"pic_1":{"width":1000,"size":113661,"ret":1,"height":1500,"name":"pic_1","pid":"b184b84dly1fvjniesdxfj20rs15o0vj"}}}}'
    #m = re.match('{', test)
    #m = re.findall(r'/({.*)/i})', test)
    print(test.find('{'))
    index = test.find('{')
    print(test[index:].json()['code'])
    

