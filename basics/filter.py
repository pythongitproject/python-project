#coding=utf-8
#过滤序列/筛选
def is_odd(x):
    return x % 2 ==1
#删掉偶数，只保留奇数
print(list(filter(is_odd,[1,5,69,7,8])))

#去掉序列中
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['a','','b',None])))

def old_iters():
    n = 1
    while True:
        n = n + 1
        yield n

def filter_n(n):
    return lambda x: x % n >0

def primes():
    yield 2
    it = old_iters() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        print(n)
        it = filter(filter_n(n), it) # 构造新序列

for i in primes():
    if i < 1000:
        print(i)
    else:
        break
