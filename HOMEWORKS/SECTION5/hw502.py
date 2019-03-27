print("""========================================

Please enter 3 or 4 digit number to check 

whether it is AMSTRONG number or NOT 

========================================""")

a = int(input("Please enter a number :"))

if (a // 1000 < 10 and a // 1000 >= 1):

    first =  (a % 10)
    #print("1 : ",first)

    second =  ((a // 10) % 10)
    #print("2 : ",second)

    third =  ((a // 100) % 10)
    #print("3 : ",third)

    forth =  (a // 1000)
    #print("4 : ",forth)

    list1 = [first,second,third,forth]
    #print(list1)

    b = (list1[0] ** 4) + (list1[1] ** 4) + (list1[2] ** 4) + (list1[3] ** 4)
    
    if a == b:
        print("This is AMSTRONG number --> ",a)
    else:
        print("Nope, this is NOT!!")

## =====

elif (a // 100 < 10 and a // 100 >= 1):

    first =  (a % 10)
    #print("1 : ",first)

    second =  ((a // 10) % 10)
    #print("2 : ",second)

    third =  (a // 100)

    list1 = [first,second,third]
    #print(list1)

    b = (list1[0] ** 3) + (list1[1] ** 3) + (list1[2] ** 3)
    
    if a == b:
        print("This is AMSTRONG number --> ",a)
    else:
        print("Nope, this is NOT!!")

else:
    print("Unexpected number!!!")