try:
    file = open("/tmp/test.txt","r")
    list1 = file.readlines()
    for i in list1:
        print(i)
    file.close
except FileNotFoundError:
    print("There is NOOOO file!")

