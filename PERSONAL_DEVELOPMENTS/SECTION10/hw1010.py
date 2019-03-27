with open("/tmp/test.txt","r+") as file:
    list1 = file.readlines()
    list1.insert(2,"Ali Mert INCE\n")
    file.seek(0)
    file.writelines(list1)