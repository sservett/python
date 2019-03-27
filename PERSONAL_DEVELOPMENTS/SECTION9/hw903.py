def is_even(a):

    if a % 2 == 0:
        print("YES, Even number")

    else:
        raise ValueError

liste = [34,23,25,43,56,493939,40955,200293,9399394,933,2,1,3,33,100,61,1800]

for i in liste:

    try:
        print(is_even(i))

    except ValueError:
        pass

