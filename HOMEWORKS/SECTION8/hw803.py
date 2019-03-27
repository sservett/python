from time import sleep

class worker():
    
    def __init__(self,name,surname,department,salary):
        print("The init fuction of worker class")
        
        self.name = name
        self.surname = surname
        self.department = department
        self.salary = salary
    
    def show_info(self):
        print("""
        ===========================
        Information of Worker Class

        Name: {}
        Surname: {}
        Department: {}
        Salary: {}
        ============================
        """.format(self.name,self.surname,self.department,self.salary))

    def chg_department(self,new_department):
        print("Changing the department...")
        sleep(1)
        self.department = new_department      

class manager(worker):

    def __init__(self,name,surname,department,salary,number_of_people):
        print("The init fuction of manager class")
        super().__init__(name,surname,department,salary)
        """
        ## Super KEY is used instaed of following methods. 
        ## Super Key inherits the method from defined one. 
        ## In this case, __init__ inherits from worker class
        self.name = name
        self.surname = surname
        self.department = department
        self.salary = salary
        """
        self.number_of_people = number_of_people

    def increase_salary(self,how_much_increase):
        print("The salary is being increased..")
        sleep(1)
        self.salary += how_much_increase  

    def show_info(self):
        print("""
        ===========================
        Information of Manager Class

        Name: {}
        Surname: {}
        Department: {}
        Salary: {}
        Number of People: {}
        ============================
        """.format(self.name,self.surname,self.department,self.salary,self.number_of_people))

    def chg_people(self,how_many):
        print("The number of team is being changed..")
        sleep(1)
        self.number_of_people += how_many  

worker1 = worker("Esin","KELES","Purchasing",3000)
manager1 = manager("Servet","INCE","DevOps",4800,24)
manager2 = manager("Arzu","BAL INCE","Finance",4000,12)

manager1.show_info()
worker1.show_info()
manager2.show_info()
manager1.chg_department("UNIX/LInux")
manager1.increase_salary(300)
manager2.increase_salary(450)
worker1.chg_department("HR")
manager2.chg_people(6)
manager1.show_info()
worker1.show_info()
manager2.show_info()

#print(dir(manager))