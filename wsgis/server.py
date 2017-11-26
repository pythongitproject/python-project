#!/usr/bin/env python3
#coding=utf-8
#负责启动WSGI服务器，加载application()函数

#从wsgiref模块导入：
from wsgiref.simple_server import make_server
#导入我们自己编写的application函数
