#!/usr/bin/env python3
#coding=utf-8
#datatime是python处理日期和时间的标准库

from datetime import datetime
now = datetime.now()  #获取当前datatime
print(now)

dt = datetime(2017,11,16,23,59,59)
print(dt)

#timestamp转换未datetime

t = 1429417200.0
print(datetime.fromtimestamp(t))

#str 转换 datetime

cday =datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print(cday)

#datetime转换str
noww = datetime.now()
print(noww.strftime('%a, %b %d %H:%M'))

#datetime加减
from datetime import timedelta
print(noww+timedelta(hours=10))
print(noww-timedelta(days=1))
print(noww+timedelta(days=2,hours=12))