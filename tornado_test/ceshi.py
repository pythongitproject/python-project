#!/usr/bin/env python3
#coding=utf-8

import requests

url = 'https://github.com/timeline.json'
params = {'stream':True}
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url=url,params=params,headers=headers)
print(r.url)
print(r.headers['Content-Type'])
print(r.json()['message'])
print(r.json().get('message'))
#print(r.json())
print(r.status_code)

#将文本流保存到文件
# with open('qq.txt','wb') as fs:
#     for chunk in r.iter_content():
#         fs.write(chunk)

# import json
# files = {'file':open('qq.txt','rb')}
# b = requests.post(url=url,files=files)
# r = requests.post(url=url,data=json.dumps(params),json=None,headers=headers)

#Cookie 的返回对象为 RequestsCookieJar，它的行为和字典类似，但界面更为完整，适合跨域名跨路径使用。
# 你还可以把 Cookie Jar 传到 Requests 中：
jar = requests.cookies.RequestsCookieJar()
jar.set('uid','yum',domain='httpbin.org', path='/cookies')
#禁用重定向
# allow_redirects=False
#响应超时时间
#timeout
# r1 = requests.get('http://httpbin.org/cookies', cookies=jar,timeout=0.001)
# print(r1.text)