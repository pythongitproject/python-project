#coding=utf-8
#递归函数
#尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
def kk(x,y):
    if x == 1:
        return y
    return kk((x-1),y)  #在函数调用前就会被计算，不影响函数调用

print(kk(1,2))
print(kk(3,2))