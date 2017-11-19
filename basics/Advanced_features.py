#coding=utf-8
#高级特性11
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

#切片Slice
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#笨方法取前三个元素
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

print(L[0:3])   #从索引0开始取，直到索引3为止，但不包括索引3
print(L[:3])    #如果第一个索引是0，还可以省略
print(L[1:3])    #也可以从索引1开始，取出2个元素出来
print(L[-1])     #取倒数第一个元素
print(L[-2:])    #倒数切片
print(L[-2:-1])

#创建一个0-99的数列
F = list(range(100))
#前10个数
print(F[:10])
#后10个数
print(F[-10:])
#前11-20个数
print(F[10:20])
#前10个数，每两个取一个
print(F[:10:2])
#所有数，每5个取一个
print(F[::5])
#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print((0, 1, 2, 3, 4, 5)[:3])
#字符串切片
print('ABCDEFG'[:3])





