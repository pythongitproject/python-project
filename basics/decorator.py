#coding=utf-8
#装饰器
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2015-03-25')
#print(now.__name__)
now()

kk = log(now)
kk()


#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
import functools
def lognormal(text):
    def decorator(func):
        #需要把原始函数的__name__等属性复制到wrapper()函数中
        #Python内置的functools.wraps就是干这个事的
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('begin call')
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@lognormal('execute')
def forcast():
    print('2017-08-16')

forcast()

#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
def logger(text):
    if(isinstance(text,str)):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print('prog beginning')
                print('%s %s' % (text,func.__name__))
                func(*args,**kw)
                print('prog endding')
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('prog begging...')
            text(*args, **kw)
            print ('prog endding...')
        return wrapper


@logger('hello')
def test():
    print('2017-08-16')

test()















