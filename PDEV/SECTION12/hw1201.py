class fileclass():
    
    def __init__(self,filename):

        with open(filename,"r") as file:

            file_content = file.read()   
            words = file_content.split()
            
            self.clear_words = list()

            for word in words:
                word = word.strip()
                word = word.strip(".")
                word = word.strip(",")
                word = word.strip("(")
                word = word.strip(")")
                word = word.strip("\n")
                self.clear_words.append(word)
            """
            for i in self.clear_words :
                print("--------------")
                print(i)
            """
    def find_word(self,search_word):
        places = list()
        count = 1 
        
        for word in self.clear_words:
            if (word == search_word):
                places.append(count)
            count += 1

        if (len(places) == 0):
            print("Cannot find this file!")
        else:
            print("The word {} is mentioned.. \n{} ".format(search_word,places))

    def word_histogram(self):

        word_fre = dict() 
        word_set = set()

        for word in self.clear_words:
            word_set.add(word)
            if (word in word_fre):
                word_fre[word] += 1
            else:
                word_fre[word] = 1
        
        print("======Frequency of Words======")
        
        for i, j in word_fre.items():
            print("The word {} is written {} times in the text".format(i,j))
    
        print("\n######ALL of Words######\n")
        for i in word_set:
            print(i)
            print("********************")


file1 = fileclass("TEXT.txt")

print("""****************

File Options

1. Learn the frequency of all of the words

2. Find World

Press 'q' to quit.

""")
while True:
    process = input("process:")

    if (process == "q"):
        print("Quiting....")
        break
    elif (process == "1"):
        file1.word_histogram()
    elif (process == "2"):
        kelime = input("HWhich word are you looking for ? :")
        file1.find_word(kelime)
    else:
        print("Invalid option..")