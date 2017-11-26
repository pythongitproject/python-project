#!/usr/bin/env python3
#coding=utf-8

#mysql连接数据库
import mysql.connector

conn = mysql.connector.connect(user='root',password='123456a',database='mysql')
cursor = conn.cursor()
cursor.execute('create table test (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into test (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)
cursor.close()
conn.commit()

cursor1 = conn.cursor()
cursor1.execute('select * from test where id = %s',('1',))
value = cursor1.fetchall()
print(value)
cursor1.close()
conn.close()