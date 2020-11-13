"""列表推导式"""
e2f = {
    "dog" : "chien" ,
    "cat" : "chat" ,
    "walrus" : "morse",
}
list1=[(m, n) for m,n in e2f.items() ]
list2=[(m,n) for m in e2f.keys() for n in e2f.values() ] #列表推导式中的嵌套子循环
print(list1,"\n",list2)


"""字典推导式"""
