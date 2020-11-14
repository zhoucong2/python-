sxh = []
for i in range(100, 1000):
    m = list(str(i))
    s = 0
    for j in m:
      s += int(j)**len(m)
    if i == s:
        print(i)
        sxh.append(i)

print("100-999的水仙花数：%s" % sxh)
