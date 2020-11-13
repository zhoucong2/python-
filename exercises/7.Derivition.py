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
word = "letters"
letter_count = {letter:word.count(letter) for  letter in word}
print(letter_count)

"""集合推导式"""
a_set = {number for number in range(6) if number % 2 ==0}
print(a_set)


