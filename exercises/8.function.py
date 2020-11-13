"""函数的定义及调用"""
"""example 1"""
def make_a_sound():
    print("quack")
make_a_sound()

"""example 2 调用一个函数，使用if语句检查它的返回值"""
def agree():
    return True
if agree():
    print("Splendid")
else:
    print("That was unexpected")

"""example 3 调用一个含有输入参数的函数"""

def commentary(color):
    if color == "red":
        return "It's a tomato."
    elif color == "green":
        return  "It's a green pepper."
    elif color == "Bee purple":
        return "I don't know what it is,but only bees can see it"
    else:
        return "I've never heard of the color " + color +"."
print(commentary("Blue"))

"""函数调用时的位置参数，关键字参数:位置参数指的是函数调用时传入参数的值是按照顺序依次复制过去的 
                                     关键字参数指的是为避免位置参数带来的混乱， 调用函数时可以指
                                     定对应参数的名字，当位置参数与关键字参数同时出现时，首先应该
                                    考虑的是位置参数"""
def menu(a,b,c):
    print({a:"A",b:"B",c:"C"})
menu(1,2,3)#仅有位置参数
menu(b=1,c=2,a=3)#仅有关键字参数
menu(1,c=2,b=3)#位置参数、关键字参数同时存在


"""使用*，**收集关键字参数"""
def arg(*a):
    print("hello world",a)
arg(1,2,3,4,5,6)# *可以将一组可变数量的位置参数集合成参数值的元组

def arg_more(a,b,*c): #当函数同时有限定的位置参数的时候，*会收集剩下的参数
    print("hello world",a)
    print("hello world again",b)
    print("hello world third",c)
arg_more(1,2,3,4,5,6,7)

def kwargs(**x): # **可以将参数收集到一个字典中，参数的名字就是字典的键，对应
    print("hello world:",x)              #参数的值就是字典的值，x在函数内部是一个字典
kwargs(a = "A",b = "B",c="C")
