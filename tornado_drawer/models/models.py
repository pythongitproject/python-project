#/usr/bin/env python3
#coding=utf-8
from tornado_drawer.utils import db
from sqlalchemy import Column,String,Integer,Date

Base = db.getBase()

class userinfo(Base):
    __tablename__ = 'userinfo'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20),nullable=False)
    telno = Column(String(20),nullable=False)
    pwd = Column(String(20),nullable=False)
    adddate = Column(Date,nullable=False)












#Base.metadata.drop_all(db.getEngine())
#Base.metadata.create_all(db.getEngine())