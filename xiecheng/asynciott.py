#!/usr/bin/env python3
#coding=utf-8

#asyncio的编程模型就是一个消息循环。
# 我们从asyncio模块中直接获取一个EventLoop的引用，
# 然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO
import asyncio

#async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换
#把@asyncio.coroutine替换为async；
#把yield from替换为await。

#@asyncio.coroutine
async def hello():
    print('hello asyncio')
    #异步调用asyncio.sleep(1)
    #r = yield from asyncio.sleep(1)
    r = await asyncio.sleep(1)
    print('hello again')

#获取Eventloop
loop = asyncio.get_event_loop()
#执行coroutine
loop.run_until_complete(hello())
loop.close()
