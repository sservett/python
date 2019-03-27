try:
    file = open("/tmp/test.txt","r")
    content1 = file.readline()
    print("CoF 1:")
    print(content1)
    content2 = file.readline()
    print("CoF 2:")
    print(content2)
    content3 = file.readline()
    print("CoF 3:")
    print(content3)
    content4 = file.readline()
    print("CoF 4:")
    print(content4)
    content5 = file.readline()
    print("CoF 5:")
    print(content5)
    file.close
except FileNotFoundError:
    print("There is NOOOO file!")

