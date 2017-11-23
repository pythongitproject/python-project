#!/usr/bin/env python3
#coding=utf-8
#contextlib

class Query(object):
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')
    def query(self):
        print('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()


#@contextmanager

from contextlib import contextmanager
class Query1(object):
    def __init__(self,name):
        self.name = name
    def query1(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query1(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query1()






