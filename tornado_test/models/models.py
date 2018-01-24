#/usr/bin/env python3
#coding=utf-8
from tornado_drawer.utils import db
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from sqlalchemy.orm import relationship

Base = db.getBase()

class UserInfo(Base):
    __tablename__ = 'userinfo'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20),nullable=False)
    telno = Column(String(20),nullable=False)
    pwd = Column(String(20),nullable=False)
    adddate = Column(DateTime,nullable=False)
    pts = relationship('Posts')

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('userinfo.id'),nullable=False)
    title = Column(String(50),nullable=False)
    content = Column(String(300),nullable=False)
    click_count = Column(Integer,nullable=False,default=0)
    like_count = Column(Integer,nullable=False,default=0)
    adddate = Column(DateTime,nullable=False)
    uinfo = relationship('UserInfo')
    clipost  = relationship('ClickPosts')

class ClickPosts(Base):
    __tablename__ = 'clickpost'
    id = Column(Integer, primary_key=True, autoincrement=True)
    postsid = Column(Integer,ForeignKey('posts.id'),nullable=False)
    user_id = Column(Integer,ForeignKey('userinfo.id'),nullable=False)
    adddate = Column(DateTime,nullable=False)
    pts = relationship('Posts')



#Base.metadata.drop_all(db.getEngine())
#Base.metadata.create_all(db.getEngine())