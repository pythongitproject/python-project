#/usr/bin/env python3
#coding=utf-8
from tornado_drawer.utils import db
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from sqlalchemy.orm import relationship

Base = db.getBase()

class userinfo(Base):
    __tablename__ = 'userinfo'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20),nullable=False)
    telno = Column(String(20),nullable=False)
    pwd = Column(String(20),nullable=False)
    adddate = Column(DateTime,nullable=False)
    pts = relationship('posts')

class posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('userinfo.id'))
    title = Column(String(50),nullable=False)
    content = Column(String(100),nullable=False)
    click_cout = Column(Integer,nullable=False,default=0)
    like_count = Column(Integer,nullable=False,default=0)
    adddate = Column(DateTime,nullable=False)
    uinfo = relationship('userinfo')

#Base.metadata.drop_all(db.getEngine())
#Base.metadata.create_all(db.getEngine())