def lcm(a,b):

    i = 1
        
    while True:

        if (a * i) % b == 0:
            print("The LCM of {} and {} is".format(a,b),(a * i))
            break
        else:
            i += 1

Num1 = int(input("Please enter 1st Number : "))

Num2 = int(input("Please enter 2nd Number : "))

lcm(Num1,Num2)
  