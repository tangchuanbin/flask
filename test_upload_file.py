# 上传图片测试
import requests

#获取微信access_token
def get_access_token():
    payload_access_token={
        'grant_type' : 'client_credential',
        'appid'      : 'wx909a4616af066eaf',
        'secret'     : '25001f12ab70a308115797ae964200e9'
    }
    token_url='https://api.weixin.qq.com/cgi-bin/token'
    r = requests.get(token_url,params=payload_access_token)
    dict_result = (r.json())
    return dict_result['access_token']

def upload():
    url = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=' + get_access_token()
    print(url)
    files = {'file': open("bq.jpg", 'rb')}
    res = requests.post(url, files = files)
    print(res.text)


upload()
exit()
url = 'https://t1.onvshen.com:85/gallery/26481/27580/s/001.jpg'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
header = {
        'User-Agent'                : user_agent,
        'Host'                      : 'www.nvshens.com',
        'Upgrade-Insecure-Requests' : 1
}

html = requests.get(url, headers = header)
with open('cha.jpg', 'wb') as f:
        f.write(html.content)


