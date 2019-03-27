import time

class car():

    def __init__(self,brand,model,hp,color,clinyder,features):

        self.brand = brand
        self.model = model
        self.hp = hp
        self.color = color
        self.clinyder = clinyder
        self.features = features

    def show_details(self):

        print("""
        ===================
        Here is the details
        
        Brand : {}
        
        Model: {}
        
        hp: {}
        
        color: {}
        
        clinyder: {}

        features: {}
        ===================
        """.format(self.brand,self.model,self.hp,self.color,self.clinyder,self.features))
    
    def change_color(self,new_color):

        print("Changing color now...")
        time.sleep(1)

        self.color = new_color

    def add_feature(self,new_feature):

        print("Adding a new feature...")
        time.sleep(1)

        self.features.append(new_feature)

    def add_hp(self,add_hp):

        print("Adding HP..")
        time.sleep(1)

        self.hp += add_hp



car1 = car("BMW","X5",272,"Red",8,["ABS","AC","Aibags"])

car2 = car("BMW","3.20ie",172,"White",8,["ABS","Aibags","Speed Limiter"])

car3 = car("VW","Golf",116,"Black",4,["ABS","GPS","DVD"])

list1 = [car1,car2,car3]

"""
for i in list1:
    print("Model of {} is = {}".format(i,i.model))
"""
car1.show_details()

car3.show_details()

car1.change_color("Green")

car1.add_feature("DVD")

car3.add_hp(10)

car1.show_details()

car3.show_details()