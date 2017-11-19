#!/usr/bin/env python3
#coding=utf-8
#多进程
import os
print('process (%s) start...' % os.getpid())


#有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，
# 每当有新的http请求时，就fork出子进程来处理新的http请求
#因为fork这个系统命令，只在linux中才有用
# psid = os.fork()
# if psid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))

#multiprocessing模块就是跨平台版本的多进程模块(支持linux/unitx/windows)

from multiprocessing import Process
import os

#子模块
def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    #创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单
    p = Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    print('Child process end')























