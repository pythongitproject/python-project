#!/usr/bin/env python3
#coding=utf-8
#Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，
# 对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
import time,threading

#新线程执行的代码



def loop():
    print('thread %s is running...' % threading.current_thread().name)
    print('zhixing')

print('thread %s is running....' % threading.current_thread().name)
t = threading.Thread(target=loop,name="LoopThread")
t.start()
t.join()
print('thread %s is ended.' % threading.current_thread().name)
print('------------------------')
#嘉定这是银行存款
balance = 0
#线程锁
lock = threading.Lock()


def chage_it(n):
    #先存后取，结果应该为0
    global balance
    balance =balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        #获取锁
        lock.acquire()
        try:
            chage_it(n)
        finally:
            #改完了释放锁
            lock.release()



t1 = threading.Thread(target=run_thread,args=(6,))
t2 = threading.Thread(target=run_thread,args=(9,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

#死循环
def loop1():
    x = 0
    while True:
        x = x*1
import multiprocessing
for i in range(multiprocessing.cpu_count()):
    tt = threading.Thread(target=loop1)
    tt.start()