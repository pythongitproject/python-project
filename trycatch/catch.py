#!/usr/bin/env python3
#coding=utf-8
#捕捉异常
try:
    print('try')
    r = 10 / 0
    print('result:',r)
except ZeroDivisionError as  e:
    print("except:",e)
finally:
    print('finally')
print('end')

try:
    print('try')
    q = 10 / int('2')
    print('result:',q)
except ValueError as e:
    print('valueerror:',e)
except ZeroDivisionError as  e:
    print('zerovalue:',e)
else:
    print('no error')
finally:
    print('finally')
print('end')

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')