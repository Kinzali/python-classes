class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year= year
    
    # def get_descriptive_name(self):
    #     long_name = f"{self.year}{self.make}{self.model}"
    #     return long_name.title()
    
    # def get_km(self):
    #     print("This car has "+ str(self.km)+ "kilometers on it")
    
class Battery:
    def __init__(self, battery_size = 100):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"This car has {self.battery_size} -kWh battery.")
    
    def upgrade_battery(self):
        print(f"This car has {self.battery_size} -kWh battery.")
        
        
    def get_range():
        pass
        
class ElectricCar (Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
        
    def fill_gas_tank(self):
        print("This car doesnot need a gas tank")
            
    #     def print_battery(self):
    #         print("75..")
            
        
    # tesla = ElectricCar()
    # tesla.battery.print_battery()
    # print(tesla.x)

ec = ElectricCar('Tesla', 'Model S', 2022)
ec.battery.describe_battery()
