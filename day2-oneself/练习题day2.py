
def list(list1):
    list2 = [i for i in list1 if i > 0]
    list3 = [i for i in list1 if i < 0]
    return ' 正数数量: ', len(list2), ' 负数数量: ', len(list3)


if __name__ == '__main__':
    x = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
print(list(x))






# str1 = "axbyczdj"
# print( str1[0 : : 2] )






# str1 = "hello_world_"
# tuble1 = str1[0: 5], str1[-6: -1]
# print(list(tuble1))







# value = 1
# print("{0}{0}{0}{1}".format(0, value))




# list1 = [1, 3, 5, 7]
# list1.insert(3, list1[0])
# del list1[0]
# print(list1)


# a = 9
# b = 8
# a, b = b, a
# print(a, b)


# a = "100"
# while int(a) < 1000:
#     if int(a[0]) ** 3 + int(a[1]) ** 3 + int(a[2]) ** 3 != int(a):
#         a = str(int(a) + 1)
#         continue
#     print(int(a))
#     a = str(int(a) + 1)
