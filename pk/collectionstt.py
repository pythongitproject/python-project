#!/usr/bin/env python3
#coding=utf-8
#collections

#namedtuple
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p =Point(1,2)
print(p.x)
print(p.y)

#deque
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

#Counter
from collections import Counter
c = Counter()
for ch in 'programming':
    #Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次
    c[ch] = c[ch] + 1
print(c)