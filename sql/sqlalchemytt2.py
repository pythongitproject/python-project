#/usr/bin/env python3
#coding=utf-8
#多对多

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import Integer,String,create_engine,Column,ForeignKey,Table
db_url = 'mysql+pymysql://root:123456a@127.0.0.1:3306/alchemy?charset=utf8'
engine = create_engine(db_url,echo=True)
Base = declarative_base(engine)
session = sessionmaker(engine)()

# 创建一个多对多的关系(老师与学生的关系)需要创建一个中间表
# 创建一个中间表
class Men_to_Women(Base):
    __tablename__ = 'men_to_women'
    id = Column(Integer,primary_key=True,autoincrement=True)
    men_id = Column(Integer,ForeignKey('men.id'))
    women_id = Column(Integer,ForeignKey('women.id'))

class Men(Base):
    __tablename__ = 'men'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20),nullable=False)

class Women(Base):
    __tablename__ = 'women'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20), nullable=False)

Base.metadata.create_all(engine)