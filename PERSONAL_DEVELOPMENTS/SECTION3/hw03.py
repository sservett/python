import time

print ("""++++++++++++++++++++++++++++++++++++++++++++++

Calculate your FUEL Consumption of your JOURNEY.

Please enter the following VALUES;

++++++++++++++++++++++++++++++++++++++++++++++""")

a = float(input("What is consumption of your car per km? (Please enter pence): "))
b = float(input("How many KMs have you done? : "))

TOTAL = float((a * b) /100)

print("It's being calculated now..")
time.sleep(2)

print("Total amohtn you need to pay is {} pound".format(TOTAL))

