#!/usr/bin/env python3
#coding=utf-8
#SQLAlchemy orm框架
from sqlalchemy import  create_engine
from  sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship


engine = create_engine("mysql+pymysql://root:123456a@127.0.0.1:3306/alchemy")
Base = declarative_base()

#创建单表
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(10))
    extra = Column(String(10))

    def __repr__(self):
        return "%s - %s - %s" % (self.id,self.name,self.extra)

# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
#增
# obj = Users(name='alex',extra ='kk')
# session.add(obj)
# session.add_all([
# Users(name='alex1',extra ='kk'),
# Users(name='alex2',extra ='kk')
# ])
#删
# session.query(Users).filter(Users.id > 2).delete()
#改
# session.query(Users).filter(Users.id == 1).update({"name":"666"})
#查
ret = session.query(Users).all()
print(ret)
ret1 = session.query(Users.name,Users.extra).all()
print(ret1)
ret2 = session.query(Users).filter_by(name = '666').all()
print(ret2)
ret3 = session.query(Users).filter_by(name = '666').first()
print(ret3)
# filters = {
#      Users.id <=2,
#      Users.name == 'kk'
# }
# ret4 = session.query(Users)\
#     .filter(*filters).order_by(Users.id).all()

ret4 = session.query(Users).filter("id<:value and name=:name").params(value=2,name='666').order_by(Users.id).all()
print(ret4)

ret5 = session.query(Users).from_statement("select * from users where name=:name").params(name='666').all()
print(ret5)


session.commit()