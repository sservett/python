a1 = "one"
a2 = "two"
a3 = "three"
a4 = "four"
a5 = "five"
a6 = "six"
a7 = "seven"
a8 = "eight"
a9 = "nine"
a10 = "ten"
a11 = "eleven"
a12 = "twelve"
a13 = "thirteen"
a14 = "fourteen"
a15 = "fifteen"
a16 = "sixteen"
a17 = "seventeen"
a18 = "eightteen"
a19 = "nineteen"
a20 = "twenty"
a30 = "thirty"
a40 = "fourty"
a50 = "fifty"
a60 = "sixty"
a70 = "seventy"
a80 = "eighty"
a90 = "ninety"

list1 = ["",a1,a2,a3,a4,a5,a6,a7,a8,a9]
list2 = ["",a11,a12,a13,a14,a15,a16,a17,a18,a19]   
list3 = ["","",a20,a30,a40,a50,a60,a70,a80,a90]

def spelling(a):

    if a >= 10 and a <= 99:
        fd = (a % 10)
        sd = (a // 10)

        if sd == 1 and fd !=0:
            return list2[fd]
        elif sd == 1 and fd ==0:
            return a10
        else:
            return list3[sd] + " " + list1[fd]
    else :
        return "Invalid Number!"

a = int(input("Please enter 2 digit number: "))

print(spelling(a))