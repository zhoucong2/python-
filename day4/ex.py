'''
统计： 函数的调用执行时间
'''
import time
def bussiness(fn):
    def inner():
        start_time = time.time()
        fn()
        end_time = time.time()
        print(end_time-start_time)
    return  inner
@bussiness
def foo1():
    print("------执行业务操作1-----")
    time.sleep(1)
    pass
@bussiness
def foo2():
    print("------执行业务操作2-----")
    time.sleep(3)
    pass
if __name__ == '__main__':
    foo1()
    foo2()