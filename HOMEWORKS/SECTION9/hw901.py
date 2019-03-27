try:

    a = int(input("Number1:"))
    b = int(input("Number2:"))
    print(a/b)

except (ValueError,SyntaxError):

    print("Please enter a NUMBER!!")

except ZeroDivisionError:

    print("Cannot divide it to ZERO!!")

finally:

    print("Finally it worked!")

print("The blocks are end")