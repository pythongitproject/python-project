#/usr/bin/env python3
#coding=utf-8
from tornado_drawer.utils import db

Base = db.getBase()














Base.metadata.create_all(db.getEngine())