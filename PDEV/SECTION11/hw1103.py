from functools import reduce

def add(x,y):
    return x+y

def is_even(x):
    if x % 2 == 0:
        return x
    
list1 = [1,2,3,4,5,6,7,8,9,10]

print(reduce(add,(list(filter(is_even,list1)))))

print(bin(max(list1)))

print(hex(max(list1)))

"""
##Just one line.. 

print(reduce(lambda x,y: x+y ,list(filter(lambda x: x%2==0 , list1))))

"""