#coding=utf-8


#map
def g(x):   #调用map函数后，g（x）将会作用到列表的每个元素
    return 3 * x
l=map(g,[1,3,4,5,7,10])
print(list(l))

#reduce
#add（x,y）是我们定义的一个函数，将add函数和[1,2,3,4,6]列表传入reduce函数，
# 就相当于1+2+3+4+6 =16。即把结果继续和序列的下一个元素做累加。
#前一个结果作为下个x
from functools import reduce
def add(x,y): #定义一个相加函数
     return x+y
r = reduce(add,[1,2,3,4,6])
print(r)


def fun(x, y):  # 定义一个函数
    return 10 * x + y