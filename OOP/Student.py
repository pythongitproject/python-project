#!/usr/bin/env python3
#coding=utf-8
#对象
#自定义的对象数据类型就是面向对象中的类（Class）的概念
#通常，如果没有合适的继承类，就使用object类
class Student(object):    #Student这种数据类型应该被视为一个对象
    def __init__(self,name,score):   #对象拥有name和score这两个属性（Property）
        self.name = name
        self.score = score
    def print_score(self):   #数据封装
        print('%s %s' % (self.name,self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

if __name__== '__main__':
    bart = Student('Bart Simpson', 59)  #实例（Instance）
    lisa = Student('Lisa Simpson', 87)
    bart.print_score()
    lisa.print_score()
    print(bart.get_grade())
