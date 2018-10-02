class Animal:
    def __init__(self,name,health=100):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print(f"-----{self.name}-----\n  Health: {self.health}\n")
        return self
class Dog(Animal):
    def __init__(self,name="dog",health=150):
        super().__init__(name,health)
    def pet(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self,name="dragon",health=170):
        super().__init__(name,health)
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super().displayHealth()
        print(" I am a Dragon\n")
        return self


animal1 = Animal("zebra")
animal1.walk().walk().walk().run().run().displayHealth()
dog1 = Dog()
dog1.walk().run().pet().displayHealth()
dragon1 = Dragon()
dragon1.fly().fly().fly().displayHealth()

