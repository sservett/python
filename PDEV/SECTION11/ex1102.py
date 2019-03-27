
######## MAP ########

def double(a):
    return a * 2

print(list(map(double,[1,2,3,4,5,6,7])))

print(list(map(lambda x : x ** 2 , (1,2,3,4,5,6,7,8,9,10) )))


list1 = [1,2,3,4,5]

list2 = [5,10,15,20,25,30,35]

list3 = [3,6,9,12]


print(list(map(lambda x,y,z : x * y * z, list1, list2, list3)))

######## REDUCE ########

from functools import reduce

print(reduce(lambda x,y : x * y, [1,2,3,4,5]))

def max(x,y):
    if x > y:
        return x
    else:
        return y

print(reduce(max,[2,3,4,133,294,224,3874,2223,387,323]))

######## FILTER ########

print(list(filter(lambda x : x % 2 == 0 , [23,45,33,22,264])))

def is_prime(x):
    i = 2
    if (x == 1):
        return x + False
    elif (x == 2):
        return x + True
    else:
        while(i < x):
            if (x % i == 0):
                return x + False
            i += 1
        return x + True

print(list(filter(is_prime,range(2,100))))


######## ZIP ########

list1 = [1,2,3,4,5]

list2 = [5,10,15,20,25,30,35]


i = 0 
result = list()
while (i < len(list1) and i < len(list2)):
    result.append((list1[i],list2[i]))
    i += 1
print(result)

print(list(zip(list1,list2)))