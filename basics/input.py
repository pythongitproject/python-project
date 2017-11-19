#coding=utf-8
#input
s = input('birth:')
birth = int(s)   #input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数
if birth < 2000 :
    print('00前')
else:
    print('00后')