#coding=utf-8
#循环
names = ['a','b','c']
for name in names:      #for...in循环，依次把list或tuple中的每个元素迭代出来
    print(name)

sum = 0
for i in [1,2,3,4,5,6,7,8,9]:
    sum = sum + i
print(sum)

print(list(range(5))) #range(5)生成的序列是从0开始小于5的整数

sum1 = 0
for i in range(101):
    sum1 = sum1 + i
print(sum1)

#while循环 计算100以内所有奇数之和
sum = 0
n = 99
while n>0:
    sum = sum + n
    n = n - 2
print(sum)

#break
q = 1
while q <= 100:
    if q>10:
        break
    print(q)
    q = q + 1
print('end')

#continue
z = 0
while z < 10:
    z = z +1
    print(z)
