#!/usr/bin/env python3
#coding=utf-8
#json类型
import json
d = dict(name='bob',age=20)
#dumps()方法返回一个str
print(json.dumps(d))
#要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
json_str = '{"name": "bob", "age": 20}'
print(json.loads(json_str))

#json进阶
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def Studentdict(std):
    return {'name':std.name,
            'age':std.age,
            'score':std.score}
s = Student('bob',20,88)
#Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
print(json.dumps(s, default=Studentdict))
#通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量
print(json.dumps(s,default=lambda obj: obj.__dict__))

#json反序列成对象
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

stt ='{"age":20,"name":"dd","score":80}'
print(json.loads(stt,object_hook=dict2student))
