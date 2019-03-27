with open("/tmp/test.txt","r") as file:
    file.seek(10)
    print(file.read(10))
    file.tell()
  
