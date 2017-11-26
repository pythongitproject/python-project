#!/usr/bin/env python3
#coding=utf-8

#sqlalchemy
# from sqlalchemy import Column, String , create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# #创建对象的基类
# Base = declarative_base()
# class Student(Base):
#     __tablename__ = 'student'
#     #表的结构
#     id = Column(String(20),primary_key=True)
#     name = Column(String(20))
#
# engine = create_engine('mysql+mysqlconnector://root:123456a@localhost:3306/mysql')
# #创建DBsession类型
# DBsession = sessionmaker(bind=engine)
# #由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个Student对象：
# #创建session对象
# session = DBsession()
# #创建新student对象
# new_stu = Student(id='5',name='Amy')
# #添加到session
# session.add(new_stu)
# #提交保存到数据库
# session.commit()
# #断开连接
# session.close()
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Student(Base):
    # 表的名字:
    __tablename__ = 'student'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql://root:123456a@localhost:3306/mysql')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_stu = Student(id='5', name='Bob')
# 添加到session:
session.add(new_stu)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()