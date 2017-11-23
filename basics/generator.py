#coding=utf-8
#生成器and 生成器
#第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))
for n in g:    #正确的方法是使用for循环，因为generator也是可迭代对象
    print(n)

#迭代器
list = [1,2,3,4]
it = iter(list)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素
for x in it:
    print(x,end=" ")

# import sys
# ls = [1,2,3,4]
# it = iter(ls)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

for x in [1,2,3,4]:
    print(x)

it = iter([6, 7, 8, 9, 10])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

