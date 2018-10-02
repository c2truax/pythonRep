class Human:
    def __init__(self):
        self.health = 5
        self.intelligence = 3
        self.strength = 2
        self.stealth = 1
class Wizard(Human):
    def __init__(self):
        super().__init__() # use super to call the Human __init__() method
        self.intelligence = 10 # every wizard starts off with 10 intelligence, overwriting the 3 from Human
    def heal(self):
        self.health += 10 # all wizards also get a heal() method
class Ninja(Human):
    def __init__(self):
        super().__init__() # use super to call the Human __init__() method
        self.stealth = 10 # every Ninja starts off with 10 stealth, overwriting the stealth of 1 from Human
    def steal(self):
        self.stealth += 5 # all ninjas also get a steal() method
class Samurai(Human):
    def __init__(self):
        super().__init__() # use super to call the Human __init__() method
        self.strength = 10 # every Samurai starts off with 10 strength, overwriting the 2 from Human
    def sacrifice(self):
        self.health -= 5 # all samurais also get a sacrifice() method
