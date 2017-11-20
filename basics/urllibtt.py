#!/usr/bin/env python3
#coding=utf-8

#urllib
#get
from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s' % (k,v))
    print('Data:',data.decode('utf-8'))

#post
#如果要以post发送一个请求，只需要把参数data以bytes形式传入
from urllib import parse
print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([

])