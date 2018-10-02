class Product:
    def __init__(self,price,item_name,weight,brand,status="for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
    def sell(self):
        self.status = "sold"
        return self
    def add(self,tax):
        self.price = round(self.price*(1 + tax))
        return self
    def returns(self,reason):
        if reason == "defective":
            self.status = reason
            self.price = 0
        elif reason == "like new":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "used"
            self.price -= round(self.price*.20)
        else:
            print("Please submit a valid reason: defective, like new, or opened")
        return self
    def displayInfo(self):
        print(f"------------------------\nItem Name: {self.item_name}\nPrice: ${self.price}\nWeight: {self.weight}lbs\nBrand: {self.brand}\nStatus: {self.status}\n------------------------\n")
        return self

product1 = Product(300,'iPhone',2,'Apple')
product2 = Product(30,'slinky',1,'ToyINC')
product3 = Product(300000,'X',500000000,'Tesla')

product1.sell().add(.25).displayInfo()
product2.returns("defective").displayInfo()
product3.returns("opened").displayInfo()