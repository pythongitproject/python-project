#coding=utf-8
#函数
a = -101
#绝对值
print(abs(a))
# 多个参数返回最大值
print(max(2,3,-9,0))

#数据类型转换
print(int('123'))   #转换为整数
print(float('12.58'))  #转换为浮点数
print(str(123))    #转换为字符串
print(bool(1))  #输出bool值True
print(bool('')) #输入bool值False

aa = abs  #变量aa指向abs函数
print(aa(-1))

#定义函数
def myabs(x):
    if x>0:
        return x
    else:
        return -x

print(myabs(-5))

age =18
if age>=18:
    pass

def myabs2(z):

#对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现
    if not isinstance(z,(int,float)):
        raise TypeError('bad operand type')
    if z >= 0:
        return z
    else:
        return -z

#print(myabs2('-2'))

#返回多个值
import math
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y -step*math.sin(angle)
    return nx,ny

def power(x,n):
    s = 1
    while n>0:
        n = n-1
        s = s * x
    return s

print(power(5,3))

def add_end(L=None):
    if L is None:  #定义默认参数要牢记一点：默认参数必须指向不变对象
        L = []
    L.append('END')
    return L

#可变参数
#定义可变参数和定义一个list或tuple参数相比，
#仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple
def manyargs(*numbers):
    sum = 0
    for i in numbers:
        sum = sum +i*i
    return sum

print(manyargs())
print(manyargs(2,3,4))
nums = [1,2,3]
print(manyargs(nums[0],nums[1],nums[2]))
print(manyargs(*nums))

#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，
# 这些关键字参数在函数内部自动组装为一个dict
def person(x,y,**kw):
    print('x:', x, 'y:', y, 'other:', kw)
print(person('a','b'))
print(person('a','b',city='beijing'))
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, city=extra['city'], job=extra['job']))

def nb(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

print(nb('lin',9,city=6))

#命名关键字
#命名关键字参数必须传入参数名，这和位置参数不同,*后面的参数被视为命名关键字参数
def pers(name, age, *, city='Beijing', job): #命名关键字参数可以有缺省值，从而简化调用
    print(name, age, city, job)

print(pers('dd',55,job='ds'))

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

#通过一个tuple和dict，你也可以调用上述函数：
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
print(f1(*args, **kw))





















