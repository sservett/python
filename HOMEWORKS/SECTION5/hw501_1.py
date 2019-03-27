for a in range(1,10000):   
    list1 = []
    i = 1

    while i < a:    
        if (a % i == 0):
            list1.append(i)
        i += 1

    b = 0

    for i in list1:
        b = b + i

    if a == b :
        print("{} Wonderful NUMBER".format(a))
  