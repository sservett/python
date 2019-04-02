"""
a = int(input())
b = int(input())

if not (a >= 1 and a <= (10 ** 10)):
    print("a is Invalid number")

if not (b >= 1 and b <= (10 ** 10)):
    print("b is Invalid number")


total = a + b

diff = a - b 

multiply = a * b 

print(total)
print(diff)
print(multiply)

==================================

a = int(input())
b = int(input())

print(a // b)
print(a % b)
print(divmod(a, b))

==================================

a = int(input())
b = int(input())
m = int(input())

if not ( a>=1 and a<=10):
    print("a Ivalid number")
elif not ( b>=1 and b<=10):
    print("b Ivalid number")
elif not ( m>=2 and m<=1000):
    print("m Ivalid number")
else:
    print(pow(a,b))
    print(pow(a,b,m))

==================================

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(pow(a,b)+pow(c,d))

==================================


N = int(input())

if (N >=1 and N <= 9):
    for i in range(1,N): 
        if (i == 1):
            print(i)
        else:
            while True:
                result=11 
                print(i * result)    
                result += (10 ** i)

==================================

for i in range(1,int(input())):
    print(((10**i)//9) * i)




def servet(ali):
    def arzu():
        print("Ben Arzu")
        ali()
    return arzu

@servet
def ince():
    print("INCEEE")


ince()

"""