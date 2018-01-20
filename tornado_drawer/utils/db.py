#/usr/bin/env python3
#coding=utf-8
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 连接数据库的数据

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'boot'
USERNAME = 'root'
PASSWORD = '123456a'

# DB_URI的格式：dialect（mysql/sqlite）+driver://username:password@host:port/database?charset=utf8

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

def getEngine():
    return create_engine(DB_URI,echo = True)

def getBase():
    return declarative_base()

def getSession():
    engine = getEngine()
    Session = sessionmaker(engine)
    return Session()
