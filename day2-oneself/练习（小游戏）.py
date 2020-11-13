'''猜数字游戏：
（1）提示用户“猜数字游戏开始了”
（2）指定一个数字让用户来猜
（3）提示用户猜一个数字并获取用户猜的数字
（4）把用户猜的数字	和指定的数字进行比较
	如果猜对了，输入“恭喜你，猜对了，可惜没有奖励！”
	如果猜错了，输出“猜错了，正确答案是**”
（5）猜完以后输出“游戏结束了，不玩了！'''
# print("游戏已经开始了")
# x=8
# guss=int(input("猜猜我想的是什么数字？"))
# y="恭喜你猜对了，可惜没有奖励" if guss == 8 else "猜错了，正确答案是8"
# print(y, "   游戏已经结束了，不玩了  ")

# 优化猜数字游戏
# （1）猜错了提示用户，猜大了还是猜小了
# （2）用户可以有3次猜的机会
# （3）猜玩两次以后提示用户"还有最后一次机会"
# （4）使用random模块，里面有一个函数randint()，可产生一个随机数
# 	a、导入模块
# 	import random
# 	b、产生随机数
# 	key=random.randint(1,10)#参数的意思是产生一个1-10之间的随机数
import random
x=int(random.randint(1,10))
print("游戏已经开始了")
guss1=int(input("猜猜我想的是什么数字？"))
if guss1 == x:
    print( "恭喜你猜对了，可惜没有奖励")
elif guss1 < x:
    print("猜小了")
    guss2=int(input("第二次机会了，猜猜我想的是什么数字"))
    if guss2 == x:
        print( "恭喜你猜对了，可惜没有奖励")
    elif guss2 < x:
        print("猜小了")
        guss3=int(input("第三次机会了，猜猜我想的是什么数字"))
        if guss3==x:
            print("恭喜你猜对了，可惜没有奖励")
        else:
            print("猜错了，答案是",x)
    else :
        print("猜大了")
        guss3=int(input("第三次机会了，猜猜我想的是什么数字"))
        if guss3==x:
            print("恭喜你猜对了，可惜没有奖励")
        else:
            print("猜错了，答案是", x )
else:
    print("猜大了")
    guss2=int(input("第二次机会了，猜猜我想的是什么数字"))
    if guss2 == x:
        print("恭喜你猜对了，可惜没有奖励")
    elif guss2 >x:
        print("猜大了")
        guss3 = int(input("第三次机会了，猜猜我想的是什么数字"))
        if guss3==x:
            print("恭喜你猜对了，可惜没有奖励")
        else:
            print("猜错了，答案是", x )
    else:
        print("猜小了")
        guss3 = int(input("第三次机会了，猜猜我想的是什么数字"))
        if guss3 == x:
            print("恭喜你猜对了，可惜没有奖励")
        else:
            print("猜错了，答案是",x)

print("   游戏已经结束了，不玩了！  ")
