#!/usr/bin/env python3
#coding=utf-8
#requests

import requests

r = requests.get('https://www.douban.com/') #访问豆瓣首页
print(r.status_code)
print(r.text)

#https://www.douban.com/search?cat=1002&q=雷神
param = {'cat':'1002','q':'雷神'}
m = requests.get('https://www.douban.com/search',params=param)
print(m.url)
print(m.encoding)
print(m.content)

#需要传入HTTP Header时，我们传入一个dict作为headers参数：
r1 = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r1.text)

#POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
rr = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(rr.status_code)

#requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
# params = {'key': 'value'}
# r = requests.post(url, json=params) # 内部自动序列化为JSON

#files上传文件
# upload_files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=upload_files)

#获取cookie
r.cookies['ts']

#传入cookie
# cs = {'token': '12345', 'status': 'working')
# r = requests.get(url, cookies=cs)

#r = requests.get(url, timeout=2.5) # 2.5秒后超时