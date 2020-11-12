
y=["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
s=int(input("请输入数字"))
if s in range(1,8):
    print(y[s-1])
else:
    print("无效")
