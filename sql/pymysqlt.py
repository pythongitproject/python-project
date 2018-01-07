#!/usr/bin/env python3
#coding=utf-8

import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456a',db='houtai')
cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)

#执行存储过程
strsql = 'select * from module where mid > ?'
mnum = 2
cursor.callproc('pro_sql',(strsql,mnum))
#获取结果集
result = cursor.fetchall()

cursor.close()
conn.close()
print(result)