#!/usr/bin/env python3
#coding=utf-8

#sqllite(内置在python标准库中)
import sqlite3
conn = sqlite3.connect('test.db') #若不存在则自动创建
#创建游标cursor
cursor = conn.cursor()
#创建用户表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#执行插入语句
cursor.execute(r"insert into user (id, name) values ('1', 'Michael')")
print(cursor.rowcount)  #获取插入条数
cursor.close()  #关闭游标
conn.commit()   #提交事务
conn.close()    #断开连接
conn1 = sqlite3.connect('test.db')
cursor1 = conn1.cursor()
cursor1.execute('select * from user where id=?', ('1',))
value = cursor1.fetchall()
print(value)
cursor1.close()
conn1.close()
conn2 = sqlite3.connect('test.db')
cursor2 = conn2.cursor()
cursor2.execute('select * from user where id=? and name=?', ('1', 'Michael'))
value2= cursor2.fetchall()
print(value2)
cursor2.close()
conn2.close()