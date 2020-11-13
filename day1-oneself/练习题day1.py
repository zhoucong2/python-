# list1 = [1, 2, 3, 1, 2, 3]
# del list1[0:3]
# print(list1)

# list1 = [1, 2, 3, 1, 2, 3]
# list1.sort()
# a=0
# for i in list1:
#     if list1[a] != list1[a+1] and a !=len(list1)-1:
#         i=list1[a]
#     else:
#         del list1[a]
#     a=a+1
# print(list1)



# str1=" hello "
# str2=" world "
# str3=str1.replace(" ","")+" "+str2.replace(" ","")
# print(str3)


# str1 = " hello "
# str2 = " world "
# a = str1.lstrip()
# b = a.rstrip()
# c = str2.lstrip()
# d = c.rstrip()
# print(b + " " + d)

# list1 = [1, "abcd", ['a', 'ed'], "fd"]
# value1 = list1[2]
# value = value1[0]
# print(value)

list1 = ["语文", "数学", "英语"]
list2 = [90, 80, 70]
for k, c in zip(list1, list2):
    print(" 科目={} ""  成绩={}  ".format(k, c))
