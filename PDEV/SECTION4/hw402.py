print("""=================================================
 
Please enter 3 number, the highest one will be printed..
 
 ================================================="""
)

a = int(input("1st Number : "))
b = int(input("2nd Number : "))
c = int(input("3rd Number : "))


if a > b  and a > c :
    print("The Highest Number is {}".format(a))
elif b > a  and b > c :
    print("The Highest Number is {}".format(b))
elif c > a  and c > b :
    print("The Highest Number is {}".format(c))
elif a == b  and b > c :
    print("1st and 2nd Numbers are Equal and the number is {}".format(a))
elif a == c  and a > b :
    print("1st and 3rd Numbers are Equal and the number is {}".format(a))
elif b == c  and b > a :
    print("2nd and 3rd Numbers are Equal and the number is {}".format(b))
else:
    print("All Numbers are Equal!!")
