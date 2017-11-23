#!/usr/bin/env python3
#coding=utf-8
#我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
# 在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思
#序列化
import pickle
d = dict(name='bob',age=20)
print(pickle.dumps(d))   #pickle.dumps()方法把任意对象序列化成一个bytes
f = open('testdir/tt.txt','wb')
pickle.dump(d,f)   #pickle.dump()直接把对象序列化后写入一个file-like Object
f.close()

ff = open('testdir/tt.txt','rb')
dd = pickle.load(ff)  #从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象
print(dd)
ff.close()