import time

print ("""++++++++++++++++++++++++++++++++

Please enter your HEIGHT AND WEIGHT to 

calculate your BODY INDEX...

++++++++++++++++++++++++++++++++""")

a = float(input("Please enter your HEIGHT: "))

b = float(input("Please enter your WEIGHT: "))

if a > 3: 
    a = a / 100

else:
    pass

index = b / (a * a)

print("It is being calculated... Please wait!")

time.sleep(2)

print("Your BODY INDEX is {}".format(index))