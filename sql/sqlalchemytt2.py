#/usr/bin/env python3
#coding=utf-8
#多对多

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import Integer,String,create_engine,Column,ForeignKey,Table
db_url = 'mysql+pymysql://root:123456a@127.0.0.1:3306/alchemy?charset=utf8'
engine = create_engine(db_url,echo=True)
Base = declarative_base(engine)
Session = sessionmaker(engine)
session = Session()

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
    gf = relationship("Women", secondary=Men_to_Women.__table__)

class Women(Base):
    __tablename__ = 'women'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20), nullable=False)
    bf = relationship("Men",secondary = Men_to_Women.__table__)

# Base.metadata.create_all(engine)
# m1 = Men(name = 'lb')
# w1 = Women(name = 'wuq')
# w2 = Women(name = 'wuq1')
# session.add_all([m1,w1,w2])

# m1id = session.query(Men.id).filter_by(id='1')
# w1id = session.query(Women.id).filter_by(id='1')
# mw1 = Men_to_Women(men_id=m1id,women_id=w1id)
# session.add(mw1)

# m1 = session.query(Men).filter_by(id='2').first()
# w1 = session.query(Women).filter_by(id='1').all()
# m1.gf=w1
# session.add(m1)

session.commit()