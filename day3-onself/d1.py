'''

'''
def test1(data):
    if isinstance(data  , dict):
        data["name"] = "kevin"
if __name__ == '__main__':
    test_data = {}
test1(test_data)
print(test_data)
pass

def test(*a):
    print(*a)
b=[1,2,1]
test(*b)

def test2(x,*,y,z,**args):
    print(x,y,z,args)
test2(1,y=2,z=3 ,age=19)

