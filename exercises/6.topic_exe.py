'''
(1) 创建一个叫作 years_list 的列表，存储从你出生的那一年到五岁那一年的年份。例
如，如果你是 1980 年出生的，那么你的列表应该是 years_list = [1980, 1981, 1982,
1983, 1984, 1985]。
如果你现在还没到五岁却在阅读本书，那我真的没有什么可教你的了。
(2) 在 years_list 中，哪一年是你三岁生日那年？别忘了，你出生的第一年算 0 岁。
(3) 在 years_list 中，哪一年你的年纪最大？
(4) 创建一个名为 things 的列表，包含以下三个元素："mozzarella"、"cinderella" 和
"salmonella"。
(5) 将 things 中代表人名的字符串变成首字母大写形式，并打印整个列表。看看列表中的
元素改变了吗？
(6) 将 things 中代表奶酪的元素全部改成大写，并打印整个列表。
(7) 将代表疾病的元素从 things 中删除，收好你得到的诺贝尔奖，并打印列表。
(8) 创建一个名为 surprise 的列表，包含以下三个元素："Groucho"、"Chico" 和 "Harpo"。
(9) 将 surprise 列表的最后一个元素变成小写，翻转过来，再将首字母变成大写。
(10) 创建一个名为 e2f 的英法字典并打印出来。这里提供一些单词对：dog 是 chien，cat
是 chat，walrus 是 morse。
(11) 使用你的仅包含三个词的字典 e2f 查询并打印出 walrus 对应的的法语词。
(12) 利用 e2f 创建一个名为 f2e 的法英字典。注意要使用 items 方法。
(13) 使用 f2e，查询并打印法语词 chien 对应的英文词。
(14) 创建并打印由 e2f 的键组成的英语单词集合。
(15) 建立一个名为 life 的多级字典。将下面这些字符串作为顶级键：'animals'、'plants'
以及 'others'。令 'animals' 键指向另一个字典，这个字典包含键 'cats'、'octopi'
以及 'emus'。令 'cat' 键指向一个字符串列表，这个列表包括 'Henri'、'Grumpy' 和
'Lucy'。让其余的键都指向空字典。
(16) 打印 life 的顶级键。
(17) 打印 life['animals'] 的全部键。
(18) 打印 life['animals']['cats'] 的值
'''
year_list = [1995,1996,1997,1998,1999,2000]
print("三岁生日年份：",year_list[3])
print("年龄最大的一年：",max(year_list))
things = ["mozzarella","cinderella","salmonella"]
a = things[0].replace("m","M"),things[1].replace("c","C"),things[2].replace("s","S")
print(list(a))
surprise = ["Groucho","Chico","Harpo"]
str1 = surprise[-1].replace("H","h")[::-1].replace("o","O")
print(str1)

e2f = {
    "dog" : "chien" ,
    "cat" : "chat" ,
    "walrus" : "morse",
}
print(e2f["walrus"])
list3 = list(e2f.values())
list4 =list(e2f.keys())
f2e = dict(zip(list3,list4))
print(f2e)
print(f2e["chien"])
life = {
    "animals":{"cats":"","octopi":"","emus":""},
    "cat" : ["Henri","Grumpy","Lucy"],
    "plants":{},
    "others":{}
}
print(life)
print(life["animals"].keys())
print(life['animals']['cats'])