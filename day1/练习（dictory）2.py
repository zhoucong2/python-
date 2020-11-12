stu = {
    "studentNo": "001",
    "studentName": "陈超",
    "phone": "1212312",
    "address": "武汉",
    "bornDate": "2020/9/8",
    "gradeId": 3
}
logins = {
    1: "甘露",
    2: "陈超",
    3: "张芳",
    4: "范帅",
}
for k,v in stu.items():
   print("key = {},value={}".format(k,v))
for key in logins.keys():
   print("会话id == {}".format(key))
for name in logins.values():
    print("登录用户名 == {}".format(name))