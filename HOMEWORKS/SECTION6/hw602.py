def gcm(a,b):

    list1 = []
    
    i = 1
        
    while (i <= a) and (i <= b):
    
        if (a % i == 0) and (b % i == 0):
            list1.append(i)
    
        i += 1

    print("The GCM of {} and {} is".format(a,b),max(list1))

Num1 = int(input("Please enter 1st Number : "))

Num2 = int(input("Please enter 2nd Number : "))

gcm(Num1,Num2)




  