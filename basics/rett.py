#!/usr/bin/env python3
#coding=utf-8
#re正则表达式
#使用Python的r前缀，就不用考虑转义的问题

import re
test = '010-  123a'
if re.match(r'\d{3}\-\s+\d{3}\w$',test):
    print('ok')
else:
    print('bu ok')

print('a b  c'.split(' '))
print(re.split(r'\s+','a b  c'))
print(re.split(r'[\s\,\;]+','a,b;;  c'))

#分组
mm = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
#注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串
print(mm.group(0))
print(mm.group(1))
print(mm.group(2))

t = '19:05:30'
m1 = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m1.groups())

#贪婪匹配
print(re.match(r'^(\d+)(0*)$', '102300').groups())
#由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
print(re.match(r'^(\d+?)(0*)$', '102300').groups())