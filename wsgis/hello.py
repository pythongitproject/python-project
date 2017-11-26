#!/usr/bin/env python3
#coding=utf-8

#实现web应用程序的wsgi处理函数

def application(environ, start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]