#!/usr/bin/env python3
#coding=utf-8

#为了限制score的范围，可以通过一个set_score()方法来设置成绩，
# 再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value >100:
            raise ValueError('score must between 0~100')
        self._score = value

s = Student()
s.set_score(60)
print(s.get_score())

#s.set_score(9999)

class Student2(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

b = Student2()
b.birth = 66
print(b.birth)
b.birth = 122

class Animal(object):
    pass
class Mammal(Animal):
    pass
class RunnableMixIn(object):
    def run(self):
        print('Running...')

class CarnivorousMixIn(object):
    def fly(self):
        print('Flying...')
##多重继承
#在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass