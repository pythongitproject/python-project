#!/usr/bin/env python3
#coding==utf-8
from wsgiref.simple_server import make_server

from web.urls import urls

def run_server(environ, start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    url = environ['PATH_INFO']
    if url in urls.keys():
        ret = urls[url]
    else:
        ret = '404'
    return [ret.encode('utf-8')]

if __name__ == '__main__':
    httpd = make_server('',8000,run_server)
    httpd.serve_forever()
