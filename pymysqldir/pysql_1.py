#!/usr/bin/env python3
#coding==utf-8

#pymysql操作mysql数据库

import pymysql
#创建连接
conn =  pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456a',db='test')
#创建游标,游标设置为字典类型
cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
#执行SQL并返回受影响条数
effect_row = cursor.execute('update funddetail set money=30.8')
print('effect_row: %s' % effect_row)

# 提交，不然无法保存新建或者修改的数据
conn.commit()

#执行SQL并返回受影响条数
effect_rows = cursor.execute('update funddetail set money=30.8 where nid > %s ',(0,) )
print('effect_rows: %s' % effect_rows)

cursor.execute('insert into funddetail(money,descs)VALUES (%s,%s)',(6.25,'fd'))
print('lastrowid: %s' % cursor.lastrowid)

#cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])

#获取查询数据
cursor.execute('select nid,money,descs from funddetail')
#获取第一条数据
row_1 = cursor.fetchone()
print(row_1)
#获取前两条数据
row_2 = cursor.fetchmany(2)
print(row_2)
#获取所有数据
row_all = cursor.fetchmany()
print(row_all)

#cursor.scroll(1,mode='relative')  # 相对当前位置移动
#cursor.scroll(2,mode='absolute') # 相对绝对位置移动




conn.commit()

#关闭游标
cursor.close()
#断开连接
conn.close()
