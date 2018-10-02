class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.12 if self.price <= 10000 else 0.15
        self.display_all()
    def display_all(self):
        print(f"-------------------------\nCost: ${self.price}\nSpeed: {self.speed}mph\nFuel level: {self.fuel}\nMileage: {self.mileage}mpg\nTax: {self.tax}\n-------------------------\n")
        return self

Car1 = Car(2000,35,'Full',15)
Car2 = Car(2000,5,'Not Full',105)
Car3 = Car(2000,15,'Kind of Full',95)
Car4 = Car(2000,25,'Full',25)
Car5 = Car(2000,45,'Empty',25)
Car6 = Car(20000000,35,'Empty',15)