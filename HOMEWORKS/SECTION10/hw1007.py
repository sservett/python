with open("/tmp/test.txt","r") as file:
    print(file.tell())
    file.seek(20)
    print(file.tell())
  
