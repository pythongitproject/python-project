#!/usr/bin/env python3
#coding=utf-8
import threading

#创建全局ThreadLocal对象
#你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，
# 可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
local_school = threading.local()

def process_student():
    #获取当前线程关联的student
    std = local_school.student
    print('hello %s (in %s)' % (std,threading.current_thread().name))

def process_thread(name):
    #绑定threadlocal的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=('Alice',),name='thread-a')
t2 = threading.Thread(target=process_thread,args=('bob',),name='thread-b')
t1.start()
t2.start()
t1.join()
t2.join()