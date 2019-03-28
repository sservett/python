#SHORT SOLUTION

def cal_area1(s):
    return s[0] * s[1]

list_0 = [(3,4),(10,3),(5,6),(1,9)]

print(list(map(cal_area1,list_0)))


##LONG SOLUTION

def cal_area2(a,b):
    return a * b 

list0 = [(3,4),(10,3),(5,6),(1,9)]

list1 = list()
list2 = list()

for i,j in list0:
    list1.append(i)
    list2.append(j)

print(list(map(lambda a,b : cal_area2(a,b) , list1,list2)))

### CALCULATING ROUND
def cal_round(a):
    return 2 * (a[0] + a[1])

list_0 = [(3,4),(10,3),(5,6),(1,9)]

print(list(map(cal_round,list_0)))
"""

def is_triangle(tuple):
    
    if (tuple[0]+tuple[1] > tuple[2] and tuple[0]+tuple[2] > tuple[1] and tuple[1]+tuple[2] > tuple[0]):
        return True
    else:
        return False


list0 = [(3,4,5),(6,8,10),(3,10,7),(3,5,7),(5,12,14),(7,2,10)]

print(list(filter(is_triangle,list0)))
"""

"""
list = [[1,2,3], [4,5,6,7],[8,9]]

list1 = [2 * i for i in list]

print(list1)

list = [(1,2),(3,4),(5,6)]

list1 = [i * j for i,j in list]

print(list1)

print(list(map(list1,level)))

#print(list(map(lambda x,y : x * y ,list11,list12)))

"""
    