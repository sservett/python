class animals():
    
    def __init__(self,name,family,homeland,nutrition,skin):
        self.name = name 
        self.family = family 
        self.homeland = homeland
        self.nutrition = nutrition
        self.skin = skin 
    
    def __str__(self):
        return "Name: {}\nFamily: {}\nHomeland: {}\nNutrition: {}\nSkin: {}".format(self.name,self.family,self.homeland,self.nutrition,self.skin)
    

class dog(animals):

    def __init__(self,name,family,homeland,nutrition,skin,paw,tail):
        super().__init__(name,family,homeland,nutrition,skin)
        self.paw = paw
        self.tail = tail
    
    def __str__(self):
        return """
        Name: {}
        Family: {}
        Homeland: {}
        Nutrition: {}
        Skin: {}
        Paw: {}
        Tail: {}
        """.format(self.name,self.family,self.homeland,self.nutrition,self.skin,self.paw,self.tail)

class bird(animals):

    def __init__(self,name,family,homeland,nutrition,skin,beak,wing):
        super().__init__(name,family,homeland,nutrition,skin)
        self.beak = beak
        self.wing = wing
    
    def __str__(self):
        return """
        Name: {}
        Family: {}
        Homeland: {}
        Nutrition: {}
        Skin: {}
        Beak: {}
        Wing: {}
        """.format(self.name,self.family,self.homeland,self.nutrition,self.skin,self.beak,self.wing)

class horse(animals):

    def __init__(self,name,family,homeland,nutrition,skin,genus,color):
        super().__init__(name,family,homeland,nutrition,skin)
        self.genus = genus
        self.color = color
    
    def __str__(self):
        return """
        Name: {}
        Family: {}
        Homeland: {}
        Nutrition: {}
        Skin: {}
        Genus: {}
        Color: {}
        """.format(self.name,self.family,self.homeland,self.nutrition,self.skin,self.genus,self.color)


anamail1 = animals("Crocodila","Reptiles","Africa","Carnivorous","Scale")

dog1 = dog("Kangal","Wolf","Turkey","Carnivorous","Hairy","Twice","Long")

bird1 = bird("Crow","Birds","India","Herbivorous","Hairy","Short","Small")

horse1 = horse("Pony","Horses","Ireland","Carnivorous","Hairy","Pony","White")

print(anamail1.name)
print(dog1.homeland)
print(bird1.beak)
print(horse1.color)