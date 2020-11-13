x= "bugteacher.cn"
a,b,c=input("请输入起始位置"),input("请输入终点位置"),input("要替换的字符串")
a,b=int(a),int(b)
y=x[ :a-1]
z=x[b: ]
print(y+c+z)