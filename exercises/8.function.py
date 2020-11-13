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

