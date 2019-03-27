def is_triangle(tuple):
    
    if (abs(tuple[0]+tuple[1]) > tuple[2] and abs(tuple[0]+tuple[2]) > tuple[1] and abs(tuple[1]+tuple[2]) > tuple[0]):
        return True
    else:
        return False


list0 = [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(is_triangle,list0)))

"""
list0 = [(3,4,5),(6,8,10),(3,10,7)]

list1 = list()
list2 = list()
list3 = list()

for x,y,z in list0:
    list1.append(x)
    list2.append(y)
    list3.append(z)

print(list1)
"""
