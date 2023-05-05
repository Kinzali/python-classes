class Car:
    
    wheels = 4
    
    def __init__(self,make,model, year, km=0):
        # self.make= make
        self.model = model
        self.year= year
        self.km = km
        # wheels = 5
        # self.battery = battery
        
       
    def get_km(self):
        print("This car has "+ str(self.km)+ "kilometers on it")
        print(Car.wheels)
        
        # print(f"{self.make}{self.model}has drivem {self.km}kilometers.")
        
    def run(self):
        print("car running")
        
class Audi(Car):
    def __init__(self,make,model,year,km):
        super().__init__(make,model,year,km)
        
    def run(self): #method overriding 
        print(self.make, "running")
        
class Skoda(Car):
     def __init__(self,make,model,year,km):
        super().__init__(make,model,year,km)
    
        
class VW(Car):
     def __init__(self,make,model,year,km):
        super().__init__(make,model,year,km)
        
     def run(self):
        print("VW is running!")
    
def createcars():
    audi = Audi("Audi", "A6", 2000, 200000.)
    skoda = Skoda("skoda", "octivia", 2010, 500000)
    vm = VW("VW", "passat", 2017, 100000.)
    print(audi.km+skoda.km+vm.km)
    audi.run()
    skoda.run()
    vm.run()
    
        
createcars()
    

        