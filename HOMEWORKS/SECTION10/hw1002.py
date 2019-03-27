try:
    file = open("/tmp/test.txt","r")
    for i in file:
        print(i, end = "")
    file.close
except FileNotFoundError:
    print("There is NOOOO file!")

