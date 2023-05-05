class Animal:
    def __init__(self):
        self.name = "Animal"
        self.saying = "Default animal saying"
        # self.print_animal_info()
      
    def print_animal_info(self):
        # print(f"{self.name}\n{self.saying}")
        print("dcnjdcnj")
        
class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.name ="Cat"
        self.saying = "MEOW!"
        Animal.print_animal_info(self)
        self.print_animal_info()
        
kissa = Cat()