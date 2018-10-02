class Bike:
    def __init__(self,name,price,max_speed):
        self.name = name
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print(f"{self.name}'s price is {self.price}. This bike has a max speed of {self.max_speed}. This bike has {self.miles} miles")
        return self
    def ride(self, num=1):
        print(f"Riding {self.name}\n" * num)
        self.miles += 10 * num
        return self
    def reverse(self, num=1):
        if self.miles <= 0:
            print("You cannot reverse anymore!")
        else:
            print(f"Reversing {self.name}\n" * num)
            self.miles -= 5 * num
        return self

Cougar = Bike("Cougar", "$15,000", "35mph")
Tiger = Bike("Tiger", "$2,000", "25mph")
Sloth = Bike("Sloth", "$20", "2mph")

Cougar.ride(3).reverse().displayInfo()
Tiger.ride(2).reverse(2).displayInfo()
Sloth.reverse(3).displayInfo()
