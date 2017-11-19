#!/usr/bin/env python3
#coding=utf-8
#操作文件和目录
import os
print(os.name) #获取操作系统类型
#print(os.uname()) #获取系统详细信息  #uname()函数在Windows上不提供

print(os.environ) #获取环境变量
print(os.environ.get('Path'))  #要获取某个环境变量的值

#查看当前目录的绝对路径
print('当前目录绝对路径 '+os.path.abspath('.'))
## 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
#os.path.join('E:\PycharmProjects\pytext\ioprogramme','testdir')
## 然后创建一个目录:
#os.mkdir('E:\\PycharmProjects\\pytext\\ioprogramme\\testdir')
#当前目录os.mkdir('testdir')
# 删掉一个目录:
#os.rmdir('E:\\PycharmProjects\\pytext\\ioprogramme\\testdir')

#拆分路径
#要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，
# 后一部分总是最后级别的目录或文件名
print(os.path.split('E:\\PycharmProjects\\pytext\\ioprogramme\\testdir'))
#os.path.splitext()可以直接让你得到文件扩展名
print(os.path.splitext('E:\\PycharmProjects\\pytext\\ioprogramme\\testdir\\tt.txt'))

#文件重命名
#os.rename('tt.txt','test.py')
#os.remove('test.py')

#列表生成式

#要列出当前目录下的所有目录
print(list(x for x in os.listdir('.') if os.path.isdir(x)))

#要列出所有的.py文件
print(list(y for y in os.listdir('.') if os.path.isfile(y) and os.path.splitext(y)[1]=='.py'))
