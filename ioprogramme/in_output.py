#!/usr/bin/env python3
#coding=utf-8

#读文件
f = open('c:/test.txt','r')
print(f.read())
f.close()

#Python引入了with语句来自动帮我们调用close()方法
with open('c:/test.txt','r') as fk:
    print(fk.read())

#反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
with open('c:/test.txt','r') as kk:
    for line in kk.readlines():
        print(line.strip())    # 把末尾的'\n'删掉

#二进制文件(b)、字符编码(utf-8)、编码错误忽略、写文件
#valueerror:二进制模式并不需要一个编码参数
ff = open('c:/test.txt','w',encoding='utf-8',errors='ignore')
ff.write('in my heart for never be')

ff.close()