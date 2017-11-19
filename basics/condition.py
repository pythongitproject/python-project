#coding=utf-8
#条件判断
age = 7
if age>=18:    #如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
    print('you age is',age)
elif age<=6:
    print('your age is',-age)
else:
    print(age)

if age:  #只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
    print('True')