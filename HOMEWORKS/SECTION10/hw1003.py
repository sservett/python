try:
    file = open("/tmp/test.txt","r")
    content1 = file.read()
    print("CoF 1:")
    print(content1)
    content2 = file.read()
    print("CoF 2:")
    print(content2)
    content3 = file.read()
    print("CoF 3:")
    print(content2)
    file.close
except FileNotFoundError:
    print("There is NOOOO file!")

