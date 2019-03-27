import modul1
import time 

print("""==================================

WELCOME CALCULATOR

Please select your process;

1.) Adding        --> a + b
2.) Subtracting   --> a - b
3.) Multiplying   --> a * b
4.) Dividing      --> a / b
5.) Exponent      --> a ** b
6.) Root          --> b _/""a

==================================""")

process = input("Your choice: ")

if process != "1" or process != "2" or process != "3" or process != "4" or process != "5" or process != "6":
    print("Invalid Choice!!")

a = float(input("Please enter 1st Number:"))
b = float(input("Please enter 2nd Number:"))

print("Calculating..")
time.sleep(1)
while True:

    if (process == "1"):
        print(modul1.add(a,b))
        break
    elif (process == "2"):
        print(modul1.subtract(a,b))
        break
    elif (process == "3"):
        print(modul1.multiply(a,b))
        break
    elif (process == "4"):
        print(modul1.divide(a,b))
        break
    elif (process == "5"):
        print(modul1.exponent(a,b))
        break
    elif (process == "6"):
        print(modul1.root(a,b))
        break
    else:
        print("Invalid Choice!!")
        break