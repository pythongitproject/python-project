#coding=utf-8
#字典：dict的支持，dict全称dictionary，其他语言中也称为map，使用键-值（key-value）存储
d = {'aa':12,'bb':33}
print(d)
print(d['aa'])
d['aa']=66
print(d['aa'])
d['aa']=77
print(d['aa'])   #多次对一个key放入value，后面的值会把前面的值冲掉
print(d.get('aa'),-1)  #如果key不存在，可以返回None，或者自己指定的value
d.pop('bb')  #删除一个key
print(d)
#无序