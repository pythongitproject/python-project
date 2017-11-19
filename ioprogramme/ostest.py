#!/usr/bin/env python3
#coding: utf-8
#获取包含当前输入字符的文件的相对路径

import os

keyword = input('Input keyword: ')
up = '.'
result = []

def check(up, keyword):
    all = os.listdir(up)
    for x in all:
        try:
            abs_x = os.path.join(up, x)
            if os.path.isdir(abs_x):
                up = os.path.join(up, x)
                check(up, keyword)
                up = os.path.split(up)[0]
            if os.path.isfile(abs_x):
                if keyword in x:
                    result.append(abs_x)
        except:
            continue


check(up, keyword)
print('\n==========Find %d files==========\n' % len(result))
num = 0
for r in result:
    num += 1
    print('%d  %s' % (num, r))
print('\n===============END===============\n')