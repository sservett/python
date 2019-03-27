class book():
    
    def __init__(self,name,writer,nop,type):
        print("Init function")
        self.name = name 
        self.writer = writer
        self.nop = nop
        self.type = type

    def __str__(self):
        return "Name : {}\nWriter {}\nPage: {}\nType: {}".format(self.name,self.writer,self.nop,self.type)
    
    def __len__(self):
        return self.nop
    
    def __del__(self):
        print("The book is being deleted now...")

book1 = book("Elmer","Ibrahim Berk INCE",24,"Cartoon")
print(book1)
print(len(book1))
del(book1)