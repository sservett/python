def multiply():
    
    a = int(input("Number1: "))
    b = int(input("Number1: "))

    if (type(a) == int) and (type(a) == int):
        print(a * b)
    else:
        print("here")
        raise ValueError

try:
    multiply()
except ValueError:
    print("Yokkkk gari")