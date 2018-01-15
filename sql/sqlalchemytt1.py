from msilib import type_nullable
from sqlalchemy import create_engine,Integer,String,Column
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey

#一对多
engine = create_engine("mysql+pymysql://root:123456a@127.0.0.1:3306/alchemy?charset=utf8",echo = True)
Base = declarative_base()

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer,primary_key = True,autoincrement=True)
    name = Column(String(10),nullable = False)
    # child = relationship('Child')
    # def __repr__(self):
    #     return '$s - %s' % (self.id,self.name)

class Child(Base):
    __tablename__ = 'child'
    cid = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(10),nullable=False)
    p_id = Column(Integer,ForeignKey("parent.id"))
    parent = relationship('Parent',backref = 'child')

# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
# p1 = Parent(name='699')
# c1 = Child(name='c1')
# c2 = Child(name='c2')
# p1.child = [c1,c2]
# session.add_all([p1,c1,c2])

# ret = session.query(Child).filter_by(cid=2).first()
# print(ret.name)
# print(ret.parent.name)
ret1 = session.query(Parent).filter_by(id=1).first()
c3 = Child(name='c3')
ret1.child.append(c3)
session.add(ret1)
session.commit()