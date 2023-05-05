#multiple_inheritance

class Animal:
    def __init__(self,animal):
        print(animal,"is an animal")
        
class Mammal(Animal):
    def __init__(self,mammal):
        print(mammal, "is mammal animal")
        super().__init__(mammal)
        
class CannotFlyMammal(Mammal):
    def __init__(self,cannot_fly_mammal):
       print(cannot_fly_mammal,"can not fly!")
       
class CannotSwimMammal(Mammal):
    def __init__(self,cannot_swim_mammal):
        print(cannot_swim_mammal,"can not swim..")
        
class Kalakukko(CannotSwimMammal, CannotFlyMammal):
    def __init__(self):
        print("kalakukko has no legs")
        super().__init__('Kalakukko')
        
kk = Kalakukko()

bat = CannotSwimMammal('Batman')