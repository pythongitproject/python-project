#!/usr/bin/env python3
#coding==utf-8
import os
from jinja2 import Template
def new():
    f = open(os.path.join('views','s1.html'),'r')
    data = f.read()
    f.close()
    return data

def index():
    return 'index'

def home():
    f = open(os.path.join('views','home.html'),'r')
    result = f.read()
    template = Template(result)
    #reder渲染模板
    data = template.render(name='linweili',user_list=['lin','weili'])
    return data