#!/usr/bin/env python3
#coding=utf-8

#摘要算法简介
import hashlib
md5 = hashlib.md5()
md5.update('linweili123'.encode('utf-8'))
print(md5.hexdigest())