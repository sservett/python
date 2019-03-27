import time

print ("""++++++++++++++++++++++++++++++++

Please enter 3 numbers

They will be multiplied. 

++++++++++++++++++++++++++++++++""")

a = float(input("Please enter 1st number: "))

b = float(input("Please enter 2nd number: "))

c = float(input("Please enter 3rd number: "))

print("It is being calculated... Please wait!")

time.sleep(3)

SOLUTION = a * b * c

print("{} , {} , {} nin carpimlari {} dir".format(a,b,c,SOLUTION))