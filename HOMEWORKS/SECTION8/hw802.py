from time import sleep

class student():

    def __init__(self,name,surname,number,lessons,rank):

        self.name = name
        self.surname = surname 
        self.number = number 
        self.lessons = lessons 
        self.rank = rank 
    
    def showinfo(self):

        print("""
        ================================

        Name Surname : {} {}

        Number: {}

        Lessons: {}

        Rank: {}
        
        ================================
        """.format(self.name,self.surname,self.number,self.lessons,self.rank))

    def chg_number(self,new_number):
        
        print("The number is being changed...")
        sleep(1)

        self.number = new_number

    def add_lesson(self,new_lesson):

        print("Adding a new lesson..")
        sleep(1)

        self.lessons.append(new_lesson)
    
    def increase_rank(self,how_much):
        
        print("The rank is being changed...")
        sleep(1)

        self.rank -= how_much

student1 = student("Servet","INCE",1240,["Math","Science","English"],23)
student2 = student("Arzu","BAL INCE",1186,["Turkish","Math","French"],12)

print(dir(student))
"""
student1.showinfo()
student2.showinfo()
student1.chg_number(1999)
student1.add_lesson("Chinese")
student2.add_lesson("German")
student1.increase_rank(5)
student2.increase_rank(6)
student1.showinfo()
student2.showinfo()

"""

