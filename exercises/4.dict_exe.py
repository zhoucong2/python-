pythons = {
    "chapman" : "graham",
    "cleese" : "john",
    "gilliam" : "teddy",
    "idle" : "eric",
    "jones" : "terry",
    "palin" : "michael"
}
others = {
    "marx" : "groucho",
    "howard" : "moe"
}
pythons.update(others)#update()用来合并字典，也可以修改字典
print(pythons)
del pythons["marx"]#del 用来删除具有指定键的元素
print(pythons)
a = pythons.keys()#keys()用来获取所有的键
b = pythons.values()#values()用来获取所有的值
c = pythons.items()#items()用来获取所有值对
print(a)
print(b)
print(c)
