#!/usr/bin/env python3
#coding=utf-8
#继承和多态

class Animal(object):  #基类
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    #当子类和父类都存在相同的run()方法时，
    # 我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')

def run_twice(animal):
    animal.run()

class Timer(object):
    def run(self):
        print('Start...')

if __name__ == '__main__':
    Dog().run()
    run_twice(Animal())
    #多态
    #新增一个Animal的子类，不必对run_twice()做任何修改，
    # 实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态
    run_twice(Dog())
    #鸭子类型
    # 不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
    run_twice(Timer())
