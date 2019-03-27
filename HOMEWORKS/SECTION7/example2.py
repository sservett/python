import servet
import time 

def welcome():
    print("""==================================

    WELCOME CALCULATOR

    Please select your process;

    1.) Adding        --> a + b
    2.) Subtracting   --> a - b
    3.) Multiplying   --> a * b
    4.) Dividing      --> a / b
    5.) Exponent      --> a ** b
    6.) Root          --> b _/""a

    Press "q" to QUIT

    Press "p" to PRINT again

==================================""")

welcome()

while True:
    print("")
    process = input("Your choice: ")

    if (process == "p"): 
        welcome()
        continue


    if (process == "1" or process == "2" or process == "3" or process == "4" or process == "5" or process == "6" or process == "q"):

        if (process == "q"):
            print("")
            print("Thank you. Goodbye!!")
            break

        a = float(input("Please enter 1st Number:"))
        b = float(input("Please enter 2nd Number:"))

        print("Calculating..")
        time.sleep(1)


        if (process == "1"):
            print(modul1.add(a,b))
            
        elif (process == "2"):
            print(modul1.subtract(a,b))
            
        elif (process == "3"):
            print(modul1.multiply(a,b))
            
        elif (process == "4"):
            print(modul1.divide(a,b))
            
        elif (process == "5"):
            print(modul1.exponent(a,b))
            
        elif (process == "6"):
            print(modul1.root(a,b))

        else:
            continue

    else:
        print("--------------------")
        print("Invalid Choice!!")
        print("--------------------")
        welcome()