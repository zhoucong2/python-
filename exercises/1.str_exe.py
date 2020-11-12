letters = 'abc，def ghi，jkl mno pqrs tuv wxyz'
print(letters[::7])#从开始到结尾，步数为7
print(letters[-1::-1])#从结尾到开始
letters1=letters.split("，")#split（）函数：字符串以“，”为分隔符，将字符串分割成列表
print(letters1)
letters2=",".join(letters1)#join（）函数：列表以“，”为合并符，将列表合并成字符串
print(letters2)
letters3=letters.replace("def ghi","123")#replace()函数：对字符串进行简单的子替换
print(letters3)

