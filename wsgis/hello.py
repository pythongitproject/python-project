#!/usr/bin/env python3
#coding=utf-8

#实现web应用程序的wsgi处理函数

def application(environ, start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    return [b'<h1>Hello,web!</h1>']