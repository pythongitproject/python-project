#!/usr/bin/env python3
#coding=utf-8

import threading
import asyncio

@asyncio.coroutine
def hello():
    print('hello world! ( %s )' % threading.current_thread())
    yield from asyncio.sleep(1)
    print('hello again! (  %s )' % threading.current_thread())
#由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。
loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()



















