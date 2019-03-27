with open("/tmp/test.txt","r+") as file:
    list1 = file.readlines()
    list1.insert(2,"Ali Berke INCE\n")
    file.seek(0)
    for i in list1:
        file.write(i)