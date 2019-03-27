def is_perfect(a):

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
        print("This is Wonderful NUMBER")
    else:
        print("This is Simple Number")

is_perfect(6)
  