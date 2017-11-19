#coding=utf-8
#返回函数
def calc_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax + i
        return ax
    return sum
f = calc_sum(1,2,3,5,7,9)
#当lazy_sum返回函数sum时，
# 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”
print(f)      #返回的是求和函数，而不是求和结果
print(f())    #调用函数f时，才真正计算求和的结果


#闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
#返回函数不要引用任何循环变量，或者后续会发生变化的变量
f1, f2, f3 = count()
print(f1(), f2(), f3())
def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f4,f5,f6 = count1()
print(f4(),f5(),f6() )
