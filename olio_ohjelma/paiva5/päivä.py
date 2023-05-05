class Car:
    def __init__(self, make, model, year, isElectric=False):
        self.make = make
        self.model = model
        self.year = year
        if isElectric or make == "Tesla":
            self.eCar = ElectricCar(make, model, year, True)
        else:
            self.eCar = ElectricCar(make, model, year, False)

class ElectricCar:
    def __init__(self, make, model, year, isTesla=True):
        self.make = make
        self.model = model
        self.year = year
        if isTesla:
            self.getTeslaInfo(True)
        else:
            self.getTeslaInfo(False)

    def getTeslaInfo(self, isTesla):
        if isTesla:
            print(f"{self.make} {self.model} {self.year} is a Tesla car.")
        else:
            print(f"{self.make} {self.model} {self.year} is an electric car, but not Tesla.")

# Example usage
myCar = Car("Tesla", "Model S", 2019)
myCar2 = Car("Electra", "Type X", 2000, True)
myCar3 = Car("Ford", "Focus", 2000)

    