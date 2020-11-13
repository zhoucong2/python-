'''自定义一个函数，做两个数的加法运算，需要返回结果，然后调用函数，打印结果'''
def add(x,y):
    return x+y
if __name__ == '__main__':
    print(add(3,2))


# 练习2：自定义一个函数，求2个数值的最大值，并打印结果

def max(x,y):
    return  x if x>y else y
if __name__ == '__main__':
    print(max(4,2))


# 自定义一个函数，求20 ， 30 ， ‘a’, -1, 2.34 的平均值
def avg(x):
    list1 = []
    for i in x:
         if not isinstance(i,str) :
             list1.append(i)
    return sum(list1)/len(list1)
if __name__ == '__main__':
    tuble=[20,30,-1,'a',2.34]
    print(avg(tuble))




