class computer():
    
    def __init__(self,name,brand,proceesor,cpu,memory,hdd,speed,videocard,screensize):
        self.name = name 
        self.brand = brand 
        self.proceesor = proceesor
        self.cpu = cpu
        self.memory = memory 
        self.hdd = hdd
        self.speed = speed
        self.videocard = videocard
        self.screensize = screensize
    
    def __str__(self):
        return """
        Name: {}
        Brand: {}
        Proceesor: {}
        Cpu: {}
        Memory: {}
        HDD: {}
        Speed: {}
        Videocard: {}
        Screensize: {}
        """.format(self.name,self.brand,self.proceesor,self.cpu,self.memory,self.hdd,self.speed,self.videocard,self.screensize)

class iMac(computer):

    def __init__(self,name,brand,proceesor,cpu,memory,hdd,speed,videocard,screensize,ali1,veli2):
        super().__init__(name,brand,proceesor,cpu,memory,hdd,speed,videocard,screensize)
        self.ali1 = ali1
        self.veli2 = veli2

    def __str__(self):
        return """
        Name: {}
        Brand: {}
        Proceesor: {}
        Cpu: {}
        Memory: {}
        HDD: {}
        Speed: {}
        Videocard: {}
        Screensize: {}
        Ali1: {}
        Veli2: {}
        """.format(self.name,self.brand,self.proceesor,self.cpu,self.memory,self.hdd,self.speed,self.videocard,self.screensize,self.ali1,self.veli2)

computer1 = computer("x1 Carbon","Lenovo","i7","8","16GB","512GB","1.9gHz","1920x1080","14inch")

apple1 = iMac("MacBook","Apple","m3","4","8GB","256GB","2.1gHz","1920x1080","13inch","ali1","veli2")

print(computer1)
print(apple1)