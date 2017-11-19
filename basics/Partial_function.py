#coding=utf-8
#偏函数
print(int('12345', base = 10))   #如果传入base参数，就可以做N进制的转换
#转换大量的二进制字符串
def int2(x, base=2):
    return int(x, base)

print(int2('100000'))
import functools
max2 = functools.partial(max,10)
print(max2(11,5,6))