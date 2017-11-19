#!/usr/bin/env python3
#coding=utf-8
#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO

from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())  #getvalue()方法用于获得写入后的str

#要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取
ff = StringIO('hello!\nhi!\ngoodbye!')
while True:
    s = ff.readline()
    if s == '':
        break
    print(s.strip())

#BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes
from io import BytesIO
qq = BytesIO()
qq.write('中文'.encode('utf-8'))
print(qq.getvalue())











