#!/usr/bin/env python3
#coding=utf-8
from tornado.web import UIModule

#模板对象
class custom(UIModule):
    def render(self, *args, **kwargs):
        return '1234'