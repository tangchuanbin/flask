# 保存图片测试
import requests
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


