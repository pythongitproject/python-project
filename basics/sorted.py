#coding=utf-8
#排序sorted
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
print(sorted([1,-10,-20,30,9],key=abs))
#忽略大写，反向
print(sorted(['bob','about','Zoo','Cra'],key=str.lower,reverse=True))
from operator import itemgetter
students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#分别按名字排序
print(sorted(students, key=itemgetter(0)))
#按成绩从高到低排序
print(sorted(students, key=lambda t: t[1],reverse=True))
print(sorted(students, key=itemgetter(1), reverse=True))
