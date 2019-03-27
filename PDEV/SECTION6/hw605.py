def pisagor():

    list_pisagor = list()
    
    for i in range(1,101):
    
        for j in range(1,101):
    
            third_edge = ((i ** 2) + (j ** 2)) ** 0.5

            if third_edge == int(third_edge):
                list_pisagor.append((i,j,int(third_edge)))
    return list_pisagor

for i in pisagor():
    print(i)