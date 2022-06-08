from Animal import animal
from Animal import lion
from Animal import tiger
from Animal import sheep

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append( lion(name) )
    def add_tiger(self, name):
        self.animals.append( tiger(name) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info(2)
    def att2(self):
        for tiger in self.animals:
            tiger.attack(10)
print("------------------------------------------------------------------------")
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()

    