#!/usr/bin/env python3
#coding=utf-8

#创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
class Student(object):
    pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self,age): ## 定义一个函数作为实例方法
    self.age = age

#为了给所有实例都绑定方法，可以给class绑定方法：
Student.set_age = set_age

from types import MethodType
s.set_age = MethodType(set_age,s)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print(s.age)


#给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
s2.set_age(20)
print(s2.age)

##限制实例属性  __slots__
#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Tea(object):
    __slots__ = ('name','age')  #用tuple定义允许绑定的属性名称

q = Tea()
q.name = 'dsfsd'
q.age = 25
q.score = 99