print ("""++++++++++++++++++++++++++++++++++++++++++++++

Please ENTER 2 numbers;

++++++++++++++++++++++++++++++++++++++++++++++""")

a = int(input("First Number:"))
b = int(input("Second Number:"))

a,b = b,a+b

print("A : ",a)
print("B : ",b)