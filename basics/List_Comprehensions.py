#coding=utf-8
#列表生成式
L = []
for x in range(1, 11):  #生成[1x1, 2x2, 3x3, ..., 10x10]怎么做
    L.append(x * x)
print(L)
#列表生成式 要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
print(list(x * x for x in range(1, 11)))

#两层循环
print(list(m + n for m in 'ABC' for n in 'XYZ'))

#出当前目录下的所有文件和目录名
import os
print(list(d for d in os.listdir(".")))

#列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print(list(k + '=' + v for k, v in d.items()))

#把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple',99]
#使用内建的isinstance函数可以判断一个变量是不是字符串：
print(list(s.lower() for s in L if isinstance(s,str) ))

