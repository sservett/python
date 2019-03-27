import time 

print ("""++++++++++++++++++++++++++++++++++++++++++++++

Please ENTER Triangle's right EDGEs hypotenuse EDGE;

++++++++++++++++++++++++++++++++++++++++++++++""")

a = int(input("First Edge:"))
b = int(input("Second Edge:"))

c = float((a ** 2 + b ** 2) ** 0.5)

print("Calculating...")
time.sleep(1)

print("HYPOTENUSE EDGE : ",c)