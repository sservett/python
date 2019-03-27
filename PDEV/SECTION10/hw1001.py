try:
    file = open("/tmp/test.txt","a")
    file.write("\nMustafa INCE\nKemal INCE")
    file.close
except FileNotFoundError:
    print("There is NOOOO file!")

