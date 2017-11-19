#coding=utf-8

#字符串
print('abc')
print("i'm ok!")        #如果'本身也是一个字符，那就可以用""括起来
print('i\'m \"ok\"')   #字符串内部既包含'又包含"怎么办？可以用转义字符\来标识
print('\\\n\\')
print(r'\\\t\\')  #如果字符串里面有很多字符都需要转义，
# 就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
print(r"\\\t\\")
print('''fsddddddddddddddd
sdfsdfsdf
dfsssssssssss''')
#布尔值
print(True)
print(False)
print(3>2)
print(True and False)
print(True or False)
#变量
age = 17;
if(age > 18 ):
    print(age)
else:
    print(-age)

a = 'abc'
b = a
a = 'fsdf'
print(b)
#常量
print(10/3) #除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：
print(10//3) #除法是//，称为地板除，两个整数的除法仍然是整数
print( 10 % 3) #无论整数做//除法还是取余数，结果永远是整数

print('中文')
print(len('ABC'))
print(len('中文'))