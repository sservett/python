def function1(*args):
        for i in args:
                print(i)

def function2(*kwargs):
        for i in kwargs:
                print(i)

def greetings(name):
        print("Hello",name,"!")

hello = greetings

print(function1(1,2,3,4,5,6,7,8))

hello("ArzU")
greetings("Arzuuu")


def funct1(*args):

        def add(args):
                total = 0
                for i in args:
                        total += i
                return total
        print(add(args))

print(funct1(3,4,5,6,7))

print(function2("Servet","iNCE","1983","ibrahim"))

#5443524509