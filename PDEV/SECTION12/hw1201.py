class fileclass():
    
    def __init__(self):

        with open("/Users/c0257951/Documents/GITLAB/python/PDEV/SECTION12/TEXT.txt","r") as file:

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
            for i in self.clear_words :
                print("--------------")
                print(i)
    
    def find_word(self,search_word):
        places = list ()
        count = 1 
        
        for word in self.clear_words:
            if (word == search_word):
                places.append(count)
            count += 1

        if (len(places) == 0):
            print("Cannot find this file!")
        else:
            print("The word {} is mentioned.. \n{} ")


file1 = fileclass()

