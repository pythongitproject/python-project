#/usr/bin/env python3
#coding=utf-8
from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base

def getEngine():
    return create_engine("mysql+pymysql://root:123456a@127.0.0.1:3306/alchemy",echo = True)

def getBase():
    return declarative_base()