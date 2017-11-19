#coding=utf-8
#元组
t = ('a',1,2) #？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
print(t)
t1 = (1,)    #只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
print(t1)
t3 = ('a','b',['c','d'])
print(t3)
t3[2][0] = 'q'
t3[2][1] = 'q'
print(t3)