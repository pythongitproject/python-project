#!/usr/bin/env python3
#coding=utf-8

#当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')
# 来尝试获得属性，这样，我们就有机会返回score的值
class Student(object):
    def __init__(self,name):
        self.name = name
    def __getattr__(self, item):
        if item =='score':
            return 99

s = Student('lin')
print(s.name)
print(s.score)
