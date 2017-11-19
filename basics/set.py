#coding=utf-8
#set和dict类似，也是一组key的集合，但不存储value,无序
#自动过滤重复元素，自动排序
s = set([1,5,3,4,3])
print(s)
s.add(66)  #添加元素
print(s)
s.remove(66) #删除元素
print(s)
s1 = set([1,2,3])
print(s & s1) #查询两个set相同的元素
print(s | s1) #两个set并集

#list排序
a = ['c','b','d']
a.sort()
print(a)
#list替换
b = 'abc'
c = b.replace('a','A')
print(c)