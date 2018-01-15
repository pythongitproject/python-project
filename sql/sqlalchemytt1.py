from msilib import type_nullable

from sqlalchemy import create_engine,Integer,String,Column
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey

engine = create_engine("mysql+pymysql://root:123456a@127.0.0.1:3306/alchemy",echo = True)
Base = declarative_base()

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer,primary_key = True,autoincrement=True)
    name = Column(String(10),nullable = False)
    # def __repr__(self):
    #     return '$s - %s' % (self.id,self.name)

class Child(Base):
    __tablename__ = 'child'
    cid = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(10),nullable=False)
    p_id = Column(Integer,ForeignKey("parent.id"))

# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
p1 = Parent(name='668')

session.add(p1)

session.commit()