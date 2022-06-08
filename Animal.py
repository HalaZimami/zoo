from email.base64mime import header_length

class animal:
    def __init__(self, name, age, healthLevel, happinessLevel):
        self.name=name
        self.age=age
        self.healthLevel=healthLevel
        self.happinessLevel=happinessLevel

    def display_info(self, age=0):
        self.age=age
        print(f"Name: {self.name} | Type: {self.type} | Age: {self.age} | Health level: {self.healthLevel} | Happiness level: {self.happinessLevel}")
        return self

    def feed(self, inc):
        self.healthLevel+=inc
        self.happinessLevel+=inc
        return self

class lion(animal):
    def __init__(self, name):
        super().__init__(name, age=0, healthLevel=100, happinessLevel=75)
        self.type="Lion"
    
    def information(self):
        print(f"hello iam {self.name} and my type is {self.type} ")

class tiger(animal):
    def __init__(self, name):
        super().__init__(name, age=0, healthLevel=85, happinessLevel=60)
        self.type="Tiger"
        self.skin="Pink"

    def information(self):
        print(f"hello iam {self.name} and my type is {self.type} ")

    def display_info(self):
        super().display_info(2)
        print(f"Skin: {self.skin}")
    
    
    def attack(self,energy):
        print("PinkPanther attacked the sheep and ate it!!! Increase Health and happiness :)")
        self.feed(energy)
        return self


class sheep(animal):
    def __init__(self, name):
        super().__init__(name, age=0, healthLevel=80, happinessLevel=40)
        self.type="Sheep"

    def information(self):
        print(f"hello iam {self.name} and my type is {self.type} ")


simba = lion("simba")
pinkPanther = tiger("PinkPanther")
sheepy = sheep("sheepy")

simba.information()
simba.display_info(3)
pinkPanther.information()
pinkPanther.display_info()
pinkPanther.attack(10).display_info()
sheepy.information()
sheepy.display_info(1)
