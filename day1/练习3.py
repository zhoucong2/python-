test_data = [10,20, 30, 90, 100,80]
test_data.sort()
_, *middle, _=test_data
print(sum(middle)/len(middle))
