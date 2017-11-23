#coding=utf-8
#列表
classmates = ['d','b','a']
print(classmates)
print(len(classmates)) #获取list个数
print(classmates[0]) #第一个
print(classmates[-1]) #最后一个
classmates.append('d') #追加元素到末尾
print(classmates)
classmates.insert(1,'q') #把元素插入到指定的位置
print(classmates)
classmates.pop() #删除list末尾的元素
print(classmates)
classmates.pop(1) #删除第二个
print(classmates)
classmates[1] = 'Sarah' #替换第二个
print(classmates)
p = [1,2]
classmates.append(p) #list中包含list
print(classmates)
print(classmates[3][1]) #可以看成是一个二维数组

